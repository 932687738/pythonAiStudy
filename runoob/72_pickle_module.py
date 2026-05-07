"""72 Python Pickle 模块

来源: https://www.runoob.com/python3/pyhton-pikle.html
可单独运行: python 72_pickle_module.py
"""

from __future__ import annotations

import pickle
import tempfile
from dataclasses import dataclass
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 pickle 方法和注意事项。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        """格式化一行表格。"""
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


@dataclass
class User:
    """用于演示自定义类实例序列化。"""

    name: str
    age: int


def demo_pickle_intro() -> None:
    """保留序列化和反序列化的概念说明。"""
    show_table(
        ("概念", "说明"),
        [
            ("Pickling", "将 Python 对象转换为字节序列"),
            ("Unpickling", "将字节序列恢复为 Python 对象"),
            ("dump/load", "写入或读取文件"),
            ("dumps/loads", "转换为或读取字节串"),
            ("注意", "不要反序列化不可信来源的数据"),
        ],
    )


def demo_dump_load_file() -> None:
    """执行 pickle.dump 和 pickle.load 文件序列化示例。"""
    data = {"name": "Alice", "age": 25, "hobbies": ["reading", "traveling"]}
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "data.pkl"
        with open(path, "wb") as file:
            pickle.dump(data, file)
        with open(path, "rb") as file:
            loaded_data = pickle.load(file)
        print(loaded_data)


def demo_dumps_loads() -> None:
    """执行 pickle.dumps 和 pickle.loads 字节串示例。"""
    data = [1, 2, 3, 4, 5]
    byte_data = pickle.dumps(data)
    print(byte_data[:20])
    original_data = pickle.loads(byte_data)
    print(original_data)


def demo_supported_types() -> None:
    """演示基本类型、集合类型和自定义类实例都可以被 pickle。"""
    values = {
        "number": 1,
        "float": 3.14,
        "text": "Runoob",
        "list": [1, 2],
        "tuple": (1, 2),
        "dict": {"a": 1},
        "set": {1, 2},
        "object": User("Bob", 18),
    }
    restored = pickle.loads(pickle.dumps(values))
    print(restored)


def demo_protocols() -> None:
    """保留 pickle 协议版本说明，并展示最高协议。"""
    print("pickle.HIGHEST_PROTOCOL:", pickle.HIGHEST_PROTOCOL)
    data = {"site": "runoob"}
    for protocol in [0, pickle.HIGHEST_PROTOCOL]:
        payload = pickle.dumps(data, protocol=protocol)
        print(protocol, payload[:30], pickle.loads(payload))


def main() -> None:
    """按 Pickle 页面顺序运行全部示例。"""
    print("Python Pickle 模块")
    show_section("1. 概念")
    demo_pickle_intro()
    show_section("2. dump/load")
    demo_dump_load_file()
    show_section("3. dumps/loads")
    demo_dumps_loads()
    show_section("4. 可序列化对象")
    demo_supported_types()
    show_section("5. 协议版本")
    demo_protocols()


if __name__ == "__main__":
    main()
