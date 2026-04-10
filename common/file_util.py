# -*- coding: utf-8 -*-
"""项目根目录与 data 路径。"""
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def data_path(*parts: str) -> Path:
    return project_root().joinpath("data", *parts)


def read_text(rel_under_root: str, encoding: str = "utf-8") -> str:
    p = project_root() / rel_under_root
    return p.read_text(encoding=encoding)


def write_text(rel_under_root: str, content: str, encoding: str = "utf-8") -> None:
    p = project_root() / rel_under_root
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding=encoding)
