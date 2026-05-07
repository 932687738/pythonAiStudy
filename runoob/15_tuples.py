"""15 Python3 元组

来源: https://www.runoob.com/python3/python3-tuple.html
可单独运行: python 15_tuples.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的元组运算符和函数表。"""
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


def demo_create_tuple() -> None:
    """演示元组创建方式，包括不使用括号也能创建元组。"""
    tup1 = ("Google", "Runoob", 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = "a", "b", "c", "d"
    print(tup1)
    print(tup2)
    print(tup3)
    print(type(tup3))


def demo_empty_and_single_tuple() -> None:
    """演示空元组和单元素元组，强调单元素元组必须带逗号。"""
    empty_tuple = ()
    not_tuple = (50)
    one_item_tuple = (50,)
    print(f"empty_tuple -> {empty_tuple}, type={type(empty_tuple).__name__}")
    print(f"(50) -> {not_tuple}, type={type(not_tuple).__name__}")
    print(f"(50,) -> {one_item_tuple}, type={type(one_item_tuple).__name__}")


def demo_access_tuple() -> None:
    """演示使用下标索引和切片访问元组。"""
    tup1 = ("Google", "Runoob", 1997, 2000)
    tup2 = (1, 2, 3, 4, 5, 6, 7)
    print("tup1[0]: ", tup1[0])
    print("tup2[1:5]: ", tup2[1:5])


def demo_update_tuple() -> None:
    """演示元组元素不可修改，但可以连接生成新的元组。"""
    tup1 = (12, 34.56)
    tup2 = ("abc", "xyz")
    try:
        tup1[0] = 100  # type: ignore[index]
    except TypeError as exc:
        print(f"尝试修改元组元素失败: {exc.__class__.__name__}")

    tup3 = tup1 + tup2
    print(tup3)


def demo_delete_tuple() -> None:
    """演示元组元素不能单独删除，但可以用 del 删除整个元组引用。"""
    tup = ("Google", "Runoob", 1997, 2000)
    print(tup)
    del tup
    print("删除后的元组 tup : ")
    try:
        print(tup)  # type: ignore[name-defined]
    except NameError as exc:
        print(f"访问已删除元组失败: {exc.__class__.__name__}")


def demo_tuple_operators() -> None:
    """保留元组运算符表，并执行长度、连接、复制、成员判断和迭代。"""
    a = (1, 2, 3)
    b = (4, 5, 6)
    c = a + b
    a += b
    repeated = ("Hi!",) * 4
    contains = 3 in (1, 2, 3)
    show_table(
        ("Python 表达式", "结果", "描述"),
        [
            ("len((1, 2, 3))", str(len((1, 2, 3))), "计算元素个数"),
            ("(1,2,3)+(4,5,6)", str(c), "连接，生成新元组"),
            ("a += b", str(a), "连接后重新绑定变量"),
            ("('Hi!',) * 4", str(repeated), "复制"),
            ("3 in (1,2,3)", str(contains), "元素是否存在"),
            ("for x in (1,2,3)", "1 2 3", "迭代"),
        ],
    )
    for item in (1, 2, 3):
        print(item, end=" ")
    print()


def demo_tuple_index_and_slice() -> None:
    """演示元组索引和截取，复刻页面 tup 示例。"""
    tup = ("Google", "Runoob", "Taobao", "Wiki", "Weibo", "Weixin")
    show_table(
        ("表达式", "结果", "描述"),
        [
            ("tup[1]", str(tup[1]), "读取第二个元素"),
            ("tup[-2]", str(tup[-2]), "反向读取倒数第二个元素"),
            ("tup[1:]", str(tup[1:]), "从第二个开始截取"),
            ("tup[1:4]", str(tup[1:4]), "从第二个截取到第四个元素"),
        ],
    )


def demo_tuple_functions() -> None:
    """保留元组内置函数表，并执行 len、max、min、tuple 示例。"""
    tuple1 = ("Google", "Runoob", "Taobao")
    tuple2 = ("5", "4", "8")
    list1 = ["Google", "Taobao", "Runoob", "Baidu"]
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("len(tuple)", "计算元组元素个数", str(len(tuple1))),
            ("max(tuple)", "返回元组中元素最大值", str(max(tuple2))),
            ("min(tuple)", "返回元组中元素最小值", str(min(tuple2))),
            ("tuple(iterable)", "将可迭代系列转换为元组", str(tuple(list1))),
        ],
    )


def demo_tuple_immutability() -> None:
    """说明元组不可变指向不变，重新赋值会绑定到新对象。"""
    tup = ("r", "u", "n", "o", "o", "b")
    old_id = id(tup)
    try:
        tup[0] = "g"  # type: ignore[index]
    except TypeError as exc:
        print(f"修改 tup[0] 失败: {exc.__class__.__name__}")
    print(f"旧元组 id: {old_id}")
    tup = (1, 2, 3)
    print(f"重新赋值后元组 id: {id(tup)}")

    tricky = ("a", "b", ["A", "B"])
    tricky[2][0] = "X"
    tricky[2][1] = "Y"
    print(f"包含列表的元组: {tricky}")
    print("元组元素指向的列表没换，但列表内部内容可以改变。")


def main() -> None:
    """按元组页面顺序运行全部示例。"""
    print("Python3 元组")

    show_section("1. 创建元组")
    demo_create_tuple()

    show_section("2. 空元组与单元素元组")
    demo_empty_and_single_tuple()

    show_section("3. 访问元组")
    demo_access_tuple()

    show_section("4. 修改元组")
    demo_update_tuple()

    show_section("5. 删除元组")
    demo_delete_tuple()

    show_section("6. 元组运算符")
    demo_tuple_operators()

    show_section("7. 元组索引与截取")
    demo_tuple_index_and_slice()

    show_section("8. 元组内置函数")
    demo_tuple_functions()

    show_section("9. 关于元组不可变")
    demo_tuple_immutability()


if __name__ == "__main__":
    main()
