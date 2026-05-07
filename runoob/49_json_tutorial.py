"""49 Python3 JSON

来源: https://www.runoob.com/python3/python3-json.html
可单独运行: python 49_json_tutorial.py
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 Python 与 JSON 类型转换表。"""
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


def demo_type_tables() -> None:
    """保留 Python 编码为 JSON 与 JSON 解码为 Python 的类型转换表。"""
    show_table(
        ("Python", "JSON"),
        [
            ("dict", "object"),
            ("list, tuple", "array"),
            ("str", "string"),
            ("int, float", "number"),
            ("True", "true"),
            ("False", "false"),
            ("None", "null"),
        ],
    )
    show_table(
        ("JSON", "Python"),
        [
            ("object", "dict"),
            ("array", "list"),
            ("string", "str"),
            ("number(int)", "int"),
            ("number(real)", "float"),
            ("true", "True"),
            ("false", "False"),
            ("null", "None"),
        ],
    )


def demo_dumps_loads() -> None:
    """执行 json.dumps 和 json.loads 编解码示例。"""
    data = {"no": 1, "name": "Runoob", "url": "https://www.runoob.com"}
    json_str = json.dumps(data)
    print("Python 原始数据：", repr(data))
    print("JSON 对象：", json_str)
    decoded = json.loads(json_str)
    print("Python 解码数据：", decoded)
    print(decoded["name"])
    print(decoded["url"])


def demo_dump_load_file() -> None:
    """执行 json.dump 和 json.load 文件读写示例。"""
    data = {"name": "Runoob", "alexa": 10000, "site": "www.runoob.com"}
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "data.json"
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
        with open(path, "r", encoding="utf-8") as file:
            print(json.load(file))


def demo_formatting_options() -> None:
    """演示 ensure_ascii、indent、sort_keys 等 dumps 参数。"""
    data = {"中文": "菜鸟教程", "number": 3, "items": [1, 2, 3]}
    print(json.dumps(data))
    print(json.dumps(data, ensure_ascii=False))
    print(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))


def demo_custom_object() -> None:
    """演示不可直接序列化对象时可先转换为字典。"""

    class Student:
        """自定义对象示例。"""

        def __init__(self, name: str, age: int) -> None:
            """初始化姓名和年龄。"""
            self.name = name
            self.age = age

    student = Student("Alice", 18)
    print(json.dumps(student.__dict__, ensure_ascii=False))


def main() -> None:
    """按 JSON 页面顺序运行全部示例。"""
    print("Python3 JSON")
    show_section("1. 类型转换表")
    demo_type_tables()
    show_section("2. dumps 与 loads")
    demo_dumps_loads()
    show_section("3. dump 与 load")
    demo_dump_load_file()
    show_section("4. 格式化选项")
    demo_formatting_options()
    show_section("5. 自定义对象")
    demo_custom_object()


if __name__ == "__main__":
    main()
