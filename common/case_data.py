# -*- coding: utf-8 -*-
"""用例 YAML 约定：endpoints 与 cases 分离；每条 case 为单个字典。"""
from pathlib import Path
from typing import Any, Dict, List, MutableMapping, Union

from common.yaml_util import load_yaml


def load_endpoints(path: Union[str, Path]) -> Dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise ValueError(f"endpoints 文件应为字典: {path}")
    return data


def load_cases_list(path: Union[str, Path]) -> List[MutableMapping[str, Any]]:
    raw = load_yaml(path)
    if isinstance(raw, dict) and "cases" in raw:
        cases = raw["cases"]
    elif isinstance(raw, list):
        cases = raw
    else:
        raise ValueError(f"cases 文件应为 {{cases: [...]}} 或列表: {path}")
    if not isinstance(cases, list):
        raise ValueError(f"cases 必须为列表: {path}")
    return cases


def resolve_case_urls(
    case: MutableMapping[str, Any],
    endpoints: Dict[str, Any],
) -> Dict[str, Any]:
    """校验 endpoint 键存在，并附上 resolved_url。"""
    ek = case.get("endpoint")
    if not ek:
        raise KeyError("case 缺少 endpoint 字段（对应 endpoints.yaml 中的键）")
    if ek not in endpoints:
        raise KeyError(f"endpoints 中未定义键 {ek!r}，已有: {list(endpoints.keys())}")
    url = endpoints[ek]
    if not url:
        raise ValueError(f"endpoint {ek!r} 的 URL 为空")
    out = dict(case)
    out["endpoint_key"] = ek
    out["resolved_url"] = url
    return out


def build_parametrize_cases(
    endpoints_path: Union[str, Path],
    cases_path: Union[str, Path],
) -> List[Dict[str, Any]]:
    """供 pytest_generate_tests：每条 case 一个 dict，含 resolved_url、repeat_count 等。"""
    ep = load_endpoints(endpoints_path)
    out: List[Dict[str, Any]] = []
    for c in load_cases_list(cases_path):
        r = resolve_case_urls(c, ep)
        out.append(
            {
                "case_no": str(c["caseNo"]),
                "case_name": c["caseName"],
                "endpoint_key": r["endpoint_key"],
                "req": c["request"],
                "expect": dict(c.get("expect") or {}),
                "resolved_url": r["resolved_url"],
                "repeat_count": int(c.get("repeat_count", 1)),
            }
        )
    return out
