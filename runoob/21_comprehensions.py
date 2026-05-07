"""21 Python3 推导式

来源: https://www.runoob.com/python3/python-comprehensions.html
可单独运行: python 21_comprehensions.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的推导式格式说明。"""
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


def demo_syntax_table() -> None:
    """保留页面列出的四类推导式格式。"""
    show_table(
        ("类型", "基本格式", "带条件格式"),
        [
            ("列表推导式", "[表达式 for 变量 in 列表]", "[表达式 for 变量 in 列表 if 条件]"),
            ("字典推导式", "{key: value for value in collection}", "{key: value for value in collection if 条件}"),
            ("集合推导式", "{expression for item in Sequence}", "{expression for item in Sequence if 条件}"),
            ("元组推导式", "(expression for item in Sequence)", "(expression for item in Sequence if 条件)"),
        ],
    )


def demo_list_comprehension() -> None:
    """执行页面中的列表推导式：过滤短字符串并转大写、筛选 30 内 3 的倍数。"""
    names = ["Bob", "Tom", "alice", "Jerry", "Wendy", "Smith"]
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)

    multiples = [item for item in range(30) if item % 3 == 0]
    print(multiples)


def demo_dict_comprehension() -> None:
    """执行页面中的字典推导式：字符串长度字典和数字平方字典。"""
    listdemo = ["Google", "Runoob", "Taobao"]
    newdict = {key: len(key) for key in listdemo}
    print(newdict)

    dic = {x: x**2 for x in (2, 4, 6)}
    print(dic)
    print(type(dic))


def demo_set_comprehension() -> None:
    """执行页面中的集合推导式：平方集合和过滤字符集合。"""
    setnew = {item**2 for item in (1, 2, 3)}
    print(setnew)

    letters = {char for char in "abracadabra" if char not in "abc"}
    print(letters)
    print(type(letters))


def demo_tuple_comprehension() -> None:
    """执行页面中的元组推导式，说明其返回生成器对象，需要 tuple() 才能展开。"""
    generator = (x for x in range(1, 10))
    print(generator)
    print(tuple(generator))


def demo_conditional_expression_note() -> None:
    """保留页面笔记中的条件表达式推导式写法。"""
    words = ["python", "test1", "test2"]
    result = [word.title() if word.startswith("p") else word.upper() for word in words]
    print(result)


def main() -> None:
    """按推导式页面顺序运行全部示例。"""
    print("Python3 推导式")

    show_section("1. 推导式格式")
    demo_syntax_table()

    show_section("2. 列表推导式")
    demo_list_comprehension()

    show_section("3. 字典推导式")
    demo_dict_comprehension()

    show_section("4. 集合推导式")
    demo_set_comprehension()

    show_section("5. 元组推导式")
    demo_tuple_comprehension()

    show_section("6. 条件表达式补充")
    demo_conditional_expression_note()


if __name__ == "__main__":
    main()
