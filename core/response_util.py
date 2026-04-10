# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional

import requests


def as_json(response: requests.Response) -> Dict[str, Any]:
    return response.json()


def get_code(response: requests.Response) -> Any:
    return as_json(response).get("code")


def get_tip(response: requests.Response) -> Any:
    return as_json(response).get("tip")
