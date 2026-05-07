"""16 Python3 字典

来源: https://www.runoob.com/python3/python3-dictionary.html
可单独运行: python 16_dictionaries.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的字典函数和方法表。"""
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


def demo_create_dictionary() -> None:
    """演示字典的基本格式、键值对结构，以及不同类型键的创建方式。"""
    tinydict = {"name": "runoob", "likes": 123, "url": "www.runoob.com"}
    tinydict1 = {"abc": 456}
    tinydict2 = {"abc": 123, 98.6: 37}
    print(tinydict)
    print(tinydict1)
    print(tinydict2)
    print("键必须唯一，值可以是任意类型；键必须是不可变类型。")


def demo_empty_dictionary() -> None:
    """演示用 {} 和 dict() 创建空字典，并查看长度和类型。"""
    empty_dict = {}
    print(empty_dict)
    print("Length:", len(empty_dict))
    print(type(empty_dict))

    empty_dict = dict()
    print(empty_dict)
    print("Length:", len(empty_dict))
    print(type(empty_dict))


def demo_access_dictionary() -> None:
    """演示使用方括号按键访问字典值，并捕获缺失键 KeyError。"""
    tinydict = {"Name": "Runoob", "Age": 7, "Class": "First"}
    print("tinydict['Name']: ", tinydict["Name"])
    print("tinydict['Age']: ", tinydict["Age"])

    try:
        print("tinydict['Alice']: ", tinydict["Alice"])
    except KeyError as exc:
        print(f"访问不存在的键失败: {exc.__class__.__name__}: {exc}")


def demo_update_dictionary() -> None:
    """演示修改已有键值和添加新的键值对。"""
    tinydict = {"Name": "Runoob", "Age": 7, "Class": "First"}
    tinydict["Age"] = 8
    tinydict["School"] = "菜鸟教程"
    print("tinydict['Age']: ", tinydict["Age"])
    print("tinydict['School']: ", tinydict["School"])


def demo_delete_dictionary_items() -> None:
    """演示 del 删除单个键、clear 清空字典，以及 del 删除整个字典引用。"""
    tinydict = {"Name": "Runoob", "Age": 7, "Class": "First"}
    print("原始字典:", tinydict)
    del tinydict["Name"]
    print("删除 Name 后:", tinydict)
    tinydict.clear()
    print("clear 后:", tinydict)
    del tinydict
    try:
        print(tinydict)  # type: ignore[name-defined]
    except NameError as exc:
        print(f"del 字典后访问失败: {exc.__class__.__name__}")


def demo_key_features() -> None:
    """演示字典键的两个特性：重复键保留最后一个值，列表不能作为键。"""
    tinydict = {"Name": "Runoob", "Age": 7, "Name": "小菜鸟"}
    print("tinydict['Name']: ", tinydict["Name"])

    valid = {(1, 2): "tuple key", 10: "number key", "name": "string key"}
    print("不可变类型可作为键:", valid)

    try:
        invalid = {["Name"]: "Runoob", "Age": 7}  # type: ignore[list-item]
        print(invalid)
    except TypeError as exc:
        print(f"列表不能作为字典键: {exc.__class__.__name__}: {exc}")


def demo_builtin_functions() -> None:
    """保留字典内置函数表，并执行 len、str、type 示例。"""
    tinydict = {"Name": "Runoob", "Age": 7, "Class": "First"}
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("len(dict)", "计算字典元素个数", str(len(tinydict))),
            ("str(dict)", "输出字典的字符串表示", str(tinydict)),
            ("type(variable)", "返回变量类型", str(type(tinydict))),
        ],
    )


def demo_dictionary_methods() -> None:
    """保留字典内置方法表，并执行每个常用方法的代表性示例。"""
    base = {"Name": "Runoob", "Age": 7, "Class": "First"}
    copied = base.copy()
    fromkeys_result = dict.fromkeys(["Name", "Age"], None)
    get_result = base.get("School", "默认学校")
    contains_name = "Name" in base
    items_result = list(base.items())
    keys_result = list(base.keys())
    setdefault_target = {"Name": "Runoob"}
    setdefault_result = setdefault_target.setdefault("Age", 7)
    update_target = {"Name": "Runoob"}
    update_target.update({"Age": 7})
    values_result = list(base.values())
    pop_target = base.copy()
    pop_result = pop_target.pop("Age")
    popitem_target = base.copy()
    popitem_result = popitem_target.popitem()
    clear_target = base.copy()
    clear_target.clear()

    show_table(
        ("方法", "描述", "示例结果"),
        [
            ("clear()", "删除字典内所有元素", str(clear_target)),
            ("copy()", "返回浅复制", str(copied)),
            ("fromkeys()", "按序列创建键", str(fromkeys_result)),
            ("get()", "获取值，不存在返回默认值", str(get_result)),
            ("key in dict", "判断键是否存在", str(contains_name)),
            ("items()", "返回键值对视图", str(items_result)),
            ("keys()", "返回键视图", str(keys_result)),
            ("setdefault()", "不存在则添加默认值", str(setdefault_result)),
            ("update()", "用另一个字典更新", str(update_target)),
            ("values()", "返回值视图", str(values_result)),
            ("pop()", "删除指定键并返回值", str(pop_result)),
            ("popitem()", "删除并返回最后一对键值", str(popitem_result)),
        ],
    )


def demo_counter_example() -> None:
    """复刻页面底部国家计数和混合键求和示例。"""
    country_counter: dict[str, int] = {}

    def addone(country: str) -> None:
        """给指定国家计数加一，不存在时先创建。"""
        if country in country_counter:
            country_counter[country] += 1
        else:
            country_counter[country] = 1

    addone("China")
    addone("Japan")
    addone("china")
    print(len(country_counter))
    print(country_counter)

    confusion: dict[object, int] = {}
    confusion[1] = 1
    confusion["1"] = 2
    confusion[1] += 1

    total = 0
    for key in confusion:
        total += confusion[key]
    print(total)
    print(confusion)


def demo_nested_and_reverse_examples() -> None:
    """保留笔记中常见的嵌套字典遍历和键值反转示例。"""
    cities = {
        "北京": {
            "朝阳": ["国贸", "CBD", "天阶"],
            "海淀": ["圆明园", "苏州街", "中关村", "北京大学"],
        },
        "河北": {
            "石家庄": ["石家庄A", "石家庄B"],
            "张家口": ["张家口A", "张家口B"],
        },
    }
    print("北京下的区域:")
    for area in cities["北京"]:
        print(area)
    print("北京海淀下的地点:")
    for place in cities["北京"]["海淀"]:
        print(place)

    data = {"a": 1, "b": 2, "c": 3}
    reverse = {value: key for key, value in data.items()}
    print(data)
    print(reverse)


def main() -> None:
    """按字典页面顺序运行全部示例。"""
    print("Python3 字典")

    show_section("1. 创建字典")
    demo_create_dictionary()

    show_section("2. 创建空字典")
    demo_empty_dictionary()

    show_section("3. 访问字典里的值")
    demo_access_dictionary()

    show_section("4. 修改字典")
    demo_update_dictionary()

    show_section("5. 删除字典元素")
    demo_delete_dictionary_items()

    show_section("6. 字典键的特性")
    demo_key_features()

    show_section("7. 字典内置函数")
    demo_builtin_functions()

    show_section("8. 字典内置方法")
    demo_dictionary_methods()

    show_section("9. 计数示例")
    demo_counter_example()

    show_section("10. 嵌套与反转示例")
    demo_nested_and_reverse_examples()


if __name__ == "__main__":
    main()
