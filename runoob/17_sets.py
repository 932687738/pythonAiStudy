"""17 Python3 集合

来源: https://www.runoob.com/python3/python3-set.html
可单独运行: python 17_sets.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的集合方法列表。"""
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


def demo_create_set() -> None:
    """演示使用大括号和 set() 创建集合，并说明空集合必须用 set()。"""
    set1 = {1, 2, 3, 4}
    set2 = set([4, 5, 6, 7])
    empty_set = set()
    empty_dict = {}
    print(set1)
    print(set2)
    print(f"set() -> {empty_set}, type={type(empty_set).__name__}")
    print(f"{{}} -> {empty_dict}, type={type(empty_dict).__name__}")


def demo_unique_and_membership() -> None:
    """演示集合自动去重，以及使用 in 快速判断元素是否存在。"""
    basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
    print(basket)
    print("'orange' in basket ->", "orange" in basket)
    print("'crabgrass' in basket ->", "crabgrass" in basket)


def demo_set_operations() -> None:
    """演示差集、并集、交集和对称差集。"""
    a = set("abracadabra")
    b = set("alacazam")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a - b = {a - b}")
    print(f"a | b = {a | b}")
    print(f"a & b = {a & b}")
    print(f"a ^ b = {a ^ b}")


def demo_set_comprehension() -> None:
    """演示集合推导式，生成满足条件且不重复的元素集合。"""
    result = {x for x in "abracadabra" if x not in "abc"}
    print(result)


def demo_add_and_update() -> None:
    """演示 add() 添加单个元素，update() 添加多个可迭代对象中的元素。"""
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.add("Facebook")
    print(thisset)

    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.update({1, 3})
    print(thisset)
    thisset.update([1, 4], [5, 6])
    print(thisset)


def demo_remove_discard_pop() -> None:
    """演示 remove、discard 和 pop 的区别，并捕获 remove 不存在元素的 KeyError。"""
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.remove("Taobao")
    print(thisset)
    try:
        thisset.remove("Facebook")
    except KeyError as exc:
        print(f"remove 不存在元素会报错: {exc.__class__.__name__}: {exc}")

    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.discard("Facebook")
    print(thisset)

    thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
    removed = thisset.pop()
    print(f"pop 移除: {removed}")
    print(thisset)


def demo_len_clear_and_membership() -> None:
    """演示 len() 计算集合大小、clear() 清空集合，以及成员判断。"""
    thisset = set(("Google", "Runoob", "Taobao"))
    print(len(thisset))
    print("Runoob" in thisset)
    print("Facebook" in thisset)
    thisset.clear()
    print(thisset)


def demo_set_methods_table() -> None:
    """保留页面中的集合内置方法完整列表，并执行代表性方法。"""
    a = {1, 2, 3}
    b = {3, 4, 5}
    show_table(
        ("方法", "描述", "示例结果"),
        [
            ("add()", "为集合添加元素", str(a | {4})),
            ("clear()", "移除集合中的所有元素", str(set())),
            ("copy()", "拷贝一个集合", str(a.copy())),
            ("difference()", "返回差集", str(a.difference(b))),
            ("difference_update()", "移除当前集合中也存在于指定集合的元素", "{1, 2}"),
            ("discard()", "删除指定元素，不存在不报错", "None"),
            ("intersection()", "返回交集", str(a.intersection(b))),
            ("intersection_update()", "更新为交集", "{3}"),
            ("isdisjoint()", "判断是否没有相同元素", str(a.isdisjoint({9}))),
            ("issubset()", "判断是否为子集", str({1, 2}.issubset(a))),
            ("issuperset()", "判断是否为超集", str(a.issuperset({1, 2}))),
            ("pop()", "随机移除元素", "返回被移除元素"),
            ("remove()", "移除指定元素，不存在报错", "KeyError"),
            ("symmetric_difference()", "返回对称差集", str(a.symmetric_difference(b))),
            ("symmetric_difference_update()", "更新为对称差集", "{1, 2, 4, 5}"),
            ("union()", "返回并集", str(a.union(b))),
            ("update()", "给集合添加元素", "{1, 2, 3, 4, 5}"),
            ("len()", "计算集合元素个数", str(len(a))),
        ],
    )


def demo_update_string_note() -> None:
    """保留页面笔记中的易错点：update 字符串和 update 集合含义不同。"""
    thisset = set(("Google", "Runoob", "Taobao"))
    thisset.update({"Facebook"})
    print(thisset)
    thisset.update("Yahoo")
    print(thisset)
    print("update('Yahoo') 会把字符串拆成单个字符加入集合。")


def main() -> None:
    """按集合页面顺序运行全部示例。"""
    print("Python3 集合")

    show_section("1. 创建集合")
    demo_create_set()

    show_section("2. 去重与成员判断")
    demo_unique_and_membership()

    show_section("3. 集合运算")
    demo_set_operations()

    show_section("4. 集合推导式")
    demo_set_comprehension()

    show_section("5. 添加元素")
    demo_add_and_update()

    show_section("6. 移除元素")
    demo_remove_discard_pop()

    show_section("7. 长度、清空和成员判断")
    demo_len_clear_and_membership()

    show_section("8. 集合方法表")
    demo_set_methods_table()

    show_section("9. update 字符串注意点")
    demo_update_string_note()


if __name__ == "__main__":
    main()
