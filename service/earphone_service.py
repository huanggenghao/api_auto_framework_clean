# -*- coding: utf-8 -*-
from api.earphone_api import EarphoneApi
from core.request_util import HttpClient


class EarphoneService:
    def __init__(self, http: HttpClient):
        self._api = EarphoneApi(http)

    def earphone_information_flow(self, earphone_type: int):
        return self._api.earphone_information_flow(earphone_type)
