"""23 Python3 with

来源: https://www.runoob.com/python3/python3-with-keyword.html
可单独运行: python 23_with_statement.py
"""

from __future__ import annotations

import decimal
import sqlite3
import tempfile
import threading
import time
from contextlib import contextmanager
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的总结表。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


def demo_try_finally_file() -> None:
    """复刻传统资源管理示例：try/finally 手动关闭文件。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "example.txt"
        path.write_text("hello with", encoding="utf-8")
        file = open(path, "r", encoding="utf-8")
        try:
            content = file.read()
            print(content)
        finally:
            file.close()
        print(f"file.closed -> {file.closed}")


def demo_with_file() -> None:
    """复刻 with 打开文件示例，文件离开代码块后自动关闭。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "example.txt"
        path.write_text("hello with", encoding="utf-8")
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
        print(f"file.closed -> {file.closed}")


def demo_multiple_files() -> None:
    """复刻同时打开多个文件示例，把输入内容转大写写入输出文件。"""
    with tempfile.TemporaryDirectory() as directory:
        input_path = Path(directory) / "input.txt"
        output_path = Path(directory) / "output.txt"
        input_path.write_text("runoob", encoding="utf-8")
        with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
            content = infile.read()
            outfile.write(content.upper())
        print(output_path.read_text(encoding="utf-8"))


def demo_sqlite_context() -> None:
    """复刻数据库连接场景，使用 sqlite3.connect 上下文管理事务。"""
    with sqlite3.connect(":memory:") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (name TEXT)")
        cursor.execute("INSERT INTO users VALUES (?)", ("Runoob",))
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print(results)


def demo_thread_lock() -> None:
    """复刻线程锁场景，with lock 自动进入和释放临界区。"""
    lock = threading.Lock()
    with lock:
        print("这段代码是线程安全的")


def demo_decimal_context() -> None:
    """复刻临时修改系统状态示例，localcontext 结束后精度恢复。"""
    original_precision = decimal.getcontext().prec
    with decimal.localcontext() as ctx:
        ctx.prec = 42
        result = decimal.Decimal(1) / decimal.Decimal(7)
        print(result)
    print(f"精度恢复: {decimal.getcontext().prec == original_precision}")


class Timer:
    """页面中的类实现上下文管理器示例。"""

    def __enter__(self) -> Timer:
        """进入上下文时记录开始时间，并把自身赋给 as 后变量。"""
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """退出上下文时记录结束时间并输出耗时，不抑制异常。"""
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.4f} 秒")
        return False


def demo_timer_context() -> None:
    """执行页面中的 Timer 自定义上下文管理器。"""
    with Timer():
        sum(range(10000))


@contextmanager
def tag(name: str):
    """页面中的 contextlib.contextmanager 示例，进入前后输出标签。"""
    print(f"<{name}>")
    yield
    print(f"</{name}>")


def demo_contextlib_manager() -> None:
    """执行 contextlib 创建上下文管理器的 tag 示例。"""
    with tag("h1"):
        print("这是一个标题")


class SwallowValueError:
    """演示 __exit__ 返回 True 时可以抑制指定异常。"""

    def __enter__(self) -> SwallowValueError:
        """进入上下文并返回自身。"""
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """只抑制 ValueError，其他异常继续传播。"""
        print(f"exit: {exc_type.__name__ if exc_type else None}")
        return exc_type is ValueError


def demo_exception_handling() -> None:
    """演示页面提到的 __exit__ 异常处理机制。"""
    with SwallowValueError():
        raise ValueError("handled")
    print("ValueError 已被上下文管理器处理")


def demo_summary_table() -> None:
    """保留页面总结要点表。"""
    show_table(
        ("关键点", "说明"),
        [
            ("自动资源管理", "with 语句确保资源被正确释放"),
            ("上下文协议", "需要实现 __enter__ 和 __exit__ 方法"),
            ("异常安全", "即使代码块出现异常，资源也会释放"),
            ("常见应用", "文件操作、数据库连接、线程锁等"),
            ("自定义实现", "可以通过类或 contextlib 创建上下文管理器"),
        ],
    )


def main() -> None:
    """按 with 页面顺序运行全部示例。"""
    print("Python3 with")

    show_section("1. try/finally 传统资源管理")
    demo_try_finally_file()

    show_section("2. with 文件操作")
    demo_with_file()

    show_section("3. 同时管理多个文件")
    demo_multiple_files()

    show_section("4. 数据库连接")
    demo_sqlite_context()

    show_section("5. 线程锁")
    demo_thread_lock()

    show_section("6. 临时修改 decimal 精度")
    demo_decimal_context()

    show_section("7. 类实现上下文管理器")
    demo_timer_context()

    show_section("8. contextlib 实现上下文管理器")
    demo_contextlib_manager()

    show_section("9. __exit__ 异常处理")
    demo_exception_handling()

    show_section("10. 总结要点")
    demo_summary_table()


if __name__ == "__main__":
    main()
