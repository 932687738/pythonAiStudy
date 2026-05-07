"""56 Python3 operator

来源: https://www.runoob.com/python3/python-operator.html
可单独运行: python 56_operator_module.py
"""

from __future__ import annotations

import operator


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 operator 函数对照表。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        """格式化表格行。"""
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


def demo_comparison_table() -> None:
    """保留 operator 比较函数与运算符关系。"""
    show_table(
        ("函数", "等价表达式", "示例结果"),
        [
            ("operator.lt(a,b)", "a < b", str(operator.lt(10, 20))),
            ("operator.le(a,b)", "a <= b", str(operator.le(10, 20))),
            ("operator.eq(a,b)", "a == b", str(operator.eq(10, 10))),
            ("operator.ne(a,b)", "a != b", str(operator.ne(10, 20))),
            ("operator.ge(a,b)", "a >= b", str(operator.ge(20, 10))),
            ("operator.gt(a,b)", "a > b", str(operator.gt(20, 10))),
        ],
    )


def demo_number_comparison() -> None:
    """执行页面中的数字比较示例。"""
    x = 10
    y = 20
    print("x:", x, ", y:", y)
    print("operator.lt(x,y): ", operator.lt(x, y))
    print("operator.gt(y,x): ", operator.gt(y, x))
    print("operator.eq(x,x): ", operator.eq(x, x))


def demo_list_comparison() -> None:
    """执行页面中的列表比较示例。"""
    a = [1, 2]
    b = [2, 3]
    c = [2, 3]
    print("operator.eq(a,b): ", operator.eq(a, b))
    print("operator.eq(c,b): ", operator.eq(c, b))


def demo_math_operators() -> None:
    """保留 operator 数学运算函数并执行 add、sub、mul、truediv 等示例。"""
    a = 4
    b = 3
    show_table(
        ("函数", "等价表达式", "结果"),
        [
            ("add(a,b)", "a + b", str(operator.add(a, b))),
            ("sub(a,b)", "a - b", str(operator.sub(a, b))),
            ("mul(a,b)", "a * b", str(operator.mul(a, b))),
            ("truediv(a,b)", "a / b", str(operator.truediv(a, b))),
            ("floordiv(a,b)", "a // b", str(operator.floordiv(a, b))),
            ("mod(a,b)", "a % b", str(operator.mod(a, b))),
            ("pow(a,b)", "a ** b", str(operator.pow(a, b))),
            ("neg(a)", "-a", str(operator.neg(a))),
        ],
    )


def demo_sequence_operators() -> None:
    """演示 operator 中的序列操作：contains、getitem、setitem、delitem。"""
    values = [1, 2, 3]
    print(operator.contains(values, 2))
    print(operator.getitem(values, 1))
    operator.setitem(values, 1, 20)
    print(values)
    operator.delitem(values, 0)
    print(values)


def demo_itemgetter_attrgetter_methodcaller() -> None:
    """补充 operator 常用工具函数：itemgetter、attrgetter 和 methodcaller。"""

    class Student:
        """用于 attrgetter 示例的简单类。"""

        def __init__(self, name: str, score: int) -> None:
            """初始化姓名和分数。"""
            self.name = name
            self.score = score

    students = [Student("Alice", 90), Student("Bob", 80)]
    print([student.name for student in sorted(students, key=operator.attrgetter("score"))])
    records = [("Alice", 90), ("Bob", 80)]
    print(sorted(records, key=operator.itemgetter(1)))
    print(operator.methodcaller("upper")("runoob"))


def main() -> None:
    """按 operator 页面顺序运行全部示例。"""
    print("Python3 operator")
    show_section("1. 比较函数表")
    demo_comparison_table()
    show_section("2. 数字比较")
    demo_number_comparison()
    show_section("3. 列表比较")
    demo_list_comparison()
    show_section("4. 数学运算函数")
    demo_math_operators()
    show_section("5. 序列操作")
    demo_sequence_operators()
    show_section("6. 常用工具函数")
    demo_itemgetter_attrgetter_methodcaller()


if __name__ == "__main__":
    main()
