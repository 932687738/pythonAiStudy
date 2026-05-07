"""79 Python csv 模块

来源: https://www.runoob.com/python3/python-csv.html
可单独运行: python 79_csv_module.py
"""

from __future__ import annotations

import csv
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 csv 对象特性和常用参数。"""
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


def demo_reader_writer() -> None:
    """执行 csv.reader 读取和 csv.writer 写入示例。"""
    data = [["Name", "Age", "City"], ["Alice", "30", "New York"], ["Bob", "25", "Los Angeles"]]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "data.csv"
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


def demo_writerows() -> None:
    """执行 writer.writerows 一次写入多行数据。"""
    rows = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "output.csv"
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(path.read_text(encoding="utf-8"))


def demo_dict_reader_writer() -> None:
    """执行 DictReader 和 DictWriter 示例，通过字段名读写 CSV。"""
    data = [
        {"Name": "Alice", "Age": "30", "City": "New York"},
        {"Name": "Bob", "Age": "25", "City": "Los Angeles"},
    ]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "people.csv"
        fieldnames = ["Name", "Age", "City"]
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print(reader.fieldnames)
            for row in reader:
                print(row["Name"], row["Age"], row["City"])


def demo_custom_dialect() -> None:
    """执行自定义 TSV 方言示例。"""
    csv.register_dialect("runoob_tsv", delimiter="\t", quoting=csv.QUOTE_NONE)
    try:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.tsv"
            path.write_text("Name\tAge\nAlice\t25\nBob\t30\n", encoding="utf-8")
            with open(path, "r", encoding="utf-8") as file:
                reader = csv.reader(file, dialect="runoob_tsv")
                for row in reader:
                    print(row)
    finally:
        csv.unregister_dialect("runoob_tsv")


def demo_parameters_table() -> None:
    """保留 csv 常用参数说明。"""
    show_table(
        ("参数", "说明", "示例值", "适用方法"),
        [
            ("delimiter", "字段分隔符", "',' 或 '\\t'", "reader/writer"),
            ("quotechar", "引用字符", "'\"'", "reader/writer"),
            ("quoting", "引用规则", "csv.QUOTE_ALL", "reader/writer"),
            ("skipinitialspace", "忽略分隔符后的空格", "True/False", "reader"),
            ("lineterminator", "行结束符", "'\\r\\n'", "writer"),
            ("dialect", "预定义方言名称", "'excel'", "所有方法"),
        ],
    )


def main() -> None:
    """按 csv 页面顺序运行全部示例。"""
    print("Python csv 模块")
    show_section("1. reader 和 writer")
    demo_reader_writer()
    show_section("2. writerows")
    demo_writerows()
    show_section("3. DictReader 和 DictWriter")
    demo_dict_reader_writer()
    show_section("4. 自定义方言")
    demo_custom_dialect()
    show_section("5. 常用参数")
    demo_parameters_table()


if __name__ == "__main__":
    main()
