"""11 Python3 运算符

来源: https://www.runoob.com/python3/python3-basic-operators.html
可单独运行: python 11_operators.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的运算符表格。"""
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


def demo_operator_intro() -> None:
    """说明操作数和运算符的关系，并列出页面覆盖的运算符类别。"""
    a = 4
    b = 5
    print(f"{a} + {b} = {a + b}")
    print("4 和 5 是操作数，+ 是运算符。")
    categories = [
        "算术运算符",
        "比较运算符",
        "赋值运算符",
        "位运算符",
        "逻辑运算符",
        "成员运算符",
        "身份运算符",
        "运算符优先级",
    ]
    for category in categories:
        print(f"- {category}")


def demo_arithmetic_operators() -> None:
    """保留算术运算符表，并执行页面中的 a=21、b=10 示例。"""
    show_table(
        ("运算符", "描述", "示例"),
        [
            ("+", "加", "a + b"),
            ("-", "减", "a - b"),
            ("*", "乘", "a * b"),
            ("/", "除", "a / b"),
            ("%", "取模", "a % b"),
            ("**", "幂", "a ** b"),
            ("//", "取整除", "a // b"),
        ],
    )

    a = 21
    b = 10
    c = a + b
    print("1 - c 的值为：", c)
    c = a - b
    print("2 - c 的值为：", c)
    c = a * b
    print("3 - c 的值为：", c)
    c = a / b
    print("4 - c 的值为：", c)
    c = a % b
    print("5 - c 的值为：", c)

    a = 2
    b = 3
    c = a**b
    print("6 - c 的值为：", c)

    a = 10
    b = 5
    c = a // b
    print("7 - c 的值为：", c)
    print(f"9 // 2 -> {9 // 2}")
    print(f"-9 // 2 -> {-9 // 2}")


def demo_comparison_operators() -> None:
    """保留比较运算符表，并执行页面中的 if/else 比较示例。"""
    show_table(
        ("运算符", "描述", "示例"),
        [
            ("==", "等于", "a == b"),
            ("!=", "不等于", "a != b"),
            (">", "大于", "a > b"),
            ("<", "小于", "a < b"),
            (">=", "大于等于", "a >= b"),
            ("<=", "小于等于", "a <= b"),
        ],
    )

    a = 21
    b = 10
    if a == b:
        print("1 - a 等于 b")
    else:
        print("1 - a 不等于 b")
    if a != b:
        print("2 - a 不等于 b")
    else:
        print("2 - a 等于 b")
    if a < b:
        print("3 - a 小于 b")
    else:
        print("3 - a 大于等于 b")
    if a > b:
        print("4 - a 大于 b")
    else:
        print("4 - a 小于等于 b")

    a = 5
    b = 20
    if a <= b:
        print("5 - a 小于等于 b")
    else:
        print("5 - a 大于 b")
    if b >= a:
        print("6 - b 大于等于 a")
    else:
        print("6 - b 小于 a")


def demo_assignment_operators() -> None:
    """保留赋值运算符表，并执行页面中的复合赋值示例。"""
    show_table(
        ("运算符", "描述", "等效写法"),
        [
            ("=", "简单赋值", "c = a + b"),
            ("+=", "加法赋值", "c = c + a"),
            ("-=", "减法赋值", "c = c - a"),
            ("*=", "乘法赋值", "c = c * a"),
            ("/=", "除法赋值", "c = c / a"),
            ("%=", "取模赋值", "c = c % a"),
            ("**=", "幂赋值", "c = c ** a"),
            ("//=", "取整除赋值", "c = c // a"),
            (":=", "海象运算符", "表达式内赋值并返回值"),
        ],
    )

    a = 21
    b = 10
    c = a + b
    print("1 - c 的值为：", c)
    c += a
    print("2 - c 的值为：", c)
    c *= a
    print("3 - c 的值为：", c)
    c /= a
    print("4 - c 的值为：", c)
    c = 2
    c %= a
    print("5 - c 的值为：", c)
    c **= a
    print("6 - c 的值为：", c)
    c //= a
    print("7 - c 的值为：", c)

    if (n := 10) > 5:
        print("海象运算符示例：", n)


def demo_bitwise_operators() -> None:
    """保留位运算符表，并执行页面中的 a=60、b=13 示例。"""
    a = 60
    b = 13
    print(f"a = {a:08b}")
    print(f"b = {b:08b}")
    show_table(
        ("运算符", "描述", "结果"),
        [
            ("&", "按位与", str(a & b)),
            ("|", "按位或", str(a | b)),
            ("^", "按位异或", str(a ^ b)),
            ("~", "按位取反", str(~a)),
            ("<<", "左移", str(a << 2)),
            (">>", "右移", str(a >> 2)),
        ],
    )
    c = a & b
    print("1 - c 的值为：", c)
    c = a | b
    print("2 - c 的值为：", c)
    c = a ^ b
    print("3 - c 的值为：", c)
    c = ~a
    print("4 - c 的值为：", c)
    c = a << 2
    print("5 - c 的值为：", c)
    c = a >> 2
    print("6 - c 的值为：", c)


def demo_logical_operators() -> None:
    """保留逻辑运算符表，并执行页面中的 and/or/not 示例。"""
    show_table(
        ("运算符", "逻辑表达式", "描述"),
        [
            ("and", "x and y", "x 为 False 返回 x，否则返回 y"),
            ("or", "x or y", "x 为 True 返回 x，否则返回 y"),
            ("not", "not x", "x 为 True 返回 False"),
        ],
    )

    a = 10
    b = 20
    if a and b:
        print("1 - 变量 a 和 b 都为 true")
    else:
        print("1 - 变量 a 和 b 有一个不为 true")
    if a or b:
        print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("2 - 变量 a 和 b 都不为 true")

    a = 0
    if a and b:
        print("3 - 变量 a 和 b 都为 true")
    else:
        print("3 - 变量 a 和 b 有一个不为 true")
    if a or b:
        print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("4 - 变量 a 和 b 都不为 true")
    if not (a and b):
        print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
    else:
        print("5 - 变量 a 和 b 都为 true")


def demo_membership_operators() -> None:
    """保留成员运算符表，并执行页面中的列表成员判断示例。"""
    show_table(
        ("运算符", "描述", "示例"),
        [
            ("in", "在序列中找到值返回 True", "x in y"),
            ("not in", "在序列中没有找到值返回 True", "x not in y"),
        ],
    )
    a = 10
    b = 20
    values = [1, 2, 3, 4, 5]
    if a in values:
        print("1 - 变量 a 在给定的列表中 values 中")
    else:
        print("1 - 变量 a 不在给定的列表中 values 中")
    if b not in values:
        print("2 - 变量 b 不在给定的列表中 values 中")
    else:
        print("2 - 变量 b 在给定的列表中 values 中")
    a = 2
    if a in values:
        print("3 - 变量 a 在给定的列表中 values 中")
    else:
        print("3 - 变量 a 不在给定的列表中 values 中")


def demo_identity_operators() -> None:
    """保留身份运算符表，并演示 is 与 == 的区别。"""
    show_table(
        ("运算符", "描述", "等效理解"),
        [
            ("is", "判断两个标识符是否引用同一个对象", "id(x) == id(y)"),
            ("is not", "判断两个标识符是否引用不同对象", "id(x) != id(y)"),
        ],
    )
    a = 20
    b = 20
    if a is b:
        print("1 - a 和 b 有相同的标识")
    else:
        print("1 - a 和 b 没有相同的标识")
    if id(a) == id(b):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    b = 30
    if a is b:
        print("3 - a 和 b 有相同的标识")
    else:
        print("3 - a 和 b 没有相同的标识")
    if a is not b:
        print("4 - a 和 b 没有相同的标识")
    else:
        print("4 - a 和 b 有相同的标识")

    list_a = [1, 2, 3]
    list_b = list_a
    list_c = list_a[:]
    print(f"list_b is list_a -> {list_b is list_a}")
    print(f"list_b == list_a -> {list_b == list_a}")
    print(f"list_c is list_a -> {list_c is list_a}")
    print(f"list_c == list_a -> {list_c == list_a}")


def demo_operator_precedence() -> None:
    """保留运算符优先级表，并执行页面中的括号优先级和 and/or 示例。"""
    show_table(
        ("优先级片段", "说明"),
        [
            ("()", "圆括号表达式"),
            ("**", "乘方"),
            ("+x, -x, ~x", "正负号与按位非"),
            ("*, /, //, %", "乘除、整除、取余"),
            ("+, -", "加减"),
            ("<<, >>", "移位"),
            ("&, ^, |", "位运算"),
            ("in, is, <, ==", "比较、成员、身份检测"),
            ("not, and, or", "逻辑运算"),
            ("if...else", "条件表达式"),
            ("lambda", "lambda 表达式"),
            (":=", "赋值表达式"),
        ],
    )

    a = 20
    b = 10
    c = 15
    d = 5
    e = (a + b) * c / d
    print("(a + b) * c / d 运算结果为：", e)
    e = ((a + b) * c) / d
    print("((a + b) * c) / d 运算结果为：", e)
    e = (a + b) * (c / d)
    print("(a + b) * (c / d) 运算结果为：", e)
    e = a + (b * c) / d
    print("a + (b * c) / d 运算结果为：", e)

    x = True
    y = False
    z = False
    print("情况1：默认优先级（先算 and）")
    if x or y and z:
        print("yes")
    else:
        print("no")
    print("情况2：强制改变优先级（先算 or）")
    if (x or y) and z:
        print("yes")
    else:
        print("no")


def main() -> None:
    """按运算符页面顺序运行全部示例。"""
    print("Python3 运算符")

    show_section("1. 什么是运算符")
    demo_operator_intro()

    show_section("2. 算术运算符")
    demo_arithmetic_operators()

    show_section("3. 比较运算符")
    demo_comparison_operators()

    show_section("4. 赋值运算符")
    demo_assignment_operators()

    show_section("5. 位运算符")
    demo_bitwise_operators()

    show_section("6. 逻辑运算符")
    demo_logical_operators()

    show_section("7. 成员运算符")
    demo_membership_operators()

    show_section("8. 身份运算符")
    demo_identity_operators()

    show_section("9. 运算符优先级")
    demo_operator_precedence()


if __name__ == "__main__":
    main()
