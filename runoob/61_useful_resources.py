"""61 Python 有用的资源

来源: https://www.runoob.com/python3/python3-resources.html
可单独运行: python 61_useful_resources.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留资源清单。"""
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


def demo_related_websites() -> None:
    """保留页面中的相关网站资源。"""
    show_table(
        ("资源", "说明"),
        [
            ("Python 3.6.3 中文手册", "Python 3 中文参考资料"),
            ("Python3 最新文档", "官方最新 Python3 文档"),
            ("Python 2.X 版本的教程", "旧版本 Python 教程"),
            ("Python 算法学习", "算法相关学习资料"),
        ],
    )


def demo_related_books() -> None:
    """保留页面中的相关书籍资源。"""
    books = [
        "父与子的编程之旅",
        "Python 学习手册",
        "Python编程 从入门到实践",
        "利用Python进行数据分析",
        "流畅的Python",
        "更多书籍",
    ]
    for index, book in enumerate(books, 1):
        print(f"{index}. {book}")


def main() -> None:
    """按有用资源页面顺序运行全部示例。"""
    print("Python 有用的资源")
    show_section("1. 相关网站")
    demo_related_websites()
    show_section("2. 相关书籍")
    demo_related_books()


if __name__ == "__main__":
    main()
