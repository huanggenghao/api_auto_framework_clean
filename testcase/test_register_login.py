# -*- coding: utf-8 -*-
# @Author : ben
# @Time : 2024/7/23 10:32
"""登录注册：auth_endpoints.yaml + auth_cases.yaml。"""
import allure

from common.case_data import build_parametrize_cases
from common.data_files import AUTH_CASES_YAML, AUTH_ENDPOINTS_YAML
from core.assert_util import assert_equal
from core.expect_util import apply_response_expectations


def pytest_generate_tests(metafunc):
    if "auth_case" not in metafunc.fixturenames:
        return
    cases = build_parametrize_cases(AUTH_ENDPOINTS_YAML, AUTH_CASES_YAML)
    metafunc.parametrize("auth_case", cases, ids=[c["case_no"] for c in cases])


@allure.feature("注册登录")
def test_auth_flow_parametrized(auth_case, register_login_data, login_service, log):
    ek = auth_case["endpoint_key"]
    assert_equal(
        auth_case["resolved_url"],
        register_login_data["endpoints"][ek],
        "resolved_url 与 register_login_data.endpoints 不一致",
    )

    allure.dynamic.title(f"[{auth_case['case_no']}] {auth_case['case_name']}")
    allure.dynamic.parameter("endpoint_key", ek)
    allure.dynamic.parameter("repeat", auth_case["repeat_count"])

    log.info(
        "POST caseNo=%s endpoint_key=%s repeat=%s",
        auth_case["case_no"],
        ek,
        auth_case["repeat_count"],
    )

    response = None
    for i in range(auth_case["repeat_count"]):
        with allure.step(f"请求 {i + 1}/{auth_case['repeat_count']}"):
            response = login_service.post(ek, auth_case["req"])

    assert response is not None
    log.info("HTTP status=%s", response.status_code)

    with allure.step("按 YAML expect 断言"):
        apply_response_expectations(response, auth_case["expect"])
