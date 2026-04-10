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

from common.data_files import (
    EARPHONE_YAML,
    MESSAGE_CENTER_YAML,
    REGISTER_LOGIN_YAML,
    USER_MINE_YAML,
)
from common.logger import Log
from common.yaml_util import load_yaml
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
    with allure.step("读取 register_login.yaml"):
        return load_yaml(REGISTER_LOGIN_YAML)


@pytest.fixture
def earphone_data():
    with allure.step("读取 earphone.yaml"):
        return load_yaml(EARPHONE_YAML)


@pytest.fixture
def user_mine_data():
    with allure.step("读取 mine.yaml"):
        return load_yaml(USER_MINE_YAML)


@pytest.fixture
def message_center_data():
    with allure.step("读取 information_center.yaml"):
        return load_yaml(MESSAGE_CENTER_YAML)


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
