# -*- coding: utf-8 -*-
import sys
import warnings
from pathlib import Path

import allure
import pytest
import requests

_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from common.case_data import load_cases_list, load_endpoints
from common.data_files import (
    AUTH_CASES_YAML,
    AUTH_ENDPOINTS_YAML,
    EARPHONE_CASES_YAML,
    EARPHONE_ENDPOINTS_YAML,
    MESSAGE_CASES_YAML,
    MESSAGE_ENDPOINTS_YAML,
    MINE_CASES_YAML,
    MINE_ENDPOINTS_YAML,
)
from common.logger import Log
from core.request_util import HttpClient
from service.earphone_service import EarphoneService
from service.login_service import LoginService
from service.message_service import MessageService
from service.user_service import UserService


@pytest.fixture(scope="session")
def log():
    return Log()


@pytest.fixture
def api_session():
    warnings.simplefilter("ignore", ResourceWarning)
    return requests.session()


@pytest.fixture
def http_client(api_session):
    return HttpClient(api_session)


@pytest.fixture
def register_login_data():
    with allure.step("读取 login/auth_endpoints.yaml + auth_cases.yaml"):
        return {
            "endpoints": load_endpoints(AUTH_ENDPOINTS_YAML),
            "cases": load_cases_list(AUTH_CASES_YAML),
        }


@pytest.fixture
def earphone_data():
    with allure.step("读取 earphone/endpoints.yaml + cases.yaml"):
        return {
            "endpoints": load_endpoints(EARPHONE_ENDPOINTS_YAML),
            "cases": load_cases_list(EARPHONE_CASES_YAML),
        }


@pytest.fixture
def user_mine_data():
    with allure.step("读取 user/mine_endpoints.yaml + mine_cases.yaml"):
        return {
            "endpoints": load_endpoints(MINE_ENDPOINTS_YAML),
            "cases": load_cases_list(MINE_CASES_YAML),
        }


@pytest.fixture
def message_center_data():
    with allure.step("读取 message/endpoints.yaml + cases.yaml"):
        return {
            "endpoints": load_endpoints(MESSAGE_ENDPOINTS_YAML),
            "cases": load_cases_list(MESSAGE_CASES_YAML),
        }


@pytest.fixture
def earphone_service(http_client):
    return EarphoneService(http_client)


@pytest.fixture
def login_service(http_client):
    return LoginService(http_client)


@pytest.fixture
def message_service(http_client):
    return MessageService(http_client)


@pytest.fixture
def user_service(http_client):
    return UserService(http_client)
