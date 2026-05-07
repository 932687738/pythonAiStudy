"""12 Python3 数字(Number)

来源: https://www.runoob.com/python3/python3-number.html
可单独运行: python 12_numbers.py
"""

from __future__ import annotations

import math
import random


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的函数表和常量表。"""
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


def demo_number_creation_and_delete() -> None:
    """演示 Number 对象在变量赋值时创建，并用 del 删除引用。"""
    var1 = 1
    var2 = 10
    print(f"var1={var1}, var2={var2}")
    del var1
    try:
        print(var1)
    except NameError as exc:
        print(f"del var1 后访问失败: {exc.__class__.__name__}")


def demo_number_types() -> None:
    """保留页面列出的 int、float、complex 类型说明，并执行典型示例。"""
    show_table(
        ("类型", "说明", "示例"),
        [
            ("int", "整数，Python3 中大小不受固定 long 限制", "10, -786, 0x69"),
            ("float", "浮点数，可用科学计数法", "0.0, 15.20, 32.3e18"),
            ("complex", "复数，由实部和虚部组成", "3.14j, 45.j, 4.53e-7j"),
        ],
    )
    numbers = [10, 0.0, 3.14j, 100, 15.20, 45j, -786, -21.9, 9.322e-36j]
    for value in numbers:
        print(f"{value!r} -> {type(value).__name__}")


def demo_hex_and_octal() -> None:
    """演示十六进制和八进制整数写法。"""
    number = 0xA0F
    print(f"0xA0F -> {number}")
    number = 0o37
    print(f"0o37 -> {number}")


def demo_number_conversion() -> None:
    """演示数字类型转换：int、float、complex。"""
    print(f"int(1.0) -> {int(1.0)}")
    print(f"float(10) -> {float(10)}")
    print(f"complex(10) -> {complex(10)}")
    print(f"complex(10, 2) -> {complex(10, 2)}")


def demo_number_operations() -> None:
    """复刻页面中把 Python 解释器当计算器使用的数字运算示例。"""
    print(f"2 + 2 -> {2 + 2}")
    print(f"50 - 5 * 6 -> {50 - 5 * 6}")
    print(f"(50 - 5 * 6) / 4 -> {(50 - 5 * 6) / 4}")
    print(f"8 / 5 -> {8 / 5}")
    print(f"17 / 3 -> {17 / 3}")
    print(f"17 // 3 -> {17 // 3}")
    print(f"17 % 3 -> {17 % 3}")
    print(f"5 * 3 + 2 -> {5 * 3 + 2}")
    print(f"7 // 2 -> {7 // 2}")
    print(f"7.0 // 2 -> {7.0 // 2}")
    print(f"7 // 2.0 -> {7 // 2.0}")


def demo_assignment_and_power() -> None:
    """演示赋值、面积计算和 ** 幂运算。"""
    width = 20
    height = 5 * 9
    print(f"width * height -> {width * height}")
    print(f"5 ** 2 -> {5 ** 2}")
    print(f"2 ** 7 -> {2 ** 7}")


def demo_undefined_variable() -> None:
    """演示变量使用前必须先赋值，否则会出现 NameError。"""
    try:
        print(n)  # type: ignore[name-defined]
    except NameError as exc:
        print(f"访问未定义变量 n: {exc.__class__.__name__}")


def demo_mixed_number_operations() -> None:
    """演示不同数字类型混合运算时，整数会转换为浮点数。"""
    print(f"3 * 3.75 / 1.5 -> {3 * 3.75 / 1.5}")
    print(f"7.0 / 2 -> {7.0 / 2}")


def demo_last_result_note() -> None:
    """模拟交互模式中 _ 保存上一次表达式结果的效果。"""
    tax = 12.5 / 100
    price = 100.50
    last = price * tax
    print(f"price * tax -> {last}")
    last = price + last
    print(f"price + _ -> {last}")
    print(f"round(_, 2) -> {round(last, 2)}")


def demo_math_functions() -> None:
    """保留页面数学函数表，并执行每个函数的代表性示例。"""
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("abs(x)", "返回绝对值", str(abs(-10))),
            ("ceil(x)", "向上取整", str(math.ceil(4.1))),
            ("cmp(x,y)", "Python3 已废弃，可用 (x>y)-(x<y)", str((3 > 2) - (3 < 2))),
            ("exp(x)", "e 的 x 次幂", str(math.exp(1))),
            ("fabs(x)", "浮点绝对值", str(math.fabs(-10))),
            ("floor(x)", "向下取整", str(math.floor(4.9))),
            ("log(x)", "自然对数", str(math.log(math.e))),
            ("log10(x)", "以 10 为底的对数", str(math.log10(100))),
            ("max(...)", "最大值", str(max(1, 2, 3))),
            ("min(...)", "最小值", str(min(1, 2, 3))),
            ("modf(x)", "返回小数和整数部分", str(math.modf(3.14))),
            ("pow(x,y)", "x 的 y 次方", str(pow(2, 3))),
            ("round(x,n)", "四舍五入", str(round(3.14159, 2))),
            ("sqrt(x)", "平方根", str(math.sqrt(16))),
        ],
    )


def demo_random_functions() -> None:
    """保留页面随机数函数表，并用固定种子让输出可复现。"""
    random.seed(7)
    values = [1, 2, 3, 4, 5]
    shuffled = values[:]
    random.shuffle(shuffled)
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("choice(seq)", "从序列随机挑选一个元素", str(random.choice(range(10)))),
            ("randrange(...)", "从指定范围按步长获取随机数", str(random.randrange(0, 10, 2))),
            ("random()", "生成 [0,1) 实数", str(round(random.random(), 4))),
            ("seed([x])", "设置随机种子", "random.seed(7)"),
            ("shuffle(lst)", "随机排序列表", str(shuffled)),
            ("uniform(x,y)", "生成 [x,y] 实数", str(round(random.uniform(1, 5), 4))),
        ],
    )


def demo_trigonometric_functions() -> None:
    """保留页面三角函数表，并执行每个函数的代表性示例。"""
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("acos(x)", "反余弦弧度值", str(math.acos(1))),
            ("asin(x)", "反正弦弧度值", str(math.asin(1))),
            ("atan(x)", "反正切弧度值", str(math.atan(1))),
            ("atan2(y,x)", "坐标反正切值", str(math.atan2(1, 1))),
            ("cos(x)", "余弦值", str(math.cos(0))),
            ("hypot(x,y)", "欧几里得范数", str(math.hypot(3, 4))),
            ("sin(x)", "正弦值", str(math.sin(math.pi / 2))),
            ("tan(x)", "正切值", str(round(math.tan(math.pi / 4), 10))),
            ("degrees(x)", "弧度转角度", str(math.degrees(math.pi / 2))),
            ("radians(x)", "角度转弧度", str(math.radians(180))),
        ],
    )


def demo_math_constants() -> None:
    """保留页面数学常量表。"""
    show_table(
        ("常量", "描述", "值"),
        [
            ("pi", "圆周率", str(math.pi)),
            ("e", "自然常数", str(math.e)),
        ],
    )


def main() -> None:
    """按数字(Number)页面顺序运行全部示例。"""
    print("Python3 数字(Number)")

    show_section("1. 数字对象创建与删除")
    demo_number_creation_and_delete()

    show_section("2. 数字类型")
    demo_number_types()

    show_section("3. 十六进制与八进制")
    demo_hex_and_octal()

    show_section("4. 数字类型转换")
    demo_number_conversion()

    show_section("5. 数字运算")
    demo_number_operations()

    show_section("6. 赋值与幂运算")
    demo_assignment_and_power()

    show_section("7. 未定义变量")
    demo_undefined_variable()

    show_section("8. 混合类型运算")
    demo_mixed_number_operations()

    show_section("9. 交互模式 _ 变量")
    demo_last_result_note()

    show_section("10. 数学函数")
    demo_math_functions()

    show_section("11. 随机数函数")
    demo_random_functions()

    show_section("12. 三角函数")
    demo_trigonometric_functions()

    show_section("13. 数学常量")
    demo_math_constants()


if __name__ == "__main__":
    main()
