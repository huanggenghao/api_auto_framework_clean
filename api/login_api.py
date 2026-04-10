# -*- coding: utf-8 -*-
import urllib3
import requests

from common.data_files import AUTH_ENDPOINTS_YAML
from common.yaml_util import load_yaml
from core.request_util import HttpClient

urllib3.disable_warnings()


def _endpoints():
    return load_yaml(AUTH_ENDPOINTS_YAML)


class LoginApi:
    def __init__(self, client: HttpClient):
        self._http = client

    def post(self, endpoint_key: str, body: dict) -> requests.Response:
        url = _endpoints()[endpoint_key]
        return self._http.post(url=url, json=body)
