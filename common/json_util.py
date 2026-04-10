# -*- coding: utf-8 -*-
import json
from pathlib import Path
from typing import Any, Union


def load_json(path: Union[str, Path], encoding: str = "utf-8") -> Any:
    p = Path(path)
    with p.open("r", encoding=encoding) as f:
        return json.load(f)


def dump_json(path: Union[str, Path], data: Any, encoding: str = "utf-8", indent: int = 2) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
