# -*- coding: utf-8 -*-
import logging
import time
from typing import Optional

from common.file_util import project_root

log_path = project_root() / "logs"
if not log_path.exists():
    log_path.mkdir(parents=True)

_http_logger: Optional[logging.Logger] = None


def get_http_logger() -> logging.Logger:
    """HTTP 客户端专用 logger，单例初始化，写入 logs/http_YYYY_MM_DD.log。"""
    global _http_logger
    if _http_logger is not None:
        return _http_logger
    name = "api_auto_framework.http"
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if logger.handlers:
        _http_logger = logger
        return logger
    fmt = logging.Formatter("[%(asctime)s] - %(name)s - %(levelname)s: %(message)s")
    fh = logging.FileHandler(
        log_path / ("http_%s.log" % time.strftime("%Y_%m_%d")),
        "a",
        encoding="utf-8",
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.propagate = False
    _http_logger = logger
    return logger


class Log:
    def __init__(self):
        self.logname = log_path / ("%s.log" % time.strftime("%Y_%m_%d"))
        self.logger = logging.getLogger("api_auto_framework")
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            "[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s"
        )

    def __console(self, level, message):
        fh = logging.FileHandler(self.logname, "a", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console("debug", message)

    def info(self, message):
        self.__console("info", message)

    def warning(self, message):
        self.__console("warning", message)

    def error(self, message):
        self.__console("error", message)
