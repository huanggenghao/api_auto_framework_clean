# -*- coding: utf-8 -*-
from common.data_files import REGISTER_LOGIN_YAML
from common.yaml_util import load_yaml
from core.request_util import HttpClient

_http = HttpClient()


def _d():
    return load_yaml(REGISTER_LOGIN_YAML)


def register_code_fail():
    register_url = _d()["register_url"]
    body = _d()["casedata"][3][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40024:
        return response.json()["code"]
    return f"The code did not meet expectations{response.status_code}"


def register_code_null():
    register_url = _d()["register_url"]
    body = _d()["casedata"][4][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 10010:
        return response.json()["code"]
    return f"Code cannot be empty{response.status_code}"


def register_phone_repeat():
    code_url = _d()["code_url"]
    body = _d()["casedata"][5][2]["reqParam"]
    response = _http.post(url=code_url, json=body)
    if response.json()["code"] == 40030:
        return response.json()["code"]
    return f"结果不符合预期{response.status_code}"


def register_check_phone():
    register_url = _d()["code_url"]
    body = _d()["casedata"][6][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40030:
        return response.json()["code"]
    return f"结果不符合预期{response.status_code}"


def repeat_code():
    register_url = _d()["code_url"]
    body = _d()["casedata"][7][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40032:
        return response.json()["code"]
    return f"获取验证码时间不符合限制1分钟{response.status_code}"


def Jp_register_code_fail():
    register_url = _d()["jp_register"]
    body = _d()["casedata"][10][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40024:
        return response.json()["code"]
    return f"The code did not meet expectations{response.status_code}"


def Jp_get_email_code():
    register_url = _d()["Jp_code_get"]
    body = _d()["casedata"][11][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["tip"] == "Success！":
        return response.json()["tip"]
    return f"The code did not meet expectations{response.status_code}"


def Jp_email_repeat():
    register_url = _d()["Jp_code_get"]
    body = _d()["casedata"][12][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40030:
        return response.json()["code"]
    return f"The code did not meet expectations{response.status_code}"


def Jp_email_maxtime():
    register_url = _d()["Jp_code_get"]
    body = _d()["casedata"][13][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40045:
        return response.json()["code"]
    return f"The code did not meet expectations{response.status_code}"


def email_repeat_code():
    register_url = _d()["Jp_code_get"]
    body = _d()["casedata"][14][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40032:
        return response.json()["code"]
    return f"获取验证码时间不符合限制1分钟{response.status_code}"


def email_pwd_reset_isregister():
    register_url = _d()["Jp_code_get"]
    body = _d()["casedata"][15][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40008:
        return response.json()["code"]
    return f"该邮箱已注册{response.status_code}"


def email_pwd_reset_get_code():
    register_url = _d()["Jp_code_get"]
    body = _d()["casedata"][16][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["tip"] == "Success！":
        return response.json()["tip"]
    return f"The code did not meet expectations{response.status_code}"


def email_pwd_reset_repeat_code():
    register_url = _d()["Jp_code_get"]
    body = _d()["casedata"][17][2]["reqParam"]
    response = _http.post(url=register_url, json=body)
    if response.json()["code"] == 40032:
        return response.json()["code"]
    return f"获取验证码时间不符合限制1分钟{response.status_code}"


def pwd_reset_phone_isregister():
    pwd_reset_url = _d()["code_url"]
    body = _d()["casedata"][18][2]["reqParam"]
    response = _http.post(url=pwd_reset_url, json=body)
    if response.json()["code"] == 40008:
        return response.json()["code"]
    return f"该邮箱已注册{response.status_code}"


def pwd_reset_get_code():
    pwd_reset_url = _d()["code_url"]
    body = _d()["casedata"][19][2]["reqParam"]
    response = _http.post(url=pwd_reset_url, json=body)
    if response.json()["tip"] == "Success！":
        return response.json()["tip"]
    return f"The code did not meet expectations{response.status_code}"


def pwd_reset_repeat_code():
    pwd_reset_url = _d()["code_url"]
    body = _d()["casedata"][20][2]["reqParam"]
    response = _http.post(url=pwd_reset_url, json=body)
    if response.json()["code"] == 40032:
        return response.json()["code"]
    return f"获取验证码时间不符合限制1分钟{response.status_code}"
