"""75 Python StringIO 模块

来源: https://www.runoob.com/python3/python-stringio.html
可单独运行: python 75_stringio_module.py
"""

from __future__ import annotations

import unittest
from io import StringIO


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 StringIO 方法表。"""
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


def demo_basic_usage() -> None:
    """执行创建、写入、getvalue、seek、readline 和 close 示例。"""
    string_io = StringIO()
    string_io.write("Hello, World!\n")
    string_io.write("This is a test.")
    print(string_io.getvalue())
    string_io.seek(0)
    print(string_io.readline().strip())
    print(string_io.read())
    string_io.close()
    print(string_io.closed)


def demo_simulate_file() -> None:
    """复刻模拟文件操作示例。"""
    string_io = StringIO()
    string_io.write("Python is awesome!\n")
    string_io.write("StringIO is useful!")
    string_io.seek(0)
    print(string_io.read())
    string_io.close()


def process_input(input_data: str) -> str:
    """将输入内容转为大写，用于单元测试示例。"""
    return input_data.upper()


class TestProcessInput(unittest.TestCase):
    """页面中的 StringIO 单元测试示例。"""

    def test_process_input(self) -> None:
        """使用 StringIO 模拟输入流并断言输出。"""
        input_data = "hello"
        expected_output = "HELLO"
        input_stream = StringIO(input_data)
        result = process_input(input_stream.read())
        self.assertEqual(result, expected_output)


def demo_unittest_usage() -> None:
    """运行 unittest 测试套件并输出结果。"""
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestProcessInput)
    result = unittest.TextTestRunner(stream=StringIO(), verbosity=0).run(suite)
    print("testsRun:", result.testsRun)
    print("wasSuccessful:", result.wasSuccessful())


def demo_methods_table() -> None:
    """保留 StringIO 常用属性和方法表。"""
    show_table(
        ("属性/方法", "描述"),
        [
            ("StringIO()", "创建 StringIO 对象"),
            ("write(s)", "写入字符串"),
            ("read([size])", "读取内容"),
            ("readline([size])", "读取一行"),
            ("readlines([sizehint])", "读取所有行"),
            ("getvalue()", "返回全部内容"),
            ("seek(offset[, whence])", "移动文件指针"),
            ("tell()", "返回当前指针位置"),
            ("truncate([size])", "截断内容"),
            ("close()", "关闭对象"),
            ("closed", "是否已关闭"),
        ],
    )


def demo_tell_truncate() -> None:
    """演示 tell 和 truncate。"""
    stream = StringIO("abcdef")
    stream.seek(3)
    print(stream.tell())
    stream.truncate(4)
    print(stream.getvalue())
    stream.close()


def main() -> None:
    """按 StringIO 页面顺序运行全部示例。"""
    print("Python StringIO 模块")
    show_section("1. 基本使用")
    demo_basic_usage()
    show_section("2. 模拟文件操作")
    demo_simulate_file()
    show_section("3. 单元测试")
    demo_unittest_usage()
    show_section("4. 方法表")
    demo_methods_table()
    show_section("5. tell 和 truncate")
    demo_tell_truncate()


if __name__ == "__main__":
    main()
