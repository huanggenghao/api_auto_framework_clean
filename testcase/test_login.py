# -*- coding: utf-8 -*-
# @Author : ben
# @Time : 2026/04/10 22:37
"""登录模块：data/login/login_endpoints.yaml + login_cases.yaml。"""
import allure

from common.case_data import build_parametrize_cases
from common.data_files import LOGIN_CASES_YAML, LOGIN_ENDPOINTS_YAML
from core.expect_util import apply_response_expectations


def pytest_generate_tests(metafunc):
    #metafunc.fixturenames:当前测试函数参数列表
    if "login_case" not in metafunc.fixturenames:
        return
    cases = build_parametrize_cases(LOGIN_ENDPOINTS_YAML, LOGIN_CASES_YAML)
    metafunc.parametrize("login_case", cases, ids=[c["case_no"] for c in cases])


@allure.feature("注册登录")
def test_login_flow_parametrized(login_case, login_service, log):
    """数据仅由 pytest_generate_tests → build_parametrize_cases 读盘一次，避免与 fixture 重复读 YAML。"""
    ek = login_case["endpoint_key"]

    allure.dynamic.title(f"[{login_case['case_no']}] {login_case['case_name']}")

    log.info(
        "POST caseNo=%s endpoint_key=%s repeat=%s"
        % (login_case["case_no"], ek, login_case["repeat_count"])
    )

    response = None
    for i in range(login_case["repeat_count"]):
        with allure.step(f"请求 {i + 1}/{login_case['repeat_count']}"):
            response = login_service.post(login_case["resolved_url"], login_case["req"])

    assert response is not None
    log.info("HTTP status=%s" % response.status_code)

    with allure.step("按 YAML expect 断言"):
        apply_response_expectations(response, login_case["expect"])
