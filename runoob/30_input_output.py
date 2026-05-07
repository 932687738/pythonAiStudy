"""30 Python3 输入和输出

来源: https://www.runoob.com/python3/python3-inputoutput.html
可单独运行: python 30_input_output.py
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


def demo_str_repr() -> None:
    """演示 str() 和 repr() 的区别，以及 repr() 对特殊字符的转义。"""
    s = "Hello, Runoob"
    print(str(s))
    print(repr(s))
    print(str(1 / 7))
    x = 10 * 3.25
    y = 200 * 200
    text = "x 的值为： " + repr(x) + ",  y 的值为：" + repr(y) + "..."
    print(text)
    hello = "hello, runoob\n"
    hellos = repr(hello)
    print(hellos)
    print(repr((x, y, ("Google", "Runoob"))))


def demo_rjust_and_format_table() -> None:
    """复刻平方与立方表的两种输出方式：rjust 和 str.format。"""
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
        print(repr(x * x * x).rjust(4))

    print("format 方式:")
    for x in range(1, 11):
        print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))


def demo_string_format() -> None:
    """演示 str.format() 的位置参数、关键字参数和格式控制。"""
    print("{}网址： \"{}!\"".format("菜鸟教程", "www.runoob.com"))
    print("{0} 和 {1}".format("Google", "Runoob"))
    print("{1} 和 {0}".format("Google", "Runoob"))
    print("{name}网址： {site}".format(name="菜鸟教程", site="www.runoob.com"))
    print("常量 PI 的值近似为： {!r}。".format(3.141592653589793))
    print("常量 PI 的值近似为 {0:.3f}。".format(3.141592653589793))


def demo_input_simulation() -> None:
    """说明 input() 会等待用户输入，并用固定值模拟以保证脚本可直接运行。"""
    simulated = "Runoob"
    print("你输入的内容是: ", simulated)


def demo_file_write_read() -> None:
    """复刻文件 write/read/readline/readlines 的核心示例，使用临时目录避免污染项目。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "foo.txt"
        file = open(path, "w", encoding="utf-8")
        file.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
        file.close()

        file = open(path, "r", encoding="utf-8")
        print(file.read())
        file.close()

        file = open(path, "r", encoding="utf-8")
        print(file.readline().strip())
        print(file.readline().strip())
        file.close()

        file = open(path, "r", encoding="utf-8")
        print(file.readlines())
        file.close()


def demo_file_iteration() -> None:
    """演示直接迭代文件对象逐行读取。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "foo.txt"
        path.write_text("第一行\n第二行\n第三行\n", encoding="utf-8")
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())


def demo_write_non_string() -> None:
    """演示写入非字符串对象前需要先用 str() 转换。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "foo1.txt"
        value = ("www.runoob.com", 14)
        text = str(value)
        with open(path, "w", encoding="utf-8") as file:
            print(file.write(text))
        print(path.read_text(encoding="utf-8"))


def demo_tell_seek() -> None:
    """演示 tell() 获取文件指针位置，seek() 移动文件指针。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "foo.txt"
        path.write_text("0123456789abcdef", encoding="utf-8")
        with open(path, "rb") as file:
            print(file.read(5))
            print(file.tell())
            file.seek(0)
            print(file.read(5))
            file.seek(5, 0)
            print(file.read(3))


def demo_json_serializing() -> None:
    """保留 JSON 序列化示例：dumps、dump、loads、load。"""
    data = {"name": "Runoob", "site": "www.runoob.com", "number": 3}
    text = json.dumps(data, ensure_ascii=False)
    print(text)
    print(json.loads(text))

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "data.json"
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
        with open(path, "r", encoding="utf-8") as file:
            print(json.load(file))


def main() -> None:
    """按输入和输出页面顺序运行全部示例。"""
    print("Python3 输入和输出")

    show_section("1. str() 与 repr()")
    demo_str_repr()

    show_section("2. 输出平方和立方表")
    demo_rjust_and_format_table()

    show_section("3. str.format()")
    demo_string_format()

    show_section("4. input() 模拟")
    demo_input_simulation()

    show_section("5. 文件读写")
    demo_file_write_read()

    show_section("6. 迭代文件对象")
    demo_file_iteration()

    show_section("7. 写入非字符串对象")
    demo_write_non_string()

    show_section("8. tell() 与 seek()")
    demo_tell_seek()

    show_section("9. JSON 保存结构化数据")
    demo_json_serializing()


if __name__ == "__main__":
    main()
