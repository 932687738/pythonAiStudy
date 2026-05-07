"""10 Python3 注释

来源: https://www.runoob.com/python3/python3-comment.html
可单独运行: python 10_comments.py
"""

from __future__ import annotations

import inspect
import pydoc


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def demo_single_line_comment() -> None:
    """演示单行注释：# 后面的内容不会被解释器执行。"""
    # 这是一个注释
    print("Hello, World!")
    # 这也是注释


def demo_triple_single_quotes() -> None:
    """演示三个单引号形式的多行注释写法。"""
    '''
    这是多行注释，用三个单引号
    这是多行注释，用三个单引号
    这是多行注释，用三个单引号
    '''
    print("Hello, World!")


def demo_triple_double_quotes() -> None:
    """演示三个双引号形式的多行注释写法。"""
    """
    这是多行注释，用三个双引号
    这是多行注释，用三个双引号
    这是多行注释，用三个双引号
    """
    print("Hello, World!")


def demo_multiline_comment_note() -> None:
    """说明多行字符串作为注释使用时并不是真正的注释，也不能嵌套。"""
    print("多行字符串不赋值、不使用时，通常不会影响程序运行。")
    print("但三引号不能随意嵌套，嵌套错误会导致语法结构被破坏。")

    correct_example = '''
这是外部的多行说明
可以包含一些描述性的内容

# 这是内部的单行注释
# 可以嵌套在多行说明中
'''
    print("正确示例内容:")
    print(correct_example.strip())


def add(a: int, b: int) -> int:
    """返回两数之和"""
    return a + b


def demo_docstring_basic() -> None:
    """演示函数 Docstring 可通过 __doc__ 属性访问。"""
    print(add.__doc__)
    print(f"add(2, 3) -> {add(2, 3)}")


def demo_help_docstring() -> None:
    """演示 help() 可以查看函数文档，这里用 pydoc.render_doc 避免进入交互分页。"""
    help_text = pydoc.render_doc(add, "Help on %s")
    lines = help_text.splitlines()
    for line in lines[:8]:
        print(line)


def demo_inspect_getdoc() -> None:
    """演示 inspect.getdoc() 可以提取并清理文档字符串。"""
    print(inspect.getdoc(add))


def calculate(a: int, b: int, operation: str = "add") -> int:
    """
    执行数学运算

    参数:
        a: 第一个数字
        b: 第二个数字
        operation: 操作类型，可选 "add", "subtract", "multiply"

    返回:
        计算结果
    """
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    raise ValueError("不支持的操作")


def demo_multiline_docstring() -> None:
    """演示复杂函数使用多行 Docstring 描述参数、返回值和行为。"""
    print(inspect.getdoc(calculate))
    print(f"calculate(6, 3, 'add') -> {calculate(6, 3, 'add')}")
    print(f"calculate(6, 3, 'subtract') -> {calculate(6, 3, 'subtract')}")
    print(f"calculate(6, 3, 'multiply') -> {calculate(6, 3, 'multiply')}")


class Person:
    """人物类，用于表示一个人的基本信息"""

    def __init__(self, name: str, age: int) -> None:
        """
        初始化人物对象

        参数:
            name: 姓名
            age: 年龄
        """
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """介绍这个人"""
        return f"我叫{self.name}，今年{self.age}岁"


def demo_class_docstring() -> None:
    """演示类和方法也可以拥有 Docstring，并能通过 __doc__ 访问。"""
    person = Person("Runoob", 7)
    print(Person.__doc__)
    print(Person.introduce.__doc__)
    print(person.introduce())


def demo_docstring_position() -> None:
    """演示文档字符串必须放在函数第一条语句位置才会成为 __doc__。"""

    def good() -> None:
        """这是文档字符串"""
        value = 1
        print(value)

    def bad() -> None:
        value = 1
        """这只是普通字符串，不会成为函数文档"""
        print(value)

    print(f"good.__doc__ -> {good.__doc__!r}")
    print(f"bad.__doc__ -> {bad.__doc__!r}")


def demo_docstring_styles() -> None:
    """保留页面中的 Docstring 规范说明。"""
    styles = [
        "Google 风格：参数和返回值有明确标签。",
        "Sphinx/reST 风格：使用 :param name: 这类字段。",
        "NumPy 风格：适合科学计算项目中的较长说明。",
    ]
    for style in styles:
        print(style)


def main() -> None:
    """按注释页面顺序运行全部示例。"""
    print("Python3 注释")

    show_section("1. 单行注释")
    demo_single_line_comment()

    show_section("2. 三个单引号多行注释")
    demo_triple_single_quotes()

    show_section("3. 三个双引号多行注释")
    demo_triple_double_quotes()

    show_section("4. 多行注释注意事项")
    demo_multiline_comment_note()

    show_section("5. Docstring 基本语法")
    demo_docstring_basic()

    show_section("6. help() 查看文档")
    demo_help_docstring()

    show_section("7. inspect 提取文档")
    demo_inspect_getdoc()

    show_section("8. 多行 Docstring")
    demo_multiline_docstring()

    show_section("9. 类的 Docstring")
    demo_class_docstring()

    show_section("10. Docstring 位置")
    demo_docstring_position()

    show_section("11. Docstring 规范")
    demo_docstring_styles()


if __name__ == "__main__":
    main()
