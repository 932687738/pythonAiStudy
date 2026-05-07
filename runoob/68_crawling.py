"""68 Python 爬虫

来源: https://www.runoob.com/python3/python-spider.html
可单独运行: python 68_crawling.py
"""

from __future__ import annotations

import re
import tempfile
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留爬虫流程和库说明。"""
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
class Link:
    """保存从 HTML 中提取到的链接文本和 URL。"""

    text: str
    href: str


class LinkParser(HTMLParser):
    """使用标准库 HTMLParser 提取 a 标签链接。"""

    def __init__(self) -> None:
        """初始化链接列表和当前 a 标签。"""
        super().__init__()
        self.links: list[Link] = []
        self.current_href: str | None = None
        self.current_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """遇到 a 标签时记录 href 属性。"""
        if tag == "a":
            attr_dict = dict(attrs)
            self.current_href = attr_dict.get("href")
            self.current_text = []

    def handle_data(self, data: str) -> None:
        """收集 a 标签内文本。"""
        if self.current_href is not None:
            self.current_text.append(data.strip())

    def handle_endtag(self, tag: str) -> None:
        """a 标签结束时保存链接。"""
        if tag == "a" and self.current_href is not None:
            self.links.append(Link("".join(self.current_text), self.current_href))
            self.current_href = None


def demo_crawler_flow() -> None:
    """保留爬虫的一般流程和常用库说明。"""
    show_table(
        ("步骤", "说明"),
        [
            ("发送请求", "使用 urllib 或 requests 获取网页"),
            ("解析页面", "使用 re、HTMLParser、BeautifulSoup、lxml 等提取数据"),
            ("保存数据", "写入 CSV、JSON、数据库或文件"),
            ("遵守规则", "查看 robots.txt，控制请求频率"),
            ("反爬处理", "合理设置 User-Agent、延迟和重试"),
        ],
    )


def demo_urllib_request() -> None:
    """复刻 urllib 请求逻辑，用 data URL 避免真实联网。"""
    url = "data:text/html;charset=utf-8,%3Chtml%3E%3Ctitle%3ERunoob%3C/title%3E%3C/html%3E"
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    print(html)


def demo_url_parse_and_encode() -> None:
    """演示爬虫中常见的 URL 编码、解码、拼接和解析。"""
    query = urllib.parse.urlencode({"s": "Python 爬虫"})
    url = "https://www.runoob.com/?" + query
    parsed = urllib.parse.urlparse(url)
    print(url)
    print(parsed)
    print(urllib.parse.parse_qs(parsed.query))
    print(urllib.parse.urljoin("https://www.runoob.com/python3/", "../html/html-tutorial.html"))


def demo_extract_links() -> None:
    """执行 HTML 链接提取示例。"""
    html = """
<html><body>
<a href="/python3/">Python3 教程</a>
<a href="/html/">HTML 教程</a>
</body></html>
"""
    parser = LinkParser()
    parser.feed(html)
    for link in parser.links:
        print(link)


def demo_regex_extract() -> None:
    """使用正则表达式提取标题和图片 URL。"""
    html = '<html><title>菜鸟教程</title><img src="logo.png"><img src="python.png"></html>'
    title = re.findall(r"<title>(.*?)</title>", html)
    images = re.findall(r'<img\s+src="(.*?)"', html)
    print(title)
    print(images)


def demo_save_results() -> None:
    """演示把爬取结果保存到本地文件。"""
    rows = ["title,url", "Python3 教程,https://www.runoob.com/python3/"]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "result.csv"
        path.write_text("\n".join(rows), encoding="utf-8")
        print(path.read_text(encoding="utf-8"))


def main() -> None:
    """按爬虫页面顺序运行全部示例。"""
    print("Python 爬虫")
    show_section("1. 爬虫流程")
    demo_crawler_flow()
    show_section("2. urllib 请求")
    demo_urllib_request()
    show_section("3. URL 处理")
    demo_url_parse_and_encode()
    show_section("4. HTML 链接提取")
    demo_extract_links()
    show_section("5. 正则提取")
    demo_regex_extract()
    show_section("6. 保存结果")
    demo_save_results()


if __name__ == "__main__":
    main()
