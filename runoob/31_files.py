"""31 Python3 File

来源: https://www.runoob.com/python3/python3-file-methods.html
可单独运行: python 31_files.py
"""

from __future__ import annotations

import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的 open 模式表和 file 方法表。"""
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


def demo_open_modes_table() -> None:
    """保留 open() 方法的主要参数和文件打开模式说明。"""
    show_table(
        ("模式", "描述"),
        [
            ("t", "文本模式，默认"),
            ("b", "二进制模式"),
            ("r", "只读，文件指针在开头"),
            ("rb", "二进制只读"),
            ("r+", "读写，文件指针在开头"),
            ("w", "只写，存在则清空，不存在则创建"),
            ("wb", "二进制只写"),
            ("w+", "读写，存在则清空"),
            ("a", "追加写入，指针在文件末尾"),
            ("a+", "追加读写，不存在则创建"),
            ("x", "独占创建，文件已存在则报错"),
            ("+", "打开文件进行更新，可读可写"),
        ],
    )


def demo_file_methods_table() -> None:
    """保留 file 对象常用函数列表。"""
    show_table(
        ("方法", "描述"),
        [
            ("close()", "关闭文件，关闭后不能继续读写"),
            ("flush()", "刷新缓冲区"),
            ("fileno()", "返回底层文件描述符"),
            ("isatty()", "是否连接到终端设备"),
            ("read([size])", "读取指定大小内容"),
            ("readline([size])", "读取一行"),
            ("readlines()", "读取所有行并返回列表"),
            ("seek(offset[, whence])", "移动文件指针"),
            ("tell()", "返回当前位置"),
            ("truncate([size])", "截断文件"),
            ("write(str)", "写入字符串"),
            ("writelines(sequence)", "写入字符串序列"),
        ],
    )


def demo_close_and_write() -> None:
    """演示 open、write、close，并说明文件关闭后不能继续读写。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "runoob.txt"
        file = open(path, "w", encoding="utf-8")
        print("文件名为: ", file.name)
        print(file.write("www.runoob.com\n"))
        file.close()
        print("文件是否已关闭:", file.closed)
        try:
            file.write("again")
        except ValueError as exc:
            print(f"关闭后写入失败: {exc.__class__.__name__}: {exc}")


def demo_read_readline_readlines() -> None:
    """执行 read、readline、readlines 三类读取示例。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "runoob.txt"
        path.write_text(
            "1:www.runoob.com\n2:www.runoob.com\n3:www.runoob.com\n4:www.runoob.com\n5:www.runoob.com\n",
            encoding="utf-8",
        )
        with open(path, "r+", encoding="utf-8") as file:
            print("文件名为: ", file.name)
            print("读取的字符串: %s" % file.read(10))
            file.seek(0)
            print("读取第一行 %s" % file.readline().strip())
            print("读取的字符串为: %s" % file.readline(5))
            file.seek(0)
            print("所有行:", file.readlines())


def demo_tell_seek() -> None:
    """执行 tell 和 seek 示例，移动文件指针并读取指定位置。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "workfile"
        with open(path, "wb+") as file:
            print(file.write(b"0123456789abcdef"))
            print(file.seek(5))
            print(file.read(1))
            print(file.seek(-3, 2))
            print(file.read(1))
            print("当前位置:", file.tell())


def demo_flush_fileno_isatty() -> None:
    """演示 flush、fileno 和 isatty 方法。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "runoob.txt"
        with open(path, "w", encoding="utf-8") as file:
            print("文件名为: ", file.name)
            file.write("Runoob")
            file.flush()
            print("文件描述符为: ", file.fileno())
            print("是否连接到终端设备: ", file.isatty())


def demo_truncate_and_writelines() -> None:
    """演示 truncate 截断文件和 writelines 写入字符串序列。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "runoob.txt"
        with open(path, "w+", encoding="utf-8") as file:
            file.writelines(["1:www.runoob.com\n", "2:www.runoob.com\n", "3:www.runoob.com\n"])
            file.seek(0)
            print(file.read())
            file.truncate(16)
            file.seek(0)
            print("截断后:", file.read())


def demo_binary_write_note() -> None:
    """演示二进制模式写入时必须写 bytes，字符串需要 encode。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "binary.bin"
        with open(path, "wb") as file:
            try:
                file.write("abc")  # type: ignore[arg-type]
            except TypeError as exc:
                print(f"二进制写入 str 失败: {exc.__class__.__name__}: {exc}")
            file.write("abc".encode("utf-8"))
        print(path.read_bytes())


def main() -> None:
    """按 File 方法页面顺序运行全部示例。"""
    print("Python3 File")

    show_section("1. open 模式表")
    demo_open_modes_table()

    show_section("2. file 方法表")
    demo_file_methods_table()

    show_section("3. close 和 write")
    demo_close_and_write()

    show_section("4. read、readline、readlines")
    demo_read_readline_readlines()

    show_section("5. tell 和 seek")
    demo_tell_seek()

    show_section("6. flush、fileno、isatty")
    demo_flush_fileno_isatty()

    show_section("7. truncate 和 writelines")
    demo_truncate_and_writelines()

    show_section("8. 二进制写入")
    demo_binary_write_note()


if __name__ == "__main__":
    main()
