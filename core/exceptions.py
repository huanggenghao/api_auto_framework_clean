# -*- coding: utf-8 -*-
from typing import Optional

import requests


class HttpClientError(Exception):
    """统一 HTTP 客户端异常：网络错误、超时、重试耗尽等。"""

    def __init__(
        self,
        message: str,
        *,
        method: str = "",
        url: str = "",
        response: Optional[requests.Response] = None,
    ):
        super().__init__(message)
        self.method = method
        self.url = url
        self.response = response

    def status_code(self) -> Optional[int]:
        return self.response.status_code if self.response is not None else None
