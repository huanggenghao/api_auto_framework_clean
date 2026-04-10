# -*- coding: utf-8 -*-
from api.message_api import MessageApi
from core.request_util import HttpClient


class MessageService:
    def __init__(self, http: HttpClient):
        self._api = MessageApi(http)

    def information_center(self, information_type, language):
        return self._api.information_center(information_type, language)
