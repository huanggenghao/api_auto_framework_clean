# -*- coding: utf-8 -*-
from typing import Any


def assert_equal(actual: Any, expected: Any, msg: str = "") -> None:
    assert actual == expected, msg or f"expected {expected!r}, got {actual!r}"
