# -*- coding: utf-8 -*-
"""测试数据路径：接口地址与用例列表分文件存放。"""
from common.file_util import data_path

# 耳机
EARPHONE_ENDPOINTS_YAML = data_path("earphone", "endpoints.yaml")
EARPHONE_CASES_YAML = data_path("earphone", "cases.yaml")

# 消息中心
MESSAGE_ENDPOINTS_YAML = data_path("message", "endpoints.yaml")
MESSAGE_CASES_YAML = data_path("message", "cases.yaml")

# 个人中心（mine）
MINE_ENDPOINTS_YAML = data_path("user", "mine_endpoints.yaml")
MINE_CASES_YAML = data_path("user", "mine_cases.yaml")

# 登录 / 注册 / 验证码等（原 register_login）
AUTH_ENDPOINTS_YAML = data_path("login", "auth_endpoints.yaml")
AUTH_CASES_YAML = data_path("login", "auth_cases.yaml")
