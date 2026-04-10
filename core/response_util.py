# -*- coding: utf-8 -*-
from typing import Any, Dict, Union

import requests

from core.assert_util import assert_equal

_MISSING = object()


def as_json(response: requests.Response) -> Dict[str, Any]:
    return response.json()


def get_code(response: requests.Response) -> Any:
    return as_json(response).get("code")


def get_tip(response: requests.Response) -> Any:
    return as_json(response).get("tip")


def assert_status(
    response: requests.Response,
    expected: int = 200,
    msg: str = "",
) -> None:
    """统一校验 HTTP 状态码。"""
    assert_equal(
        response.status_code,
        expected,
        msg or f"HTTP 状态码期望 {expected}，实际 {response.status_code}",
    )


def assert_json_field(
    response: requests.Response,
    key: str,
    expected: Any,
    msg: str = "",
) -> None:
    """校验响应 JSON 顶层字段。"""
    body = as_json(response)
    actual = body.get(key)
    assert_equal(
        actual,
        expected,
        msg or f"字段 {key!r} 期望 {expected!r}，实际 {actual!r}",
    )


def json_path_get(obj: Any, path: str, default: Any = None) -> Any:
    """
    点分路径读取 dict 嵌套字段，不支持数组下标。
    例：json_path_get(d, "info.token")
    """
    cur: Any = obj
    for part in path.split("."):
        if not part:
            continue
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def json_path_lookup(obj: Any, path: str, default: Any = None) -> Any:
    """
    点分路径，段为纯数字时按 list 下标访问。
    例：list.0.country -> obj["list"][0]["country"]
    """
    cur: Any = obj
    for part in path.split("."):
        if not part:
            continue
        if cur is None:
            return default
        if part.isdigit():
            idx = int(part)
            if isinstance(cur, (list, tuple)) and 0 <= idx < len(cur):
                cur = cur[idx]
            else:
                return default
        elif isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def assert_json_path(
    response: requests.Response,
    path: str,
    expected: Any,
    msg: str = "",
) -> None:
    """按点分路径校验 JSON 字段。"""
    body = as_json(response)
    actual = json_path_get(body, path, default=_MISSING)
    if actual is _MISSING:
        raise AssertionError(msg or f"JSON 路径不存在: {path!r}")
    assert_equal(
        actual,
        expected,
        msg or f"路径 {path!r} 期望 {expected!r}，实际 {actual!r}",
    )


def assert_json_path_exists(response: requests.Response, path: str, msg: str = "") -> Any:
    """断言路径存在并返回值。"""
    body = as_json(response)
    actual = json_path_get(body, path, default=_MISSING)
    if actual is _MISSING:
        raise AssertionError(msg or f"JSON 路径不存在: {path!r}")
    return actual


def assert_json_contains_keys(
    response: requests.Response,
    keys: Union[list, tuple],
    msg: str = "",
) -> None:
    """断言顶层包含若干 key。"""
    body = as_json(response)
    missing = [k for k in keys if k not in body]
    assert_equal(
        missing,
        [],
        msg or f"响应 JSON 缺少字段: {missing}",
    )
