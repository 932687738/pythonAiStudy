"""07 Python3 基本数据类型

来源: https://www.runoob.com/python3/python3-data-type.html
可单独运行: python 07_basic_data_types.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，方便运行输出按教程小节阅读。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的表格类信息。"""
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


def demo_variable_assignment() -> None:
    """演示变量创建、单变量赋值、多变量赋值和连续赋值。"""
    print("Python 中的变量不需要声明，变量在赋值后才会被创建。")
    counter = 100
    miles = 1000.0
    name = "runoob"
    print(counter)
    print(miles)
    print(name)

    print("多个变量赋值：")
    a = b = c = 1
    print(f"a={a}, b={b}, c={c}")

    a, b, c = 1, 2, "runoob"
    print(f"a={a}, b={b}, c={c}")


def demo_standard_types() -> None:
    """整理 Python3 页面列出的标准数据类型，并标明是否可变。"""
    show_table(
        ("类型", "说明", "是否可变"),
        [
            ("Number", "数字", "不可变"),
            ("String", "字符串", "不可变"),
            ("List", "列表", "可变"),
            ("Tuple", "元组", "不可变"),
            ("Set", "集合", "可变"),
            ("Dictionary", "字典", "可变"),
            ("Bytes", "字节序列", "不可变"),
        ],
    )


def demo_number() -> None:
    """演示 Number 类型：int、float、bool、complex，以及 del 删除引用。"""
    print("Python3 支持 int、float、bool、complex。")
    values = [20, 5.5, True, 4 + 3j]
    for value in values:
        print(f"{value!r} -> {type(value)}")

    print("删除对象引用：")
    number = 10
    print(f"删除前 number={number}")
    del number
    try:
        print(number)
    except NameError as exc:
        print(f"删除后访问会报错: {exc.__class__.__name__}")


def demo_string() -> None:
    """演示字符串索引、切片、重复、拼接、转义和原始字符串。"""
    text = "Runoob"
    print(text)
    print(text[0:-1])
    print(text[0])
    print(text[2:5])
    print(text[2:])
    print(text * 2)
    print(text + "TEST")

    print("反斜杠可以转义，r 前缀可以让字符串不转义：")
    print("Ru\noob")
    print(r"Ru\noob")


def demo_list() -> None:
    """演示列表的索引、切片、重复、拼接，以及列表可变特性。"""
    items = ["abcd", 786, 2.23, "runoob", 70.2]
    tiny_list = [123, "runoob"]

    print(items)
    print(items[0])
    print(items[1:3])
    print(items[2:])
    print(tiny_list * 2)
    print(items + tiny_list)

    print("列表是可变的：")
    items[0] = "changed"
    print(items)


def demo_tuple() -> None:
    """演示元组的索引、切片、重复、拼接，以及元组不可变特性。"""
    items = ("abcd", 786, 2.23, "runoob", 70.2)
    tiny_tuple = (123, "runoob")

    print(items)
    print(items[0])
    print(items[1:3])
    print(items[2:])
    print(tiny_tuple * 2)
    print(items + tiny_tuple)

    print("元组不可变：")
    try:
        items[0] = "changed"  # type: ignore[index]
    except TypeError as exc:
        print(f"修改元组会报错: {exc.__class__.__name__}")

    empty_tuple = ()
    one_item_tuple = (20,)
    print(f"空元组: {empty_tuple}")
    print(f"一个元素的元组需要逗号: {one_item_tuple}")


def demo_set() -> None:
    """演示集合去重、成员判断和差集/并集/交集/对称差集运算。"""
    student = {"Tom", "Jim", "Mary", "Tom", "Jack", "Rose"}
    print(student)
    print("Rose" in student)

    a = set("abracadabra")
    b = set("alacazam")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a - b = {a - b}")
    print(f"a | b = {a | b}")
    print(f"a & b = {a & b}")
    print(f"a ^ b = {a ^ b}")


def demo_dictionary() -> None:
    """演示字典赋值、按键取值、keys/values，以及字典键的限制。"""
    dictionary = {}
    dictionary["one"] = "1 - 菜鸟教程"
    dictionary[2] = "2 - 菜鸟工具"
    tiny_dict = {"name": "runoob", "code": 1, "site": "www.runoob.com"}

    print(dictionary["one"])
    print(dictionary[2])
    print(tiny_dict)
    print(tiny_dict.keys())
    print(tiny_dict.values())

    print("字典的键必须是不可变类型：")
    valid = {(1, 2): "tuple key"}
    print(valid)
    try:
        invalid = {}
        invalid[[1, 2]] = "list key"  # type: ignore[index]
    except TypeError as exc:
        print(f"列表不能作为字典键: {exc.__class__.__name__}")


def demo_bytes() -> None:
    """演示字符串和 bytes 之间的 UTF-8 编码、解码，以及 bytes 构造。"""
    text = "中文"
    data = text.encode("utf-8")
    print(f"字符串: {text}")
    print(f"编码为 bytes: {data}")
    print(f"解码回字符串: {data.decode('utf-8')}")

    binary = bytes([65, 66, 67])
    print(f"bytes([65, 66, 67]) -> {binary}")


def demo_type_conversion() -> None:
    """保留页面中的数据类型转换函数表，并给出可执行转换结果。"""
    show_table(
        ("函数", "说明", "示例结果"),
        [
            ("int(x)", "将 x 转换为整数", str(int("10"))),
            ("float(x)", "将 x 转换为浮点数", str(float("10.5"))),
            ("str(x)", "将对象转换为字符串", str(str(123))),
            ("tuple(s)", "将序列转换为元组", str(tuple([1, 2, 3]))),
            ("list(s)", "将序列转换为列表", str(list((1, 2, 3)))),
            ("set(s)", "将序列转换为集合", str(set([1, 1, 2]))),
            ("dict(d)", "创建字典", str(dict([("a", 1), ("b", 2)]))),
            ("bytes(s)", "转换为字节序列", str(bytes("hi", "utf-8"))),
        ],
    )


def main() -> None:
    """按页面顺序运行所有基本数据类型示例。"""
    print("Python3 基本数据类型")

    show_section("1. 变量赋值")
    demo_variable_assignment()

    show_section("2. 标准数据类型")
    demo_standard_types()

    show_section("3. Number 数字")
    demo_number()

    show_section("4. String 字符串")
    demo_string()

    show_section("5. List 列表")
    demo_list()

    show_section("6. Tuple 元组")
    demo_tuple()

    show_section("7. Set 集合")
    demo_set()

    show_section("8. Dictionary 字典")
    demo_dictionary()

    show_section("9. Bytes 字节")
    demo_bytes()

    show_section("10. 数据类型转换")
    demo_type_conversion()


if __name__ == "__main__":
    main()
