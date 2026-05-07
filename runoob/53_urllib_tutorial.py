"""53 Python3 urllib

来源: https://www.runoob.com/python3/python-urllib.html
可单独运行: python 53_urllib_tutorial.py
"""

from __future__ import annotations

import tempfile
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 urllib 包模块和 urlopen 参数。"""
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


def demo_modules_table() -> None:
    """保留 urllib 包四个子模块说明。"""
    show_table(
        ("模块", "说明"),
        [
            ("urllib.request", "打开和读取 URL"),
            ("urllib.error", "包含 request 抛出的异常"),
            ("urllib.parse", "解析 URL"),
            ("urllib.robotparser", "解析 robots.txt 文件"),
        ],
    )


def demo_request_get_like() -> None:
    """复刻 GET 搜索示例，构造 URL、Request 和请求头；用 data URL 避免真实联网。"""
    base_url = "https://www.runoob.com/?s="
    keyword = "Python 教程"
    key_code = urllib.request.quote(keyword)
    url_all = base_url + key_code
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 Chrome/58 Safari/537.36"
    }
    request = urllib.request.Request(url_all, headers=header)
    print(request.full_url)
    print(request.headers)

    local_request = urllib.request.Request("data:text/html;charset=utf-8,%3Ch1%3ERunoob%3C/h1%3E")
    response = urllib.request.urlopen(local_request).read()
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "urllib_test_runoob_search.html"
        path.write_bytes(response)
        print(path.read_text(encoding="utf-8"))


def demo_post_like() -> None:
    """复刻 POST 表单提交示例，保留 urlencode 和 Request(data, headers) 逻辑。"""
    url = "https://www.runoob.com/try/py3/py3_urllib_test.php"
    data = {"name": "RUNOOB", "tag": "菜鸟教程"}
    header = {"User-Agent": "Mozilla/5.0"}
    encoded = urllib.parse.urlencode(data).encode("utf8")
    request = urllib.request.Request(url, encoded, header)
    print(request.full_url)
    print(request.data)
    print(urllib.parse.parse_qs(request.data.decode("utf8")))


def demo_parse_functions() -> None:
    """演示 urlparse、urlencode、quote、unquote、parse_qs 等解析函数。"""
    url = "https://www.runoob.com/python3/?s=Python%E6%95%99%E7%A8%8B#top"
    parsed = urllib.parse.urlparse(url)
    print(parsed)
    print(urllib.parse.parse_qs(parsed.query))
    print(urllib.parse.quote("Python 教程"))
    print(urllib.parse.unquote("Python%20%E6%95%99%E7%A8%8B"))
    print(urllib.parse.urlencode({"name": "RUNOOB", "tag": "菜鸟教程"}))


def demo_error_handling() -> None:
    """保留 urllib.error 异常处理结构，构造 URLError 示例。"""
    try:
        raise urllib.error.URLError("模拟网络错误")
    except urllib.error.URLError as error:
        print("URLError:", error.reason)


def demo_robot_parser() -> None:
    """演示 robotparser 解析 robots.txt 内容。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "robots.txt"
        path.write_text("User-agent: *\nDisallow: /private\nAllow: /\n", encoding="utf-8")
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(path.as_uri())
        parser.read()
        print(parser.can_fetch("*", "https://example.com/"))
        print(parser.can_fetch("*", "https://example.com/private/page"))


def main() -> None:
    """按 urllib 页面顺序运行全部示例。"""
    print("Python3 urllib")
    show_section("1. urllib 模块")
    demo_modules_table()
    show_section("2. urllib.request GET 示例")
    demo_request_get_like()
    show_section("3. urllib.request POST 示例")
    demo_post_like()
    show_section("4. urllib.parse")
    demo_parse_functions()
    show_section("5. urllib.error")
    demo_error_handling()
    show_section("6. urllib.robotparser")
    demo_robot_parser()


if __name__ == "__main__":
    main()
