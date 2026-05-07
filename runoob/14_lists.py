"""14 Python3 列表

来源: https://www.runoob.com/python3/python3-list.html
可单独运行: python 14_lists.py
"""

from __future__ import annotations

import operator


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的列表函数和方法表。"""
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


def demo_create_lists() -> None:
    """演示创建列表，列表元素不要求类型相同。"""
    list1 = ["Google", "Runoob", 1997, 2000]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]
    list4 = ["red", "green", "blue", "yellow", "white", "black"]
    print(list1)
    print(list2)
    print(list3)
    print(list4)


def demo_access_positive_index() -> None:
    """演示通过正向索引访问列表元素，索引从 0 开始。"""
    colors = ["red", "green", "blue", "yellow", "white", "black"]
    print(colors[0])
    print(colors[1])
    print(colors[2])


def demo_access_negative_index() -> None:
    """演示通过负向索引访问列表元素，-1 表示最后一个元素。"""
    colors = ["red", "green", "blue", "yellow", "white", "black"]
    print(colors[-1])
    print(colors[-2])
    print(colors[-3])


def demo_slice() -> None:
    """演示列表切片，左闭右开，并保留负数索引截取示例。"""
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(nums[0:4])

    sites = ["Google", "Runoob", "Zhihu", "Taobao", "Wiki"]
    print("list[1]: ", sites[1])
    print("list[1:-2]: ", sites[1:-2])


def demo_update_list() -> None:
    """演示修改列表元素和 append() 追加元素。"""
    items = ["Google", "Runoob", 1997, 2000]
    print("第三个元素为 : ", items[2])
    items[2] = 2001
    print("更新后的第三个元素为 : ", items[2])

    list1 = ["Google", "Runoob", "Taobao"]
    list1.append("Baidu")
    print("更新后的列表 : ", list1)


def demo_delete_list_item() -> None:
    """演示使用 del 删除列表中的指定元素。"""
    items = ["Google", "Runoob", 1997, 2000]
    print("原始列表 : ", items)
    del items[2]
    print("删除第三个元素 : ", items)


def demo_list_operators() -> None:
    """保留列表脚本操作符表，并执行长度、拼接、重复、成员判断和迭代。"""
    show_table(
        ("Python 表达式", "结果", "描述"),
        [
            ("len([1, 2, 3])", str(len([1, 2, 3])), "长度"),
            ("[1,2,3] + [4,5,6]", str([1, 2, 3] + [4, 5, 6]), "组合"),
            ("['Hi!'] * 4", str(["Hi!"] * 4), "重复"),
            ("3 in [1,2,3]", str(3 in [1, 2, 3]), "元素是否存在"),
            ("for x in [1,2,3]", "1 2 3", "迭代"),
        ],
    )
    for item in [1, 2, 3]:
        print(item, end=" ")
    print()


def demo_list_slice_and_concat() -> None:
    """演示列表截取与拼接，复刻交互式示例。"""
    values = ["Google", "Runoob", "Taobao"]
    print(values[2])
    print(values[-2])
    print(values[1:])

    squares = [1, 4, 9, 16, 25]
    squares += [36, 49, 64, 81, 100]
    print(squares)


def demo_nested_list() -> None:
    """演示嵌套列表以及两级索引访问。"""
    letters = ["a", "b", "c"]
    numbers = [1, 2, 3]
    nested = [letters, numbers]
    print(nested)
    print(nested[0])
    print(nested[0][1])


def demo_list_compare() -> None:
    """演示使用 operator.eq 比较两个列表是否相等。"""
    a = [1, 2]
    b = [2, 3]
    c = [2, 3]
    print("operator.eq(a,b): ", operator.eq(a, b))
    print("operator.eq(c,b): ", operator.eq(c, b))


def demo_list_functions() -> None:
    """保留列表内置函数表，并执行函数示例。"""
    numbers = [3, 1, 2]
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("len(list)", "列表元素个数", str(len(numbers))),
            ("max(list)", "返回列表元素最大值", str(max(numbers))),
            ("min(list)", "返回列表元素最小值", str(min(numbers))),
            ("list(seq)", "将元组转换为列表", str(list((1, 2, 3)))),
        ],
    )


def demo_list_methods() -> None:
    """保留列表常用方法表，并执行每个方法的代表性示例。"""
    values = [1, 2, 3]
    values.append(4)
    count_result = [1, 1, 2].count(1)
    extended = [1, 2]
    extended.extend([3, 4])
    index_result = extended.index(3)
    inserted = [1, 3]
    inserted.insert(1, 2)
    popped = inserted.pop()
    removable = [1, 2, 2, 3]
    removable.remove(2)
    reversed_values = [1, 2, 3]
    reversed_values.reverse()
    sorted_values = [3, 1, 2]
    sorted_values.sort()
    copy_values = sorted_values.copy()
    cleared = [1, 2, 3]
    cleared.clear()

    show_table(
        ("方法", "描述", "示例结果"),
        [
            ("append(obj)", "末尾添加对象", str(values)),
            ("count(obj)", "统计元素次数", str(count_result)),
            ("extend(seq)", "扩展列表", str(extended)),
            ("index(obj)", "找出索引位置", str(index_result)),
            ("insert(index,obj)", "指定位置插入", str(inserted)),
            ("pop([index])", "移除并返回元素", str(popped)),
            ("remove(obj)", "移除第一个匹配项", str(removable)),
            ("reverse()", "反向列表", str(reversed_values)),
            ("sort()", "排序列表", str(sorted_values)),
            ("copy()", "复制列表", str(copy_values)),
            ("clear()", "清空列表", str(cleared)),
        ],
    )


def main() -> None:
    """按列表页面顺序运行全部示例。"""
    print("Python3 列表")

    show_section("1. 创建列表")
    demo_create_lists()

    show_section("2. 正向索引")
    demo_access_positive_index()

    show_section("3. 负向索引")
    demo_access_negative_index()

    show_section("4. 列表切片")
    demo_slice()

    show_section("5. 更新列表")
    demo_update_list()

    show_section("6. 删除列表元素")
    demo_delete_list_item()

    show_section("7. 列表脚本操作符")
    demo_list_operators()

    show_section("8. 列表截取与拼接")
    demo_list_slice_and_concat()

    show_section("9. 嵌套列表")
    demo_nested_list()

    show_section("10. 列表比较")
    demo_list_compare()

    show_section("11. 列表函数")
    demo_list_functions()

    show_section("12. 列表方法")
    demo_list_methods()


if __name__ == "__main__":
    main()
