# -*- coding: utf-8 -*-
import time
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests

from common.allure_util import attach_http_request, attach_http_response, mask_headers
from common.logger import get_http_logger
from config import get_settings
from core.exceptions import HttpClientError

# 默认重试：total=1 表示不重试；可在 config 的 http.retry 中覆盖
_DEFAULT_RETRY = {"total": 1, "backoff_seconds": 0.5, "retry_status_codes": [502, 503, 504]}


def _is_absolute_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


class HttpClient:
    """统一请求入口：base_url、headers、日志、Allure、重试、异常与超时/SSL。"""

    def __init__(
        self,
        session: Optional[requests.Session] = None,
        *,
        base_url: Optional[str] = None,
        default_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        use_allure: bool = True,
    ):
        cfg = get_settings().get("http", {})
        self.session = session or requests.Session()
        raw_base = base_url if base_url is not None else (cfg.get("base_url") or "")
        self._base_url = raw_base.rstrip("/")
        self._timeout = timeout if timeout is not None else float(cfg.get("timeout", 30))
        self._verify = cfg.get("verify_ssl", True)
        merged_headers: Dict[str, str] = {}
        for h in (cfg.get("default_headers") or {}, default_headers or {}):
            if isinstance(h, dict):
                merged_headers.update({str(k): str(v) for k, v in h.items()})
        self._default_headers = merged_headers
        self._use_allure = use_allure
        retry = {**_DEFAULT_RETRY, **(cfg.get("retry") or {})}
        self._retry_total = max(1, int(retry.get("total", 1)))
        self._retry_backoff = float(retry.get("backoff_seconds", 0.5))
        codes = retry.get("retry_status_codes")
        if codes is None:
            codes = [502, 503, 504]
        # 空列表：任意 5xx 均重试；非空：仅列表内状态码重试
        self._retry_all_5xx = len(codes) == 0
        self._retry_status_codes = set(int(x) for x in codes) if codes else set()
        self._log = get_http_logger()

    def _build_url(self, url: str) -> str:
        url = (url or "").strip()
        if not url:
            raise HttpClientError("请求 URL 为空", method="", url="")
        if _is_absolute_url(url):
            return url
        if not self._base_url:
            return url
        return urljoin(self._base_url + "/", url.lstrip("/"))

    def _merge_headers(self, headers: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        out: Dict[str, Any] = dict(self._default_headers)
        if headers:
            out.update(headers)
        return out

    def _should_retry_status(self, status: int) -> bool:
        if self._retry_all_5xx:
            return 500 <= status < 600
        return status in self._retry_status_codes

    def _single_call(
        self,
        method: str,
        url: str,
        final_headers: Dict[str, Any],
        kwargs: Dict[str, Any],
    ) -> requests.Response:
        kwargs = dict(kwargs)
        kwargs.setdefault("timeout", self._timeout)
        kwargs.setdefault("verify", self._verify)
        return self.session.request(
            method.upper(), url, headers=final_headers, **kwargs
        )

    def request(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[Dict[str, Any]] = None,
        attach_allure: Optional[bool] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """统一请求方法入口。"""
        final_url = self._build_url(url)
        do_allure = self._use_allure if attach_allure is None else attach_allure
        prep_headers = self._merge_headers(headers)
        safe_kw = {k: v for k, v in kwargs.items() if k in ("json", "data", "params")}

        if do_allure:
            attach_http_request(method.upper(), final_url, prep_headers, **safe_kw)

        self._log.info("%s %s", method.upper(), final_url)
        self._log.debug(
            "headers=%s kwargs=%s",
            mask_headers(prep_headers),
            list(kwargs.keys()),
        )

        last_exc: Optional[BaseException] = None
        last_response: Optional[requests.Response] = None

        for attempt in range(self._retry_total):
            t0 = time.perf_counter()
            try:
                resp = self._single_call(method, final_url, prep_headers, kwargs)
                elapsed_ms = (time.perf_counter() - t0) * 1000
                self._log.info(
                    "response status=%s elapsed_ms=%.1f attempt=%s/%s",
                    resp.status_code,
                    elapsed_ms,
                    attempt + 1,
                    self._retry_total,
                )
                if self._should_retry_status(resp.status_code) and attempt < self._retry_total - 1:
                    last_response = resp
                    self._log.warning(
                        "retry due to status=%s attempt=%s/%s",
                        resp.status_code,
                        attempt + 1,
                        self._retry_total,
                    )
                    time.sleep(self._retry_backoff * (attempt + 1))
                    continue
                if do_allure:
                    attach_http_response(resp)
                return resp
            except requests.Timeout as e:
                last_exc = e
                self._log.error("timeout %s %s attempt=%s/%s", method, final_url, attempt + 1, self._retry_total)
                if attempt < self._retry_total - 1:
                    time.sleep(self._retry_backoff * (attempt + 1))
                    continue
                raise HttpClientError(
                    f"请求超时: {method} {final_url}",
                    method=method,
                    url=final_url,
                ) from e
            except requests.RequestException as e:
                last_exc = e
                self._log.error("request error %s %s: %s", method, final_url, e)
                if attempt < self._retry_total - 1:
                    time.sleep(self._retry_backoff * (attempt + 1))
                    continue
                raise HttpClientError(
                    f"请求失败: {method} {final_url} — {e}",
                    method=method,
                    url=final_url,
                    response=last_response,
                ) from e

        if last_response is not None:
            return last_response
        if last_exc:
            raise HttpClientError(
                f"请求失败: {method} {final_url}",
                method=method,
                url=final_url,
            ) from last_exc
        raise HttpClientError("未知请求错误", method=method, url=final_url)

    def get(
        self,
        url: str,
        *,
        headers: Optional[Dict[str, Any]] = None,
        attach_allure: Optional[bool] = None,
        **kwargs: Any,
    ) -> requests.Response:
        return self.request("GET", url, headers=headers, attach_allure=attach_allure, **kwargs)

    def post(
        self,
        url: str,
        *,
        headers: Optional[Dict[str, Any]] = None,
        attach_allure: Optional[bool] = None,
        **kwargs: Any,
    ) -> requests.Response:
        return self.request("POST", url, headers=headers, attach_allure=attach_allure, **kwargs)

    def put(
        self,
        url: str,
        *,
        headers: Optional[Dict[str, Any]] = None,
        attach_allure: Optional[bool] = None,
        **kwargs: Any,
    ) -> requests.Response:
        return self.request("PUT", url, headers=headers, attach_allure=attach_allure, **kwargs)

    def patch(
        self,
        url: str,
        *,
        headers: Optional[Dict[str, Any]] = None,
        attach_allure: Optional[bool] = None,
        **kwargs: Any,
    ) -> requests.Response:
        return self.request("PATCH", url, headers=headers, attach_allure=attach_allure, **kwargs)

    def delete(
        self,
        url: str,
        *,
        headers: Optional[Dict[str, Any]] = None,
        attach_allure: Optional[bool] = None,
        **kwargs: Any,
    ) -> requests.Response:
        return self.request("DELETE", url, headers=headers, attach_allure=attach_allure, **kwargs)
