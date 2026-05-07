"""48 Python3 XML 解析

来源: https://www.runoob.com/python3/python3-xml-processing.html
可单独运行: python 48_xml_parsing.py
"""

from __future__ import annotations

import tempfile
import xml.dom.minidom
import xml.etree.ElementTree as ET
import xml.sax
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 XML 解析方式对比。"""
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


def demo_xml_intro() -> None:
    """保留 XML 与 Python 解析接口说明。"""
    show_table(
        ("方式", "特点", "适用场景"),
        [
            ("ElementTree", "标准库，简单高效", "常规 XML 读写"),
            ("SAX", "事件驱动，边读边处理", "大文件流式解析"),
            ("DOM", "把 XML 读成完整树", "需要随机访问节点"),
        ],
    )


def create_books_xml(path: Path) -> None:
    """创建页面中的 bookstore XML 文档并写入文件。"""
    root = ET.Element("bookstore")
    for title, author, price in [
        ("Introduction to Python", "John Doe", "29.99"),
        ("Data Science with Python", "Jane Smith", "39.95"),
    ]:
        book = ET.SubElement(root, "book")
        ET.SubElement(book, "title").text = title
        ET.SubElement(book, "author").text = author
        ET.SubElement(book, "price").text = price
    tree = ET.ElementTree(root)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def demo_element_tree() -> None:
    """复刻 ElementTree 创建、保存、解析和遍历 XML 的示例。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "books.xml"
        create_books_xml(path)
        parsed_tree = ET.parse(path)
        parsed_root = parsed_tree.getroot()
        for book in parsed_root.findall("book"):
            title = book.find("title").text if book.find("title") is not None else ""
            author = book.find("author").text if book.find("author") is not None else ""
            price = book.find("price").text if book.find("price") is not None else ""
            print(f"Title: {title}, Author: {author}, Price: {price}")


class BookHandler(xml.sax.ContentHandler):
    """SAX 解析器处理器，记录当前标签并输出书籍信息。"""

    def __init__(self) -> None:
        """初始化当前标签和字段值。"""
        super().__init__()
        self.current_data = ""
        self.title = ""
        self.author = ""
        self.price = ""

    def startElement(self, tag: str, attributes) -> None:
        """开始元素时记录当前标签。"""
        self.current_data = tag

    def endElement(self, tag: str) -> None:
        """结束 book 元素时输出当前书籍信息。"""
        if tag == "book":
            print(f"SAX Book: {self.title}, {self.author}, {self.price}")
            self.title = self.author = self.price = ""
        self.current_data = ""

    def characters(self, content: str) -> None:
        """读取文本内容并按当前标签保存。"""
        text = content.strip()
        if not text:
            return
        if self.current_data == "title":
            self.title += text
        elif self.current_data == "author":
            self.author += text
        elif self.current_data == "price":
            self.price += text


def demo_sax() -> None:
    """演示 SAX 事件驱动解析 XML。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "books.xml"
        create_books_xml(path)
        parser = xml.sax.make_parser()
        handler = BookHandler()
        parser.setContentHandler(handler)
        parser.parse(str(path))


def demo_dom() -> None:
    """演示 DOM 解析 XML 并通过节点访问数据。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "books.xml"
        create_books_xml(path)
        dom_tree = xml.dom.minidom.parse(str(path))
        collection = dom_tree.documentElement
        books = collection.getElementsByTagName("book")
        for book in books:
            title = book.getElementsByTagName("title")[0].childNodes[0].data
            author = book.getElementsByTagName("author")[0].childNodes[0].data
            price = book.getElementsByTagName("price")[0].childNodes[0].data
            print(f"DOM Book: {title}, {author}, {price}")


def main() -> None:
    """按 XML 解析页面顺序运行全部示例。"""
    print("Python3 XML 解析")
    show_section("1. XML 解析方式")
    demo_xml_intro()
    show_section("2. ElementTree")
    demo_element_tree()
    show_section("3. SAX")
    demo_sax()
    show_section("4. DOM")
    demo_dom()


if __name__ == "__main__":
    main()
