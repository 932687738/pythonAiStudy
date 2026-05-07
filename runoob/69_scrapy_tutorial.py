"""69 Python Scrapy 库

来源: https://www.runoob.com/python3/python-scrapy.html
可单独运行: python 69_scrapy_tutorial.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urljoin


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 Scrapy 方法、设置和组件表。"""
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
class FakeResponse:
    """模拟 Scrapy Response，支持 css、follow、url、status、text。"""

    url: str
    text: str
    status: int = 200
    headers: dict[str, str] | None = None
    meta: dict[str, str] | None = None

    def css(self, selector: str) -> list[str]:
        """支持页面示例中用到的几个 CSS 选择器。"""
        if selector == "span.title::text":
            return re.findall(r'<span class="title">(.*?)</span>', self.text)
        if selector == "span.rating_num::text":
            return re.findall(r'<span class="rating_num">(.*?)</span>', self.text)
        if selector == "span.inq::text":
            return re.findall(r'<span class="inq">(.*?)</span>', self.text)
        if selector == "span.next a::attr(href)":
            return re.findall(r'<span class="next"><a href="(.*?)">', self.text)
        if selector == "title::text":
            return re.findall(r"<title>(.*?)</title>", self.text)
        if selector == "a::attr(href)":
            return re.findall(r'<a href="(.*?)"', self.text)
        return []

    def follow(self, link: str, callback) -> dict[str, object]:
        """模拟 response.follow 生成后续请求。"""
        return {"url": urljoin(self.url, link), "callback": callback.__name__}

    def json(self) -> dict[str, str]:
        """模拟 response.json 方法。"""
        return {"url": self.url, "status": str(self.status)}


def demo_scrapy_intro() -> None:
    """保留 Scrapy 介绍、安装和项目结构说明。"""
    show_table(
        ("组件", "作用"),
        [
            ("Spider", "定义如何抓取和解析网页"),
            ("Item", "定义和存储抓取数据"),
            ("Pipeline", "清洗、验证、保存数据"),
            ("Middleware", "处理请求和响应"),
            ("Settings", "配置并发、延迟、User-Agent 等"),
        ],
    )
    print("pip install scrapy")
    print("scrapy startproject myproject")
    print("scrapy genspider douban_spider movie.douban.com")


def demo_project_structure() -> None:
    """保留 Scrapy 项目目录结构。"""
    structure = [
        "myproject/",
        "    scrapy.cfg",
        "    myproject/",
        "        __init__.py",
        "        items.py",
        "        middlewares.py",
        "        pipelines.py",
        "        settings.py",
        "        spiders/",
        "            __init__.py",
        "            myspider.py",
    ]
    for line in structure:
        print(line)


class DoubanSpider:
    """模拟页面中的 DoubanSpider，保留 start_requests 和 parse 逻辑。"""

    name = "douban_spider"
    start_urls = ["https://movie.douban.com/top250"]

    def start_requests(self) -> list[dict[str, object]]:
        """生成初始请求，并附带 User-Agent 与 Referer。"""
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://movie.douban.com/",
        }
        return [{"url": url, "headers": headers, "callback": self.parse.__name__} for url in self.start_urls]

    def parse(self, response: FakeResponse) -> list[dict[str, str] | dict[str, object]]:
        """使用 CSS 选择器提取电影标题、评分、简介，并处理分页。"""
        titles = response.css("span.title::text")
        ratings = response.css("span.rating_num::text")
        quotes = response.css("span.inq::text")
        results: list[dict[str, str] | dict[str, object]] = []
        for title, rating, quote in zip(titles, ratings, quotes):
            results.append({"title": title, "rating": rating, "quote": quote})
        next_pages = response.css("span.next a::attr(href)")
        if next_pages:
            results.append(response.follow(next_pages[0], self.parse))
        return results


def demo_spider_parse() -> None:
    """执行 Scrapy 爬虫解析示例，使用本地 HTML 模拟响应。"""
    html = """
<div class="item"><span class="title">电影 A</span><span class="rating_num">9.1</span><span class="inq">很好看</span></div>
<div class="item"><span class="title">电影 B</span><span class="rating_num">8.8</span><span class="inq">值得看</span></div>
<span class="next"><a href="/top250?start=25">后页</a></span>
"""
    spider = DoubanSpider()
    print(spider.start_requests())
    response = FakeResponse("https://movie.douban.com/top250", html)
    print(spider.parse(response))
    print("scrapy crawl douban_spider -o douban_movies.csv")


def demo_methods_tables() -> None:
    """保留 Scrapy 常用方法、设置和工具命令表。"""
    show_table(
        ("方法", "作用描述", "示例"),
        [
            ("start_requests()", "生成初始请求", "yield scrapy.Request(url, callback=self.parse)"),
            ("parse(response)", "处理响应并提取数据", "yield {'title': response.css('h1::text').get()}"),
            ("follow(url, callback)", "自动处理相对 URL 并生成请求", "yield response.follow(next_page, callback=self.parse)"),
            ("closed(reason)", "爬虫关闭时调用", "def closed(self, reason): ..."),
            ("log(message)", "记录日志信息", "self.log('message')"),
        ],
    )
    show_table(
        ("设置项", "作用描述", "示例"),
        [
            ("USER_AGENT", "设置请求头中的 User-Agent", "USER_AGENT = 'Mozilla/5.0'"),
            ("ROBOTSTXT_OBEY", "是否遵守 robots.txt", "ROBOTSTXT_OBEY = False"),
            ("DOWNLOAD_DELAY", "设置下载延迟", "DOWNLOAD_DELAY = 2"),
            ("CONCURRENT_REQUESTS", "设置并发请求数", "CONCURRENT_REQUESTS = 16"),
            ("ITEM_PIPELINES", "启用管道", "ITEM_PIPELINES = {'myproject.pipelines.MyPipeline': 300}"),
            ("AUTOTHROTTLE_ENABLED", "启用自动限速", "AUTOTHROTTLE_ENABLED = True"),
        ],
    )
    show_table(
        ("工具", "作用", "示例"),
        [
            ("scrapy shell", "启动交互式 Shell", "scrapy shell 'http://example.com'"),
            ("scrapy crawl", "运行指定爬虫", "scrapy crawl myspider -o output.json"),
            ("scrapy check", "检查爬虫代码", "scrapy check"),
            ("scrapy fetch", "下载指定 URL 内容", "scrapy fetch 'http://example.com'"),
            ("scrapy view", "浏览器查看下载页面", "scrapy view 'http://example.com'"),
        ],
    )


def demo_response_methods() -> None:
    """演示 response.css、response.follow、response.json、response.text 等响应方法。"""
    response = FakeResponse("http://example.com", "<title>Example</title><a href='/next'>Next</a>")
    print(response.css("title::text"))
    print(response.css("a::attr(href)"))
    print(response.follow("/next", lambda value: value))
    print(response.json())
    print(response.text)


def main() -> None:
    """按 Scrapy 页面顺序运行全部示例。"""
    print("Python Scrapy 库")
    show_section("1. Scrapy 介绍")
    demo_scrapy_intro()
    show_section("2. 项目结构")
    demo_project_structure()
    show_section("3. 爬虫解析示例")
    demo_spider_parse()
    show_section("4. 常用方法和设置")
    demo_methods_tables()
    show_section("5. Response 方法")
    demo_response_methods()


if __name__ == "__main__":
    main()
