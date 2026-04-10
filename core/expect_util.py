# -*- coding: utf-8 -*-
from typing import Any, Dict

import requests

from core.assert_util import assert_equal
from core.response_util import as_json, assert_json_field, assert_status, json_path_lookup


def apply_response_expectations(response: requests.Response, expect: Dict[str, Any]) -> None:
    """
    按 YAML expect 块统一断言。
    支持: http_status, tip, code, list_switch_status, json_equals(点分路径，支持 list 下标)。
    """
    assert_status(response, int(expect.get("http_status", 200)))
    if "tip" in expect:
        assert_json_field(response, "tip", expect["tip"])
    if "code" in expect:
        assert_json_field(response, "code", expect["code"])

    need_body = "list_switch_status" in expect or "json_equals" in expect
    if not need_body:
        return

    body = as_json(response)
    if "list_switch_status" in expect:
        expected_list = expect["list_switch_status"]
        for i, exp in enumerate(expected_list):
            assert_equal(
                body["list"][i]["switchStatus"],
                exp,
                f"list[{i}].switchStatus 期望 {exp!r}",
            )
    if "json_equals" in expect:
        for path, val in expect["json_equals"].items():
            actual = json_path_lookup(body, path)
            assert_equal(
                actual,
                val,
                f"JSON 路径 {path!r} 期望 {val!r}，实际 {actual!r}",
            )
