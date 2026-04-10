# -*- coding: utf-8 -*-
# @Author : huanggenghao
# @Time : 2024/7/31 15:09

import allure
import pytest
import requests
from unittest.mock import patch

from common.data_files import REGISTER_LOGIN_YAML
from common.yaml_util import load_yaml


@pytest.fixture
def registration_ctx():
    return {
        "merchantId": "100000000000000000",
        "account": "15992213991",
        "password": "abcd1234",
        "lang": "zh_CN",
    }


def _login_data():
    return load_yaml(REGISTER_LOGIN_YAML)


def _perform_user_flow(ctx, operation_type, mock_post):
    merchant_id = ctx["merchantId"]
    account = ctx["account"]
    password = ctx["password"]
    lang = ctx["lang"]
    data = _login_data()

    get_code_url = data["code_url"]
    get_code_params = {
        "merchantId": merchant_id,
        "account": account,
        "type": operation_type,
        "lang": lang,
    }

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "message": "Verification code sent successfully"
    }

    get_code_response = requests.post(get_code_url, params=get_code_params)
    assert get_code_response.status_code == 200, "Failed to get verification code"
    confirmation_data = get_code_response.json()
    assert "message" in confirmation_data, "No confirmation message in response"

    verification_code = "mock_verification_code"

    if operation_type == "REGISTER":
        register_url = data["register_url"]
        register_payload = {
            "merchantId": merchant_id,
            "account": account,
            "code": verification_code,
            "password": password,
        }
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "message": "User registered successfully"
        }
        register_response = requests.post(register_url, json=register_payload)
        assert register_response.status_code == 201, "Failed to register user"
        register_data = register_response.json()
        assert "message" in register_data, "No registration success message in response"

    elif operation_type == "PWD_RESET":
        reset_password_url = data["reset_password"]
        reset_payload = {
            "merchantId": merchant_id,
            "account": account,
            "code": verification_code,
            "password": password,
        }
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "message": "User reset password successfully"
        }
        reset_password_url_response = requests.post(reset_password_url, json=reset_payload)
        assert reset_password_url_response.status_code == 201, "Failed to reset password"
        reset_password_url_data = reset_password_url_response.json()
        assert "message" in reset_password_url_data, "No reset password success message in response"

    elif operation_type == "LOGOFF":
        user_logoff_url = data["user_logoff"]
        logoff_payload = {
            "merchantId": merchant_id,
            "account": account,
            "code": verification_code,
            "password": password,
        }
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "message": "User logoff account successfully"
        }
        user_logoff_url_response = requests.post(user_logoff_url, json=logoff_payload)
        assert user_logoff_url_response.status_code == 201, "Failed to logoff account"
        user_logoff_url_data = user_logoff_url_response.json()
        assert "message" in user_logoff_url_data, "No logoff account success  in response"

    elif operation_type == "LOGIN":
        user_login_url = data["login_code"]
        login_payload = {
            "merchantId": merchant_id,
            "account": account,
            "code": verification_code,
        }
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "message": "User LOGIN account successfully"
        }
        user_login_url_response = requests.post(user_login_url, json=login_payload)
        assert user_login_url_response.status_code == 201, "Failed to LOGIN account"
        user_login_url_data = user_login_url_response.json()
        assert "message" in user_login_url_data, "No LOGIN account success  in response"


@allure.feature("Mock")
@allure.title("模拟获取验证码注册账号")
@patch("requests.post")
def test_user_register(mock_post, registration_ctx):
    _perform_user_flow(registration_ctx, "REGISTER", mock_post)


@allure.feature("Mock")
@allure.title("模拟获取验证码重置账号")
@patch("requests.post")
def test_user_reset(mock_post, registration_ctx):
    _perform_user_flow(registration_ctx, "PWD_RESET", mock_post)


@allure.feature("Mock")
@allure.title("模拟获取验证码注销账号")
@patch("requests.post")
def test_user_logoff(mock_post, registration_ctx):
    _perform_user_flow(registration_ctx, "LOGOFF", mock_post)


@allure.feature("Mock")
@allure.title("模拟获取验证码登陆账号")
@patch("requests.post")
def test_user_login(mock_post, registration_ctx):
    _perform_user_flow(registration_ctx, "LOGIN", mock_post)
