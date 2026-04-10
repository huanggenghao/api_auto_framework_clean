# -*- coding: utf-8 -*-
from pathlib import Path

from common.yaml_util import load_yaml

_CONFIG_DIR = Path(__file__).resolve().parent


def _load(name: str):
    return load_yaml(_CONFIG_DIR / name)


def get_settings():
    root = _load("config.yaml")
    env = root.get("active_env", "test")
    env_data = _load(f"{env}.yaml")
    merged = {**root, **env_data}
    merged["_env"] = env
    return merged
