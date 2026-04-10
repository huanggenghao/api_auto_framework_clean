# -*- coding: utf-8 -*-
import requests

from api.message_api import MessageApi
from core.request_util import HttpClient


class MessageService:
    def __init__(self, http: HttpClient):
        self._api = MessageApi(http)

    def post_message_all_read(self, body: dict) -> requests.Response:
        return self._api.post_message_all_read(body)
