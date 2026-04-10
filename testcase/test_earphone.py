# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/07/31
# @Author : huanggenghao
"""
耳机：接口地址 data/earphone/endpoints.yaml，用例列表 data/earphone/cases.yaml。
每条 case 为单个字典；与 conftest 中 earphone_data 同源。
"""
import allure

from common.case_data import build_parametrize_cases
from common.data_files import EARPHONE_CASES_YAML, EARPHONE_ENDPOINTS_YAML
from core.assert_util import assert_equal
from core.expect_util import apply_response_expectations


def pytest_generate_tests(metafunc):
    if "earphone_case" not in metafunc.fixturenames:
        return
    cases = build_parametrize_cases(EARPHONE_ENDPOINTS_YAML, EARPHONE_CASES_YAML)
    metafunc.parametrize("earphone_case", cases, ids=[c["case_no"] for c in cases])


@allure.feature("耳机说明书")
def test_product_manual_parametrized(earphone_case, earphone_data, earphone_service, log):
    assert_equal(
        earphone_case["resolved_url"],
        earphone_data["endpoints"][earphone_case["endpoint_key"]],
        "resolved_url 与 earphone_data.endpoints 不一致",
    )

    case_no = earphone_case["case_no"]
    case_name = earphone_case["case_name"]
    req = earphone_case["req"]
    expect = earphone_case["expect"] or {"http_status": 200, "tip": "Success！"}

    allure.dynamic.title(f"[{case_no}] {case_name}")
    allure.dynamic.parameter("productId", req.get("productId"))
    allure.dynamic.parameter("expect", str(expect))

    log.info(
        "POST product_manual caseNo=%s productId=%s lang=%s url=%s",
        case_no,
        req.get("productId"),
        req.get("lang"),
        earphone_case["resolved_url"],
    )

    with allure.step(f"POST product/manual（caseNo={case_no}）"):
        response = earphone_service.post_product_manual(req)

    log.info("HTTP status=%s body_len=%s", response.status_code, len(response.text or ""))

    with allure.step("按 YAML expect 断言"):
        apply_response_expectations(response, expect)
