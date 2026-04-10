# -*- coding: utf-8 -*-
import urllib3

from common.data_files import EARPHONE_YAML
from common.yaml_util import load_yaml
from core.cache_util import get_auth_token
from core.request_util import HttpClient

urllib3.disable_warnings()


def _data():
    return load_yaml(EARPHONE_YAML)


class EarphoneApi:
    def __init__(self, client: HttpClient):
        self._http = client

    def _headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "{}".format(get_auth_token()),
        }

    def earphone_information_flow(self, earphone_type):
        earphone_information_url = _data()["earphone_information"]
        idx_map = {
            925994607524962304: (0, "获取h5耳机说明书失败"),
            927442686274351104: (1, "获取t3 pro耳机说明书失败"),
            927443095978160128: (2, "获取h6 pro耳机说明书失败"),
            934671368550416384: (3, "获取p3耳机说明书失败"),
            925997015143538688: (4, "获取mac 5c耳机说明书失败"),
            925995115073495040: (5, "获取mac 5耳机说明书失败"),
            925994896852246528: (6, "获取t6耳机说明书失败"),
        }
        idx, err = idx_map[earphone_type]
        body = _data()["casedata"][idx][2]["reqParam"]
        response = self._http.post(
            url=earphone_information_url, json=body, headers=self._headers()
        )
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"{err}{response.status_code}"
