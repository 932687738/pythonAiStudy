"""71 Python sys 模块

来源: https://www.runoob.com/python3/python-sys.html
可单独运行: python 71_sys_module.py
"""

from __future__ import annotations

import io
import sys


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 sys 常用变量和方法说明。"""
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


def demo_sys_table() -> None:
    """保留 sys 模块常用功能表。"""
    show_table(
        ("功能", "说明", "示例"),
        [
            ("sys.argv", "命令行参数列表", "sys.argv[0] 是脚本名"),
            ("sys.exit()", "退出程序", "sys.exit(0)"),
            ("sys.path", "模块搜索路径", "sys.path[:3]"),
            ("sys.version", "Python 版本信息", "sys.version"),
            ("sys.platform", "当前平台", "win32/linux/darwin"),
            ("sys.stdin", "标准输入", "sys.stdin.readline()"),
            ("sys.stdout", "标准输出", "sys.stdout.write()"),
            ("sys.stderr", "标准错误", "sys.stderr.write()"),
        ],
    )


def demo_argv_path_version() -> None:
    """执行命令行参数、模块路径和版本信息示例。"""
    print("脚本名称:", sys.argv[0])
    print("参数列表:", sys.argv[1:])
    print("Python 版本:", sys.version.split()[0])
    print("平台:", sys.platform)
    print("模块搜索路径前 3 项:")
    for path in sys.path[:3]:
        print(path)


def demo_exit_without_stopping() -> None:
    """演示 sys.exit 会抛出 SystemExit，本文件捕获它避免脚本提前退出。"""
    try:
        sys.exit(0)
    except SystemExit as exc:
        print(f"捕获 SystemExit: code={exc.code}")


def demo_standard_streams() -> None:
    """演示 stdin、stdout、stderr，使用 StringIO 模拟输入避免阻塞。"""
    original_stdin = sys.stdin
    fake_stdin = io.StringIO("Runoob\n")
    sys.stdin = fake_stdin
    try:
        print("stdin readline:", sys.stdin.readline().strip())
    finally:
        sys.stdin = original_stdin
    sys.stdout.write("stdout write demo\n")
    sys.stderr.write("stderr write demo\n")


def demo_getsizeof_modules() -> None:
    """演示 getsizeof 和 modules 映射。"""
    print("list size:", sys.getsizeof([1, 2, 3]))
    print("'sys' in sys.modules:", "sys" in sys.modules)


def main() -> None:
    """按 sys 页面顺序运行全部示例。"""
    print("Python sys 模块")
    show_section("1. 常用功能")
    demo_sys_table()
    show_section("2. argv、path、version")
    demo_argv_path_version()
    show_section("3. exit")
    demo_exit_without_stopping()
    show_section("4. 标准输入输出")
    demo_standard_streams()
    show_section("5. getsizeof 和 modules")
    demo_getsizeof_modules()


if __name__ == "__main__":
    main()
