"""58 Python requests

来源: https://www.runoob.com/python3/python-requests.html
可单独运行: python 58_requests_tutorial.py
"""

from __future__ import annotations

import json
import urllib.parse
import urllib.request
from dataclasses import dataclass


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 requests 方法和响应属性表。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        """格式化表格行。"""
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


@dataclass
class FakeResponse:
    """模拟 requests.Response，避免依赖 requests 包和真实网络。"""

    url: str
    status_code: int = 200
    text: str = "<html>Runoob</html>"
    content: bytes = b"<html>Runoob</html>"
    headers: dict[str, str] | None = None
    apparent_encoding: str = "utf-8"

    def json(self) -> dict[str, object]:
        """模拟 response.json()。"""
        return json.loads(self.text)

    def close(self) -> None:
        """模拟关闭连接。"""
        print("connection closed")


def fake_get(url: str, params: dict[str, str] | None = None, headers: dict[str, str] | None = None) -> FakeResponse:
    """模拟 requests.get，保留 params 自动编码和 headers 传入逻辑。"""
    if params:
        query = urllib.parse.urlencode(params)
        url = url + ("&" if "?" in url else "?") + query
    return FakeResponse(url=url, headers=headers or {"Content-Type": "text/html; charset=utf-8"})


def fake_post(url: str, data: dict[str, str] | None = None, json_data: dict[str, object] | None = None) -> FakeResponse:
    """模拟 requests.post，返回可 json() 的响应对象。"""
    payload = {"form": data, "json": json_data}
    return FakeResponse(url=url, text=json.dumps(payload, ensure_ascii=False), content=json.dumps(payload).encode("utf-8"))


def demo_response_attributes() -> None:
    """保留 response 对象常见属性和方法。"""
    response = fake_get("https://www.runoob.com/")
    show_table(
        ("属性或方法", "说明", "示例结果"),
        [
            ("status_code", "响应状态码", str(response.status_code)),
            ("headers", "响应头", str(response.headers)),
            ("content", "字节内容", str(response.content)),
            ("text", "文本内容", response.text),
            ("apparent_encoding", "编码方式", response.apparent_encoding),
            ("close()", "关闭连接", "见输出"),
        ],
    )
    response.close()


def demo_methods_table() -> None:
    """保留 requests 请求方法表。"""
    show_table(
        ("方法", "描述"),
        [
            ("delete(url,args)", "发送 DELETE 请求"),
            ("get(url,params,args)", "发送 GET 请求"),
            ("head(url,args)", "发送 HEAD 请求"),
            ("patch(url,data,args)", "发送 PATCH 请求"),
            ("post(url,data,json,args)", "发送 POST 请求"),
            ("put(url,data,args)", "发送 PUT 请求"),
            ("request(method,url,args)", "发送指定方法请求"),
        ],
    )


def demo_get_request() -> None:
    """复刻 requests.get 和 request('get') 示例，使用模拟响应。"""
    response = fake_get("https://www.runoob.com/")
    print(response.text)
    print(response.status_code)


def demo_params_headers() -> None:
    """复刻 params 字典和 headers 请求头示例。"""
    params = {"s": "python 教程"}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = fake_get("https://www.runoob.com/", params=params, headers=headers)
    print(response.url)
    print(response.headers)


def demo_post_json() -> None:
    """演示 POST 表单和 JSON 数据，以及 response.json()。"""
    response = fake_post("https://www.runoob.com/post", data={"name": "RUNOOB"}, json_data={"site": "runoob"})
    print(response.text)
    print(response.json())


def demo_urllib_equivalent() -> None:
    """用 urllib 构造等价请求，说明 requests 比 urllib 更简洁。"""
    data = urllib.parse.urlencode({"name": "RUNOOB"}).encode("utf-8")
    request = urllib.request.Request("https://www.runoob.com/post", data=data, headers={"User-Agent": "Mozilla/5.0"})
    print(request.full_url)
    print(request.data)
    print(request.headers)


def main() -> None:
    """按 requests 页面顺序运行全部示例。"""
    print("Python requests")
    show_section("1. response 属性")
    demo_response_attributes()
    show_section("2. requests 方法")
    demo_methods_table()
    show_section("3. GET 请求")
    demo_get_request()
    show_section("4. params 和 headers")
    demo_params_headers()
    show_section("5. POST 和 JSON")
    demo_post_json()
    show_section("6. urllib 等价写法")
    demo_urllib_equivalent()


if __name__ == "__main__":
    main()
