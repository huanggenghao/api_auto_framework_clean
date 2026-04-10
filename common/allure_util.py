# -*- coding: utf-8 -*-
import json
from typing import Any, Dict, Optional

import allure
import requests


def attach_json(name: str, data: Any) -> None:
    allure.attach(
        json.dumps(data, ensure_ascii=False, indent=2),
        name=name,
        attachment_type=allure.attachment_type.JSON,
    )


def attach_text(name: str, body: str) -> None:
    allure.attach(body, name=name, attachment_type=allure.attachment_type.TEXT)


def _try(fn) -> None:
    try:
        fn()
    except Exception:
        pass


def try_attach_json(name: str, data: Any) -> None:
    _try(lambda: attach_json(name, data))


def try_attach_text(name: str, body: str) -> None:
    _try(lambda: attach_text(name, body))


def mask_headers(headers: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not headers:
        return headers
    out = dict(headers)
    for k in list(out.keys()):
        lk = k.lower()
        if lk == "authorization" and out[k]:
            out[k] = "***"
    return out


def attach_http_request(
    method: str,
    url: str,
    headers: Optional[Dict[str, Any]] = None,
    **request_kwargs: Any,
) -> None:
    """统一记录请求上下文（敏感头已脱敏）。"""
    ctx: Dict[str, Any] = {"method": method, "url": url}
    if headers:
        ctx["headers"] = mask_headers(headers)
    for key in ("json", "data", "params"):
        if key in request_kwargs and request_kwargs[key] is not None:
            ctx[key] = request_kwargs[key]
    try_attach_json("HTTP 请求", ctx)


def attach_http_response(response: requests.Response, max_text: int = 50000) -> None:
    """统一记录响应：状态码、头、正文（过长截断）。"""
    text = response.text or ""
    if len(text) > max_text:
        text = text[:max_text] + "\n... [truncated]"
    hdr = {k: v for k, v in response.headers.items()}
    lines = [
        f"status_code: {response.status_code}",
        f"url: {response.url}",
        "headers: " + json.dumps(mask_headers(hdr) or {}, ensure_ascii=False),
        "body:",
        text,
    ]
    try_attach_text("HTTP 响应", "\n".join(lines))
