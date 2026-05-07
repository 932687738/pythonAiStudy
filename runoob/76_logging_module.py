"""76 Python logging 模块

来源: https://www.runoob.com/python3/python-logging.html
可单独运行: python 76_logging_module.py
"""

from __future__ import annotations

import logging
import tempfile
from logging.handlers import RotatingFileHandler
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 logging 类、级别和格式字段表。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        """格式化一行表格。"""
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


class ErrorOnlyFilter(logging.Filter):
    """只允许 ERROR 级别日志通过的过滤器。"""

    def filter(self, record: logging.LogRecord) -> bool:
        """返回当前日志是否为 ERROR 级别。"""
        return record.levelno == logging.ERROR


def demo_level_table() -> None:
    """保留日志级别表。"""
    show_table(
        ("级别", "数值", "说明"),
        [
            ("CRITICAL", "50", "严重错误，程序可能无法继续运行"),
            ("ERROR", "40", "错误，但程序仍可运行"),
            ("WARNING", "30", "警告信息，默认级别"),
            ("INFO", "20", "程序运行信息"),
            ("DEBUG", "10", "调试信息"),
            ("NOTSET", "0", "继承父记录器级别"),
        ],
    )


def demo_basic_config_file() -> None:
    """复刻 basicConfig 输出到文件的示例。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "app.log"
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filename=path,
            force=True,
        )
        logger = logging.getLogger("my_app")
        logger.debug("这是一条调试信息")
        logger.info("程序启动")
        print(path.read_text(encoding="utf-8"))


def demo_multiple_handlers() -> None:
    """复刻多个日志记录器和多个处理器示例。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "my_logger.log"
        logger = logging.getLogger("runoob_multi_handler")
        logger.handlers.clear()
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(path, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        logger.debug("这是一条调试信息")
        logger.info("这是一条普通信息")
        print(path.read_text(encoding="utf-8"))
        logger.handlers.clear()


def demo_filter_and_rotation() -> None:
    """演示日志过滤器和 RotatingFileHandler。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "app.log"
        logger = logging.getLogger("runoob_filter")
        logger.handlers.clear()
        logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(path, maxBytes=80, backupCount=3, encoding="utf-8")
        handler.addFilter(ErrorOnlyFilter())
        handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
        logger.addHandler(handler)
        logger.warning("警告不会通过过滤器")
        logger.error("错误会被记录")
        print(path.read_text(encoding="utf-8"))
        logger.handlers.clear()


def demo_core_tables() -> None:
    """保留 logging 核心类、处理器和格式字段表。"""
    show_table(
        ("核心类", "说明"),
        [
            ("logging.Logger", "记录器，用于发出日志消息"),
            ("logging.Handler", "处理器，决定日志输出位置"),
            ("logging.Formatter", "格式化器，控制输出格式"),
            ("logging.Filter", "过滤器，控制哪些日志被记录"),
        ],
    )
    show_table(
        ("Handler 类型", "说明"),
        [
            ("StreamHandler", "输出到流，如控制台"),
            ("FileHandler", "输出到文件"),
            ("RotatingFileHandler", "按文件大小分割日志"),
            ("TimedRotatingFileHandler", "按时间分割日志"),
            ("SMTPHandler", "通过邮件发送日志"),
        ],
    )
    show_table(
        ("字段", "说明"),
        [
            ("%(asctime)s", "日志创建时间"),
            ("%(levelname)s", "日志级别名称"),
            ("%(message)s", "日志消息内容"),
            ("%(name)s", "记录器名称"),
            ("%(filename)s", "生成日志的文件名"),
            ("%(lineno)d", "生成日志的行号"),
            ("%(funcName)s", "生成日志的函数名"),
        ],
    )


def main() -> None:
    """按 logging 页面顺序运行全部示例。"""
    print("Python logging 模块")
    show_section("1. 日志级别")
    demo_level_table()
    show_section("2. basicConfig")
    demo_basic_config_file()
    show_section("3. 多处理器")
    demo_multiple_handlers()
    show_section("4. 过滤器和轮转")
    demo_filter_and_rotation()
    show_section("5. 核心类和格式字段")
    demo_core_tables()


if __name__ == "__main__":
    main()
