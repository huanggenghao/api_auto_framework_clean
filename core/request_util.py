# -*- coding: utf-8 -*-
from typing import Any, Optional

import requests

from config import get_settings


class HttpClient:
    """requests.Session 轻量封装，统一超时等参数。"""

    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self._timeout = get_settings().get("http", {}).get("timeout", 30)

    def post(self, url: str, **kwargs: Any) -> requests.Response:
        kwargs.setdefault("timeout", self._timeout)
        return self.session.post(url, **kwargs)

    def get(self, url: str, **kwargs: Any) -> requests.Response:
        kwargs.setdefault("timeout", self._timeout)
        return self.session.get(url, **kwargs)
