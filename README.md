# API 自动化测试框架（api_auto_framework）

## 简介

本仓库是一套 **HTTP 接口自动化测试工程**，采用 **pytest** 组织与执行用例，**requests** 发起请求，**Allure** 输出可视化报告；接口路径与请求体等测试数据放在 **YAML** 中维护，代码按 **testcase → service → api → 请求工具** 分层，便于团队协作与扩展。

典型一次请求在框架内的流向为：用例层读取或触发 YAML 数据 → 调用 service → service 调用 api → api 通过 `HttpClient` 发请求 → 解析响应 → 使用 `assert_util` 断言 → Allure 记录步骤与结果。

---

## 项目结构

```
api_auto_framework/
├── testcase/          # pytest 用例（test_*.py）
├── service/           # 业务服务层，对 api 的封装与注册等场景入口
├── api/               # 接口封装层（URL、body、响应解析）
├── core/              # 请求客户端、断言、Token 缓存等核心能力
├── common/            # YAML 读写、数据路径、日志、Allure 附件工具等
├── data/              # 用例级 YAML 数据（按业务分子目录）
├── config/            # 运行环境与鉴权等配置（YAML）
├── report/            # 运行产物：allure-results、allure-report、junit.xml 等
├── conftest.py        # pytest 全局 fixture
├── pytest.ini         # pytest 默认参数
├── run.py             # 统一执行入口（pytest + Allure 报告 + 可选邮件）
├── requirements.txt   # Python 依赖
└── README.md
```

| 目录 / 文件 | 职责简述 |
|---------------|----------|
| `testcase/` | 只写场景与断言，依赖 conftest 注入的 service、数据 fixture |
| `service/` | `LoginService`、`UserService`、`EarphoneService`、`MessageService`（薄封装 api） |
| `api/` | 与各后端接口一一对应的调用与结果提取逻辑 |
| `core/` | `request_util.HttpClient`、`assert_util`、`cache_util`（如登录拿 Token）等 |
| `common/` | `yaml_util`、`data_files`、`case_data`（加载 endpoints/cases）、`logger`、`allure_util` |
| `data/` | 按业务分子目录；**每个业务两套文件**：`endpoints.yaml`（仅接口地址）、`cases.yaml`（仅 `cases:` 列表，一条用例一个字典） |
| `config/` | `config.yaml` 指定当前环境，再加载 `test.yaml` / `dev.yaml` / `prod.yaml` |

---

## 运行环境

| 项 | 说明 |
|----|------|
| Python | 建议 **3.9+**（与本地 IDE / 虚拟环境保持一致即可） |
| 操作系统 | Windows / macOS / Linux 均可 |
| 依赖安装 | 进入项目根目录执行：`pip install -r requirements.txt` |
| Allure 命令行 | **可选**。需要本地生成 HTML 报告时，可安装 [Allure 2](https://github.com/allure-framework/allure2/releases) 并确保 `allure` 在 PATH 中；仅用 `pytest` + `allure-results` 也可配合 CI 或 `allure serve` |

主要第三方库见 `requirements.txt`（如 `pytest`、`allure-pytest`、`requests`、`PyYAML`、`urllib3`）。

---

## 环境说明

1. **当前环境切换**  
   编辑 `config/config.yaml` 中的 `active_env`，取值与文件名对应，例如 `test` 会合并加载 `config/test.yaml`。

2. **环境文件内容（示例含义）**  
   - `http`：如 `timeout` 请求超时（秒）。  
   - `auth`：用于 `core.cache_util` 拉取 Token 的登录信息，例如 `login_url`、`login_account`、`login_password`、`merchant_id`、`phone_code` 等（具体键名以各 `config/*.yaml` 为准）。  
   - 部分项目还会在环境 yaml 中配置邮件 `email`（供 `run.py` 发报告，可选）。

3. **安全建议**  
   勿将含真实密码的 `config/*.yaml` 提交到公开仓库；生产/预发凭据建议使用环境变量或本地未入库的配置覆盖。

---

## 模块设计

### 分层与职责

- **testcase**：描述「测什么」；通过 fixture 拿到 YAML 数据（带 Allure 步骤）与 `*_service`；使用 `allure.feature` / `title` / `step` 与 `assert_util` 断言。  
- **service**：描述「业务上怎么调」；薄封装 `api`。  
- **api**：描述「单个接口怎么调」；**URL** 从对应业务的 `endpoints.yaml` 读取，请求体由用例传入；调用 `HttpClient.post/get`。  
- **core.request_util**：`HttpClient` 基于 `requests.Session` 封装，统一超时（来自 `get_settings()`）。  
- **core.assert_util**：如 `assert_equal`，集中断言便于扩展与报告信息统一。  
- **core.cache_util**：会话级 Token 缓存，供需要 `Authorization` 的 api 使用。  
- **common**：与业务无关的通用工具（读 YAML、路径、日志、附件等）。

### 数据流（简图）

```
YAML(endpoints.yaml + cases.yaml) ──► api 读 endpoints / 用例参数化读 cases
                              │
testcase ──► service ──► api ──► HttpClient ──► 服务端
                              │
                         assert_util ◄── 业务返回值 / 解析结果
                              │
                         Allure 步骤与附件
```

---

## 其他文件说明

| 文件 / 目录 | 说明 |
|-------------|------|
| `run.py` | 调用 `pytest.main`，指定 `--alluredir`、`--junitxml`；成功后尝试 `allure generate`；若 `config` 中邮件信息完整可发送报告附件 |
| `pytest.ini` | `testpaths=testcase`，默认 `-v --tb=short`，以及 `--alluredir=report/allure-results` |
| `conftest.py` | `api_session`、`http_client`；各业务 YAML 的 `load_yaml` fixture（带 Allure「读取 xxx.yaml」步骤）；各 `*Service` 的 fixture |
| `common/data_files.py` | 声明各业务 `*_ENDPOINTS_YAML`、`*_CASES_YAML` 绝对路径 |
| `common/case_data.py` | `load_endpoints` / `load_cases_list` / `build_parametrize_cases`（解析单字典用例） |
| `report/` | 运行后生成；`allure-results` 为原始结果，`allure-report` 为 `allure generate` 后的 HTML，`junit.xml` 由 `run.py` 写入 |
| `common/json_util.py` | 若仍有 JSON 读写需求可复用；当前主数据已为 YAML |

---

## 如何编写测试用例

1. **准备数据**  
   在 `data/<业务>/` 下维护 **`endpoints.yaml`**（仅 URL 键值）与 **`cases.yaml`**（顶层 `cases:`，列表中**每一项是一条完整用例，一个字典**）。新目录需在 `common/data_files.py` 增加路径常量。

2. **有全新接口时**  
   - 在 `endpoints.yaml` 增加 URL 键；在 `cases.yaml` 的 `cases` 里追加字典：`caseNo`、`caseName`、`endpoint`（引用 endpoints 中的键）、`request`、`expect`，可选 `repeat_count`。  
   - 在 `api/` 中从对应 `endpoints.yaml` 取 URL，使用 `HttpClient` 发请求。  
   - 在 `service/` 增加薄封装。  
   - 用例侧可用 `common.case_data.build_parametrize_cases` 做 `pytest_generate_tests` 参数化。

3. **编写 `testcase/test_xxx.py`**  
   - 使用 fixture：`register_login_data`、`earphone_data` 等，结构为 `{"endpoints": {...}, "cases": [...]}`。  
   - 注入 `login_service`、`user_service` 等；断言可用 `core.expect_util.apply_response_expectations`。

4. **单条用例字典字段说明**  
   - `endpoint`：字符串，必须在同业务的 `endpoints.yaml` 中存在。  
   - `request`：请求体（原 `reqParam` 合并进此字段，避免嵌套列表套字典的反模式）。  
   - `expect`：`http_status`、`tip`、`code`、`json_equals`、`list_switch_status` 等与 `expect_util` 一致。

---

## 执行用例

**在项目根目录 `api_auto_framework` 下执行。**

```bash
# 安装依赖
pip install -r requirements.txt

# 全量执行（写入 report/allure-results，见 pytest.ini）
pytest

# 指定文件 / 关键字
pytest testcase/test_earphone.py
pytest -k h5
```

**统一入口（含 JUnit、尝试生成 Allure HTML、可选邮件）：**

```bash
python run.py
```

**查看 Allure 报告：**

```bash
# 本地临时服务打开结果目录
allure serve report/allure-results

# 或生成静态 HTML
allure generate report/allure-results -o report/allure-report --clean
# 浏览器打开 report/allure-report/index.html
```

若未安装 Allure 命令行，`run.py` 仍会完成 pytest；可根据控制台提示仅使用 `allure-results` 目录在 CI 中上传或由其他工具展示。
