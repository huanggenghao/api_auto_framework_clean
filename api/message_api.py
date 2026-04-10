# -*- coding: utf-8 -*-
import urllib3

from common.data_files import MESSAGE_CENTER_YAML
from common.yaml_util import load_yaml
from core.cache_util import get_auth_token
from core.request_util import HttpClient

urllib3.disable_warnings()


def _data():
    return load_yaml(MESSAGE_CENTER_YAML)


class MessageApi:
    def __init__(self, client: HttpClient):
        self._http = client

    def _headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "{}".format(get_auth_token()),
        }

    def information_center(self, information_type, language):
        information_center_url = _data()["information_center"]
        key = (information_type, language)
        routes = {
            (1, "zh_CN"): (0, "系统通知全部已读失败"),
            (3, "zh_CN"): (1, "设备推送全部已读失败"),
            (4, "zh_CN"): (2, "设备分享全部已读失败"),
            (1, "en_US"): (3, "系统通知全部已读失败"),
            (3, "en_US"): (4, "设备推送全部已读失败"),
            (4, "en_US"): (5, "设备分享全部已读失败"),
        }
        idx, err = routes[key]
        body = _data()["casedata"][idx][2]["reqParam"]
        response = self._http.post(
            url=information_center_url, json=body, headers=self._headers()
        )
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"{err}{response.status_code}"
