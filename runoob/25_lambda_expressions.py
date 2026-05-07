"""25 Python3 lambda

来源: https://www.runoob.com/python3/python-lambda.html
可单独运行: python 25_lambda_expressions.py
"""

from __future__ import annotations

from functools import reduce


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的 lambda 语法说明。"""
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


def demo_lambda_syntax() -> None:
    """保留 lambda 基本语法和特点。"""
    show_table(
        ("组成部分", "说明"),
        [
            ("lambda", "定义匿名函数的关键字"),
            ("arguments", "参数列表，可有零个或多个参数"),
            ("expression", "只能有一个表达式，表达式结果就是返回值"),
        ],
    )


def demo_no_argument_lambda() -> None:
    """执行页面中的无参数 lambda 示例。"""
    func = lambda: "Hello, world!"
    print(func())


def demo_single_argument_lambda() -> None:
    """执行单参数 lambda：参数加 10。"""
    x = lambda a: a + 10
    print(x(5))


def demo_multiple_argument_lambda() -> None:
    """执行多参数 lambda：两个参数相乘、三个参数相加。"""
    multiply = lambda a, b: a * b
    add_three = lambda a, b, c: a + b + c
    print(multiply(5, 6))
    print(add_three(5, 6, 2))


def demo_map_lambda() -> None:
    """执行 lambda 与 map() 结合，计算平方列表。"""
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)


def demo_filter_lambda() -> None:
    """执行 lambda 与 filter() 结合，筛选偶数。"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)


def demo_reduce_lambda() -> None:
    """执行 lambda 与 reduce() 结合，计算累积乘积。"""
    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)


def demo_lambda_limit_note() -> None:
    """说明 lambda 适合简单表达式，复杂逻辑应使用 def。"""
    absolute = lambda x: x if x >= 0 else -x
    print(absolute(-10))
    print("lambda 只能写一个表达式，不能包含多条语句。")


def main() -> None:
    """按 lambda 页面顺序运行全部示例。"""
    print("Python3 lambda")

    show_section("1. lambda 语法")
    demo_lambda_syntax()

    show_section("2. 无参数 lambda")
    demo_no_argument_lambda()

    show_section("3. 单参数 lambda")
    demo_single_argument_lambda()

    show_section("4. 多参数 lambda")
    demo_multiple_argument_lambda()

    show_section("5. map() 与 lambda")
    demo_map_lambda()

    show_section("6. filter() 与 lambda")
    demo_filter_lambda()

    show_section("7. reduce() 与 lambda")
    demo_reduce_lambda()

    show_section("8. lambda 限制")
    demo_lambda_limit_note()


if __name__ == "__main__":
    main()
