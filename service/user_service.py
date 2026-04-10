# -*- coding: utf-8 -*-
from api.user_api import UserApi
from core.request_util import HttpClient


class UserService:
    """个人中心场景：委托 UserApi，便于 testcase 只依赖 service 层。"""

    def __init__(self, http: HttpClient):
        self._api = UserApi(http)

    def __getattr__(self, name):
        return getattr(self._api, name)
