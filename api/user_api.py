# -*- coding: utf-8 -*-
import urllib3
import requests

from common.data_files import MINE_ENDPOINTS_YAML
from common.yaml_util import load_yaml
from core.cache_util import get_auth_token
from core.request_util import HttpClient

urllib3.disable_warnings()


def _endpoints():
    return load_yaml(MINE_ENDPOINTS_YAML)


class UserApi:
    def __init__(self, client: HttpClient):
        self._http = client

    def _headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "{}".format(get_auth_token()),
        }

    def post_by_endpoint(self, endpoint_key: str, body: dict) -> requests.Response:
        url = _endpoints()[endpoint_key]
        return self._http.post(url=url, json=body, headers=self._headers())
