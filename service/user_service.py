# -*- coding: utf-8 -*-
import requests

from api.user_api import UserApi
from core.request_util import HttpClient


class UserService:
    def __init__(self, http: HttpClient):
        self._api = UserApi(http)

    def post_by_endpoint(self, endpoint_key: str, body: dict) -> requests.Response:
        return self._api.post_by_endpoint(endpoint_key, body)
