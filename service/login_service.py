# -*- coding: utf-8 -*-
import requests

from api.login_api import LoginApi
from core.request_util import HttpClient


class LoginService:
    def __init__(self, http: HttpClient):
        self._api = LoginApi(http)

    def post(self, endpoint_key: str, body: dict) -> requests.Response:
        return self._api.post(endpoint_key, body)
