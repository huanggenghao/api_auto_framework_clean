# -*- coding: utf-8 -*-
from api.login_api import LoginApi
from core.request_util import HttpClient


class LoginService:
    def __init__(self, http: HttpClient):
        self._api = LoginApi(http)

    def __getattr__(self, name):
        return getattr(self._api, name)
