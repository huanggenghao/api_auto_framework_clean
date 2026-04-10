# -*- coding: utf-8 -*-
"""统一执行入口：pytest + Allure 结果 +（可选）邮件。"""
import os
import shutil
import subprocess
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.chdir(ROOT)


def _allure_results_dir():
    return ROOT / "report" / "allure-results"


def _allure_report_dir():
    return ROOT / "report" / "allure-report"


def run_tests():
    results = _allure_results_dir()
    results.mkdir(parents=True, exist_ok=True)
    junit_path = ROOT / "report" / "junit.xml"
    junit_path.parent.mkdir(parents=True, exist_ok=True)

    args = [
        str(ROOT),
        "-v",
        "--tb=short",
        f"--alluredir={results}",
        f"--junitxml={junit_path}",
    ]
    print("pytest args:", args)
    return pytest.main(args)


def generate_allure_html():
    out = _allure_report_dir()
    cmd = [
        "allure",
        "generate",
        str(_allure_results_dir()),
        "-o",
        str(out),
        "--clean",
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Allure HTML:", out)
        return out
    except FileNotFoundError:
        print("未找到 allure 命令。可执行: allure serve report/allure-results")
        return None
    except subprocess.CalledProcessError as e:
        print("allure generate 失败:", e.stderr or e.stdout)
        return None


def send_email(sender, psw, receiver, smtpserver, attachment_path, port, subject=None):
    import smtplib

    if not attachment_path or not Path(attachment_path).is_file():
        print("无有效附件，跳过发信:", attachment_path)
        return

    msg = MIMEMultipart()
    msg["Subject"] = subject or "接口自动化测试 (api_auto_framework)"
    msg["from"] = sender
    msg["to"] = receiver

    body = MIMEText(
        "pytest + Allure 执行完成。\n附件为 JUnit XML 或 Allure 报告压缩包。\n",
        _subtype="plain",
        _charset="utf-8",
    )
    msg.attach(body)

    filename = os.path.basename(attachment_path)
    with open(attachment_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
    msg.attach(part)

    port_n = int(port) if str(port).strip() else 465
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port_n)
    except Exception:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port_n)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver.split(","), msg.as_string())
    smtp.quit()
    print("测试报告邮件已发送。")


def main():
    exit_code = run_tests()
    allure_html = generate_allure_html()
    zip_path = None
    if allure_html and allure_html.is_dir():
        zip_base = ROOT / "report" / "allure-report"
        zip_path = shutil.make_archive(str(zip_base), "zip", str(allure_html))

    from config import get_settings

    s = get_settings()
    em = s.get("email", {})
    sender = em.get("sender") or os.environ.get("SMTP_SENDER", "")
    psw = em.get("psw") or os.environ.get("SMTP_PSW", "")
    receiver = em.get("receiver") or os.environ.get("SMTP_RECEIVER", "")
    smtp_server = em.get("smtp_server") or os.environ.get("SMTP_SERVER", "")
    port = em.get("port") or os.environ.get("SMTP_PORT", 465)

    junit = ROOT / "report" / "junit.xml"
    attachment = zip_path if zip_path and Path(zip_path).is_file() else str(junit)
    if sender and psw and receiver and smtp_server and Path(attachment).is_file():
        send_email(sender, psw, receiver, smtp_server, attachment, port)
    elif not (sender and receiver):
        print("未配置完整邮箱信息，跳过发信（可在 config/test.yaml 或环境变量中配置）。")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
