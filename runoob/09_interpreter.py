"""09 Python3 解释器

来源: https://www.runoob.com/python3/python3-interpreter.html
可单独运行: python 09_interpreter.py
"""

from __future__ import annotations

import platform
import sys


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_command(command: str, description: str) -> None:
    """保留页面中的命令行示例，并说明命令用途。"""
    print(f"$ {command}")
    print(f"说明: {description}")


def demo_environment_path() -> None:
    """说明安装 Python3 后如何通过环境变量找到解释器。"""
    print("Linux/Unix 常见安装目录示例: /usr/local/python3")
    show_command("PATH=$PATH:/usr/local/python3/bin/python3", "将 Python3 路径加入 PATH")
    show_command("python3 --version", "查看 Python3 版本")
    print("Windows 示例: set path=%path%;C:\\python34")
    print(f"当前脚本使用的解释器: {sys.executable}")
    print(f"当前 Python 版本: {platform.python_version()}")


def demo_interactive_programming() -> None:
    """复刻交互式编程示例：在 >>> 提示符中执行 print 和 if 语句。"""
    print("交互式编程通常先在终端输入 python 或 python3。")
    show_command("python3", "启动 Python3 交互式解释器")

    print("页面中的交互式 print 示例对应逻辑:")
    print("Hello, Python!")

    print("页面中的多行 if 示例对应逻辑:")
    flag = True
    if flag:
        print("flag 条件为 True!")


def demo_script_programming() -> None:
    """复刻脚本式编程示例：把代码保存为 hello.py 再运行。"""
    hello_source = 'print("Hello, Python!")'
    print("hello.py 文件内容示例:")
    print(hello_source)

    print("本文件中直接执行同样逻辑:")
    print("Hello, Python!")

    show_command("python3 hello.py", "运行 Python 脚本文件")
    print("Linux/Unix 可在脚本顶部添加 shebang:")
    print("#! /usr/bin/env python3")
    show_command("chmod +x hello.py", "给脚本添加执行权限")
    show_command("./hello.py", "直接运行脚本")


def demo_interpreter_types_note() -> None:
    """保留页面笔记中提到的解释器类型，帮助理解 Python 不只有一种实现。"""
    interpreter_types = [
        ("CPython", "官方标准实现，使用 C 语言开发，生态最广泛"),
        ("IPython", "在 CPython 基础上增强交互体验"),
        ("Jython", "面向 Java 平台，可把 Python 代码编译为 Java 字节码"),
        ("PyPy", "强调执行速度的 Python 替代实现"),
    ]
    for name, description in interpreter_types:
        print(f"{name}: {description}")


def main() -> None:
    """按解释器页面顺序运行全部示例。"""
    print("Python3 解释器")

    show_section("1. 环境变量与版本")
    demo_environment_path()

    show_section("2. 交互式编程")
    demo_interactive_programming()

    show_section("3. 脚本式编程")
    demo_script_programming()

    show_section("4. 解释器类型补充")
    demo_interpreter_types_note()


if __name__ == "__main__":
    main()
