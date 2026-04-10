# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/07/26
# @Author : huanggenghao
"""个人中心：mine_endpoints.yaml + mine_cases.yaml。"""
import allure

from common.case_data import build_parametrize_cases
from common.data_files import MINE_CASES_YAML, MINE_ENDPOINTS_YAML
from core.assert_util import assert_equal
from core.expect_util import apply_response_expectations


def pytest_generate_tests(metafunc):
    if "mine_case" not in metafunc.fixturenames:
        return
    cases = build_parametrize_cases(MINE_ENDPOINTS_YAML, MINE_CASES_YAML)
    metafunc.parametrize("mine_case", cases, ids=[c["case_no"] for c in cases])


@allure.feature("个人中心")
def test_mine_flow_parametrized(mine_case, user_mine_data, user_service, log):
    ek = mine_case["endpoint_key"]
    assert_equal(
        mine_case["resolved_url"],
        user_mine_data["endpoints"][ek],
        "resolved_url 与 user_mine_data.endpoints 不一致",
    )

    allure.dynamic.title(f"[{mine_case['case_no']}] {mine_case['case_name']}")
    allure.dynamic.parameter("endpoint_key", ek)
    allure.dynamic.parameter("repeat", mine_case["repeat_count"])

    log.info(
        "POST caseNo=%s endpoint_key=%s repeat=%s",
        mine_case["case_no"],
        ek,
        mine_case["repeat_count"],
    )

    response = None
    for i in range(mine_case["repeat_count"]):
        with allure.step(f"请求 {i + 1}/{mine_case['repeat_count']}"):
            response = user_service.post_by_endpoint(ek, mine_case["req"])

    assert response is not None
    log.info("HTTP status=%s", response.status_code)

    with allure.step("按 YAML expect 断言"):
        apply_response_expectations(response, mine_case["expect"])
