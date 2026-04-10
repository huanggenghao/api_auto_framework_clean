# -*- coding: utf-8 -*-
from typing import Optional

from config import get_settings
from core.request_util import HttpClient

_token: Optional[str] = None


def get_auth_token() -> str:
    global _token
    if _token:
        return _token
    cfg = get_settings()
    auth = cfg.get("auth", {})
    body = {
        "account": auth.get("login_account"),
        "password": auth.get("login_password"),
        "merchantId": auth.get("merchant_id"),
        "phoneCode": auth.get("phone_code", "86"),
    }
    url = auth.get("login_url")
    client = HttpClient()
    response = client.post(url, json=body)
    _token = response.json()["info"]["token"]
    return _token


def clear_auth_token() -> None:
    global _token
    _token = None
