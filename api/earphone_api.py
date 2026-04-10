# -*- coding: utf-8 -*-
import urllib3
import requests

from common.data_files import EARPHONE_ENDPOINTS_YAML
from common.yaml_util import load_yaml
from core.cache_util import get_auth_token
from core.request_util import HttpClient

urllib3.disable_warnings()


def _endpoints():
    return load_yaml(EARPHONE_ENDPOINTS_YAML)


class EarphoneApi:
    def __init__(self, client: HttpClient):
        self._http = client

    def _headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "{}".format(get_auth_token()),
        }

    def post_product_manual(self, body: dict) -> requests.Response:
        url = _endpoints()["product_manual"]
        return self._http.post(url=url, json=body, headers=self._headers())
