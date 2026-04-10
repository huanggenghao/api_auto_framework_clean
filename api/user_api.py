# -*- coding: utf-8 -*-
import urllib3

from common.data_files import USER_MINE_YAML
from common.yaml_util import load_yaml
from core.cache_util import get_auth_token
from core.request_util import HttpClient

urllib3.disable_warnings()


def _data():
    return load_yaml(USER_MINE_YAML)


class UserApi:
    def __init__(self, client: HttpClient):
        self._http = client

    def _headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "{}".format(get_auth_token()),
        }

    def update_user_data(self):
        base_url = _data()["user_update_url"]
        body = _data()["casedata"][0][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success":
            return response.json()["tip"]
        return f"更新用户信息失败{response.status_code}"

    def update_user_data_null(self):
        base_url = _data()["user_update_url"]
        body = _data()["casedata"][1][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Fail":
            return response.json()["tip"]
        return f"更新用户信息为空{response.status_code}"

    def update_user_data_one(self):
        base_url = _data()["user_update_url"]
        body = _data()["casedata"][2][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Fail":
            return response.json()["tip"]
        return f"更新用户信息为空{response.status_code}"

    def update_user_data_enought(self):
        base_url = _data()["user_update_url"]
        body = _data()["casedata"][3][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Fail":
            return response.json()["tip"]
        return f"更新用户信息失败{response.status_code}"

    def update_user_avatar_success(self):
        base_url = _data()["user_update_url"]
        body = _data()["casedata"][4][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success":
            return response.json()["tip"]
        return f"更新用户头像失败{response.status_code}"

    def update_user_avatar_null(self):
        base_url = _data()["user_update_url"]
        body = _data()["casedata"][5][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success":
            return response.json()["tip"]
        return f"更新用户头像失败{response.status_code}"

    def update_user_avatar_third(self):
        base_url = _data()["user_update_url"]
        body = _data()["casedata"][6][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success":
            return response.json()["tip"]
        return f"更新用户头像失败{response.status_code}"

    def push_switch_list(self):
        base_url = _data()["push_switch_list"]
        body = _data()["casedata"][7][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        js = response.json()
        if (
            js["list"][0]["switchStatus"] is True
            and js["list"][1]["switchStatus"] is False
            and js["list"][2]["switchStatus"] is False
        ):
            return js["tip"]
        return f"获取推送列表的初始状态与默认不一致{js['list']}"

    def push_switch_update(self):
        base_url = _data()["push_switch_update"]
        body = _data()["casedata"][8][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"设置设备推送开关为开{response.json()}"

    def push_switch_update_01(self):
        base_url = _data()["push_switch_update"]
        body = _data()["casedata"][9][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"设置设备推送开关为开{response.json()}"

    def push_switch_update_02(self):
        base_url = _data()["push_switch_update"]
        body = _data()["casedata"][10][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"设置设备推送开关为开{response.json()}"

    def check_version_update_android_china(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][11][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"检测不到版本，存在问题{response.json()}"

    def check_version_update_android_china_invail(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][12][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "当前版本已经是最新！":
            return response.json()["tip"]
        return f"当前版本已是最新版本，不会有提示{response.json()}"

    def check_version_update_android_china_error(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][13][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "应用版本比较异常！":
            return response.json()["tip"]
        return f"当前版本检测存在问题{response.json()}"

    def check_version_update_android_english(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][14][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"设置设备推送开关为开{response.json()}"

    def check_version_update_android_english_invail(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][15][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "当前版本已经是最新！":
            return response.json()["tip"]
        return f"当前版本检测存在问题{response.json()}"

    def check_version_update_android_english_error(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][16][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "应用版本比较异常！":
            return response.json()["tip"]
        return f"当前版本检测存在问题{response.json()}"

    def check_version_update_ios_china(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][17][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"检测不到新版本{response.json()}"

    def check_version_update_ios_china_invail(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][18][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "当前版本已经是最新！":
            return response.json()["tip"]
        return f"当前版本检测存在问题{response.json()}"

    def check_version_update_ios_china_error(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][19][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "应用版本比较异常！":
            return response.json()["tip"]
        return f"当前版本检测存在问题{response.json()}"

    def check_version_update_ios_english(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][20][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "Success！":
            return response.json()["tip"]
        return f"检测不到新版本{response.json()}"

    def check_version_update_ios_english_invail(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][21][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "当前版本已经是最新！":
            return response.json()["tip"]
        return f"当前版本检测存在问题{response.json()}"

    def check_version_update_ios_english_error(self):
        base_url = _data()["check_version_update"]
        body = _data()["casedata"][22][2]["reqParam"]
        response = self._http.post(url=base_url, json=body, headers=self._headers())
        if response.json()["tip"] == "应用版本比较异常！":
            return response.json()["tip"]
        return f"当前版本检测存在问题{response.json()}"
