# -*- coding: utf-8 -*-
import requests

from api.earphone_api import EarphoneApi
from core.request_util import HttpClient


class EarphoneService:
    def __init__(self, http: HttpClient):
        self._api = EarphoneApi(http)

    def post_product_manual(self, body: dict) -> requests.Response:
        return self._api.post_product_manual(body)
