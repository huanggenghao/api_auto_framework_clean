# -*- coding: utf-8 -*-
import urllib3

from common.data_files import REGISTER_LOGIN_YAML
from common.yaml_util import load_yaml
from core.request_util import HttpClient

urllib3.disable_warnings()


def _data():
    return load_yaml(REGISTER_LOGIN_YAML)


class LoginApi:
    def __init__(self, client: HttpClient):
        self._http = client

    def check_login_passage_error(self):
        base_url = _data()["login_url"]
        body = _data()["casedata"][0][2]["reqParam"]
        res2 = self._http.post(url=base_url, json=body)
        if res2.json()["code"] == 20006:
            return res2.json()["code"]
        return f"The result did not meet expectations{res2.status_code}"

    def check_login_passage_null(self):
        base_url = _data()["login_url"]
        body = _data()["casedata"][1][2]["reqParam"]
        res2 = self._http.post(url=base_url, json=body)
        if res2.json()["code"] == 10010:
            return res2.json()["code"]
        return f"The result did not meet expectations{res2.status_code}"

    def check_login_passage_exist(self):
        base_url = _data()["login_url"]
        body = _data()["casedata"][2][2]["reqParam"]
        res2 = self._http.post(url=base_url, json=body)
        if res2.json()["code"] == 40008:
            return res2.json()["code"]
        return f"The result did not meet expectations{res2.status_code}"

    def check_login_passage_success(self):
        base_url = _data()["jp_login"]
        body = _data()["casedata"][8][2]["reqParam"]
        res2 = self._http.post(url=base_url, json=body)
        if res2.json()["code"] == 0:
            return res2.json()["code"]
        return f"The result did not meet expectations{res2.status_code}"

    def exchange_country_list(self):
        base_url = _data()["exchange_country_list"]
        body = _data()["casedata"][9][2]["reqParam"]
        res2 = self._http.post(url=base_url, json=body)
        if res2.json()["list"][0]["country"] == "日本":
            return res2.json()["list"][0]["country"]
        return f"The result did not meet expectations{res2.status_code}"
