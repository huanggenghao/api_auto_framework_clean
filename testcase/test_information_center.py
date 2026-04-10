# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/08/1
# @Author : huanggenghao
"""消息中心：endpoints.yaml + cases.yaml，每条 case 为单字典。"""
import allure

from common.case_data import build_parametrize_cases
from common.data_files import MESSAGE_CASES_YAML, MESSAGE_ENDPOINTS_YAML
from core.assert_util import assert_equal
from core.expect_util import apply_response_expectations


def pytest_generate_tests(metafunc):
    if "message_case" not in metafunc.fixturenames:
        return
    cases = build_parametrize_cases(MESSAGE_ENDPOINTS_YAML, MESSAGE_CASES_YAML)
    metafunc.parametrize("message_case", cases, ids=[c["case_no"] for c in cases])


@allure.feature("消息中心")
def test_message_all_read_parametrized(
    message_case, message_center_data, message_service, log
):
    assert_equal(
        message_case["resolved_url"],
        message_center_data["endpoints"][message_case["endpoint_key"]],
        "resolved_url 与 message_center_data.endpoints 不一致",
    )

    allure.dynamic.title(f"[{message_case['case_no']}] {message_case['case_name']}")
    allure.dynamic.parameter("type", message_case["req"].get("type"))
    allure.dynamic.parameter("lang", message_case["req"].get("lang"))

    log.info(
        "POST message/all/read caseNo=%s type=%s lang=%s",
        message_case["case_no"],
        message_case["req"].get("type"),
        message_case["req"].get("lang"),
    )

    with allure.step(f"POST（caseNo={message_case['case_no']}）"):
        response = message_service.post_message_all_read(message_case["req"])

    log.info("HTTP status=%s", response.status_code)

    with allure.step("按 YAML expect 断言"):
        apply_response_expectations(response, message_case["expect"])
