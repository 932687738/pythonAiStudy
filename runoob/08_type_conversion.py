"""08 Python3 数据类型转换

来源: https://www.runoob.com/python3/python3-type-conversion.html
可单独运行: python 08_type_conversion.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的转换函数表。"""
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


def demo_implicit_conversion() -> None:
    """演示整数和浮点数相加时，Python 自动执行隐式类型转换。"""
    num_int = 123
    num_flo = 1.23
    num_new = num_int + num_flo

    print("num_int 数据类型为:", type(num_int))
    print("num_flo 数据类型为:", type(num_flo))
    print("num_new 值为:", num_new)
    print("num_new 数据类型为:", type(num_new))


def demo_implicit_conversion_error() -> None:
    """演示整数和字符串不能直接相加，页面中的 TypeError 逻辑保留为可运行示例。"""
    num_int = 123
    num_str = "456"

    print("num_int 数据类型为:", type(num_int))
    print("num_str 数据类型为:", type(num_str))
    try:
        print(num_int + num_str)  # type: ignore[operator]
    except TypeError as exc:
        print("整数和字符串不能隐式相加。")
        print(f"捕获异常: {exc.__class__.__name__}: {exc}")


def demo_int_conversion() -> None:
    """演示 int() 强制转换为整型，包含整数、浮点数和数字字符串。"""
    x = int(1)
    y = int(2.8)
    z = int("3")
    print(f"int(1) -> {x}")
    print(f"int(2.8) -> {y}")
    print(f"int('3') -> {z}")


def demo_float_conversion() -> None:
    """演示 float() 强制转换为浮点型。"""
    x = float(1)
    y = float(2.8)
    z = float("3")
    w = float("4.2")
    print(f"float(1) -> {x}")
    print(f"float(2.8) -> {y}")
    print(f"float('3') -> {z}")
    print(f"float('4.2') -> {w}")


def demo_str_conversion() -> None:
    """演示 str() 将对象转换为字符串。"""
    x = str("s1")
    y = str(2)
    z = str(3.0)
    print(f"str('s1') -> {x!r}")
    print(f"str(2) -> {y!r}")
    print(f"str(3.0) -> {z!r}")


def demo_explicit_addition() -> None:
    """演示把数字字符串显式转换成整数后再参与加法运算。"""
    num_int = 123
    num_str = "456"

    print("num_int 数据类型为:", type(num_int))
    print("类型转换前，num_str 数据类型为:", type(num_str))

    num_str = int(num_str)
    print("类型转换后，num_str 数据类型为:", type(num_str))

    num_sum = num_int + num_str
    print("num_int 与 num_str 相加结果为:", num_sum)
    print("sum 数据类型为:", type(num_sum))


def demo_conversion_table() -> None:
    """保留页面列出的常用类型转换函数，并给出可执行结果。"""
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("int(x [,base])", "将 x 转换为整数", str(int("10"))),
            ("float(x)", "将 x 转换到浮点数", str(float("10.5"))),
            ("complex(real [,imag])", "创建一个复数", str(complex(1, 2))),
            ("str(x)", "将对象 x 转换为字符串", repr(str(123))),
            ("repr(x)", "将对象 x 转换为表达式字符串", repr(repr("中文"))),
            ("eval(str)", "计算字符串中的有效 Python 表达式", str(eval("1 + 2"))),
            ("tuple(s)", "将序列 s 转换为元组", str(tuple([1, 2, 3]))),
            ("list(s)", "将序列 s 转换为列表", str(list((1, 2, 3)))),
            ("set(s)", "转换为可变集合", str(set([1, 1, 2]))),
            ("dict(d)", "创建字典", str(dict([("a", 1), ("b", 2)]))),
            ("frozenset(s)", "转换为不可变集合", str(frozenset([1, 2]))),
            ("chr(x)", "将整数转换为字符", chr(97)),
            ("ord(x)", "将字符转换为整数值", str(ord("a"))),
            ("hex(x)", "将整数转换为十六进制字符串", hex(255)),
            ("oct(x)", "将整数转换为八进制字符串", oct(8)),
            ("bool(x)", "将对象转换为布尔值", str(bool(1))),
            ("bytes(...)", "转换为不可变字节序列", str(bytes("hi", "utf-8"))),
            ("bytearray(...)", "转换为可变字节数组", str(bytearray("hi", "utf-8"))),
            ("memoryview(obj)", "返回内存视图对象", str(memoryview(b"hi").tolist())),
            ("bin(x)", "将整数转换为二进制字符串", bin(7)),
            ("ascii(x)", "返回 ASCII 表示，非 ASCII 会被转义", ascii("中文")),
        ],
    )


def demo_conversion_limits() -> None:
    """补充说明并演示：不是所有数据都能任意转换，转换取决于原始数据是否足够表达目标类型。"""
    examples = ["123", "10.5", "Hello"]
    for value in examples:
        try:
            result = int(value)
            print(f"int({value!r}) -> {result}")
        except ValueError as exc:
            print(f"int({value!r}) 转换失败: {exc.__class__.__name__}")


def main() -> None:
    """按数据类型转换页面顺序运行全部示例。"""
    print("Python3 数据类型转换")

    show_section("1. 隐式类型转换")
    demo_implicit_conversion()

    show_section("2. 不能隐式转换的情况")
    demo_implicit_conversion_error()

    show_section("3. int() 强制转换")
    demo_int_conversion()

    show_section("4. float() 强制转换")
    demo_float_conversion()

    show_section("5. str() 强制转换")
    demo_str_conversion()

    show_section("6. 显式转换后再运算")
    demo_explicit_addition()

    show_section("7. 类型转换函数表")
    demo_conversion_table()

    show_section("8. 转换限制")
    demo_conversion_limits()


if __name__ == "__main__":
    main()
