"""37 Python 类型注解

来源: https://www.runoob.com/python3/python-type-hints.html
可单独运行: python 37_type_annotations.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的类型注解说明。"""
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


def greet(first_name: str, last_name: str) -> str:
    """使用函数注解标明参数和返回值都是字符串。"""
    full_name = first_name + " " + last_name
    return "Hello, " + full_name


def add_numbers(a: int, b: int) -> int:
    """将两个整数相加并返回结果。"""
    return a + b


def say_hello(name: str, times: int = 1) -> str:
    """向某人问好指定次数，演示带默认值的类型注解。"""
    return " ".join([f"Hello, {name}!"] * times)


def demo_basic_annotations() -> None:
    """执行函数类型注解和默认值示例。"""
    print(greet("Ada", "Lovelace"))
    print(add_numbers(5, 3))
    print(say_hello("Bob"))
    print(say_hello("Alice", 3))
    print(greet.__annotations__)


def demo_container_annotations() -> None:
    """保留 typing 中的 List、Dict、Tuple、Set 容器类型示例。"""
    numbers: List[int] = [1, 2, 3, 4, 5]
    student_scores: Dict[str, int] = {"Alice": 95, "Bob": 88}
    person_info: Tuple[int, str, bool] = (25, "Alice", True)
    unique_names: Set[str] = {"Alice", "Bob", "Charlie"}
    print(numbers)
    print(student_scores)
    print(person_info)
    print(unique_names)


def find_student(name: str) -> Optional[str]:
    """根据名字查找学生，找不到时返回 None。"""
    students = {"Alice": "A001", "Bob": "B002"}
    return students.get(name)


def process_input(data: Union[str, int, List[int]]) -> None:
    """处理可能是字符串、整数或整数列表的输入。"""
    if isinstance(data, str):
        print(f"字符串: {data}")
    elif isinstance(data, int):
        print(f"整数: {data}")
    elif isinstance(data, list):
        print(f"列表: {data}")


def demo_optional_union() -> None:
    """执行 Optional 和 Union 示例。"""
    print(find_student("Alice"))
    print(find_student("Charlie"))
    process_input("hello")
    process_input(42)
    process_input([1, 2, 3])


def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """演示 Callable 类型：接收一个函数作为参数。"""
    return operation(x, y)


def demo_callable_any() -> None:
    """演示 Callable 和 Any 类型。"""
    print(apply_operation(3, 4, lambda a, b: a + b))
    unknown: Any = {"name": "Runoob", "score": 100}
    print(unknown)


@dataclass
class Student:
    """使用类型注解定义数据类字段。"""

    name: str
    age: int
    score: float


def demo_class_annotations() -> None:
    """演示类属性类型注解。"""
    student = Student("Alice", 18, 95.5)
    print(student)
    print(Student.__annotations__)


def demo_modern_builtin_generics() -> None:
    """补充 Python 3.9+ 可直接使用 list[int]、dict[str, int] 形式。"""
    numbers: list[int] = [1, 2, 3]
    scores: dict[str, int] = {"Bob": 88}
    maybe_name: str | None = None
    print(numbers)
    print(scores)
    print(maybe_name)


def demo_mypy_commands() -> None:
    """保留 Mypy 静态类型检查命令。"""
    commands = [
        "pip install mypy",
        "mypy example.py",
        "mypy --strict example.py",
    ]
    for command in commands:
        print(command)


def main() -> None:
    """按类型注解页面顺序运行全部示例。"""
    print("Python 类型注解")

    show_section("1. 基本函数注解")
    demo_basic_annotations()

    show_section("2. 容器类型注解")
    demo_container_annotations()

    show_section("3. Optional 和 Union")
    demo_optional_union()

    show_section("4. Callable 和 Any")
    demo_callable_any()

    show_section("5. 类注解")
    demo_class_annotations()

    show_section("6. 现代内置泛型")
    demo_modern_builtin_generics()

    show_section("7. Mypy 命令")
    demo_mypy_commands()


if __name__ == "__main__":
    main()
