"""70 Python Markdown

来源: https://www.runoob.com/python3/python-markdown.html
可单独运行: python 70_markdown_tutorial.py
"""

from __future__ import annotations

import re
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 Markdown 库安装和用法。"""
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


def simple_markdown_to_html(text: str) -> str:
    """实现一个最小 Markdown 转 HTML 示例，避免依赖外部 markdown 包。"""
    lines = []
    in_list = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("# "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("- "):
            if not in_list:
                lines.append("<ul>")
                in_list = True
            lines.append(f"<li>{line[2:]}</li>")
        elif line:
            if in_list:
                lines.append("</ul>")
                in_list = False
            line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
            line = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', line)
            lines.append(f"<p>{line}</p>")
    if in_list:
        lines.append("</ul>")
    return "\n".join(lines)


def demo_install_and_usage() -> None:
    """保留 Python-Markdown 安装和基本调用方式。"""
    show_table(
        ("主题", "示例"),
        [
            ("安装", "pip install markdown"),
            ("导入", "import markdown"),
            ("字符串转换", "markdown.markdown(markdown_text)"),
            ("扩展", "markdown.markdown(text, extensions=['tables'])"),
            ("文件转换", "读取 .md 后写入 .html"),
        ],
    )


def demo_basic_conversion() -> None:
    """执行 Markdown 字符串到 HTML 的转换示例。"""
    md_text = """# Python Markdown
这是一个 **Markdown** 示例。
- 列表项一
- 列表项二
[菜鸟教程](https://www.runoob.com)
"""
    html = simple_markdown_to_html(md_text)
    print(html)


def demo_file_conversion() -> None:
    """演示读取 Markdown 文件并生成 HTML 文件。"""
    with tempfile.TemporaryDirectory() as directory:
        md_path = Path(directory) / "example.md"
        html_path = Path(directory) / "example.html"
        md_path.write_text("# 标题\n\n这是正文。", encoding="utf-8")
        html_path.write_text(simple_markdown_to_html(md_path.read_text(encoding="utf-8")), encoding="utf-8")
        print(html_path.read_text(encoding="utf-8"))


def demo_extensions_note() -> None:
    """保留常用扩展说明。"""
    show_table(
        ("扩展", "作用"),
        [
            ("extra", "启用一组常用扩展"),
            ("tables", "支持表格语法"),
            ("toc", "生成目录"),
            ("fenced_code", "支持围栏代码块"),
            ("codehilite", "代码高亮"),
        ],
    )


def main() -> None:
    """按 Markdown 页面顺序运行全部示例。"""
    print("Python Markdown")
    show_section("1. 安装和使用")
    demo_install_and_usage()
    show_section("2. 字符串转换")
    demo_basic_conversion()
    show_section("3. 文件转换")
    demo_file_conversion()
    show_section("4. 扩展")
    demo_extensions_note()


if __name__ == "__main__":
    main()
