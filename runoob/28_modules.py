"""28 Python3 模块

来源: https://www.runoob.com/python3/python3-module.html
可单独运行: python 28_modules.py
"""

from __future__ import annotations

import math
import sys
from types import ModuleType


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的模块概念说明。"""
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


def demo_module_intro() -> None:
    """说明模块是包含 Python 定义和语句的文件。"""
    show_table(
        ("概念", "说明"),
        [
            ("模块", "一个 .py 文件就是一个模块"),
            ("import", "导入整个模块"),
            ("from...import", "从模块导入指定对象"),
            ("as", "给模块或对象起别名"),
            ("sys.path", "解释器查找模块的路径列表"),
        ],
    )


def fib(n: int) -> None:
    """页面 fibo.py 中的 fib 函数：打印小于 n 的斐波那契数。"""
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()


def fib2(n: int) -> list[int]:
    """页面 fibo.py 中的 fib2 函数：返回小于 n 的斐波那契列表。"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def demo_module_function() -> None:
    """在单文件中模拟 fibo 模块的导入和调用效果。"""
    fib(1000)
    print(fib2(100))
    print(f"fib.__name__ -> {fib.__name__}")


def demo_sys_module() -> None:
    """复刻 using_sys.py：输出命令行参数和 Python 查找路径。"""
    print("命令行参数如下:")
    for item in sys.argv:
        print(item)
    print("Python 路径前 5 项为:")
    for path in sys.path[:5]:
        print(path)


def demo_import_forms() -> None:
    """演示 import、from import、别名导入和导入多个名称。"""
    import math as math_module
    from math import pi, sqrt

    print(math_module.sin(math_module.pi / 2))
    print(pi)
    print(sqrt(16))


def demo_name_main() -> None:
    """说明 __name__ 属性在直接运行和导入时的不同含义。"""
    print(f"当前模块 __name__: {__name__}")
    if __name__ == "__main__":
        print("程序自身在运行")
    else:
        print("我来自另一模块")


def demo_dir() -> None:
    """演示 dir() 可以列出模块内定义的名称。"""
    math_names = dir(math)
    print(math_names[:10])
    current_names = [name for name in dir() if not name.startswith("__")]
    print(current_names[:10])


def demo_packages_note() -> None:
    """保留包的概念：目录加 __init__.py 可组织多个模块。"""
    fake_package = ModuleType("sound.effects.echo")
    fake_package.description = "包可以按目录层级组织模块"
    print(fake_package.__name__)
    print(fake_package.description)


def main() -> None:
    """按模块页面顺序运行全部示例。"""
    print("Python3 模块")

    show_section("1. 模块概念")
    demo_module_intro()

    show_section("2. 模拟 fibo 模块")
    demo_module_function()

    show_section("3. sys 模块")
    demo_sys_module()

    show_section("4. import 语句形式")
    demo_import_forms()

    show_section("5. __name__ 属性")
    demo_name_main()

    show_section("6. dir() 函数")
    demo_dir()

    show_section("7. 包")
    demo_packages_note()


if __name__ == "__main__":
    main()
