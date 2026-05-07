"""42 Python3 CGI编程

来源: https://www.runoob.com/python3/python3-cgi-programming.html
可单独运行: python 42_cgi_programming.py
"""

from __future__ import annotations

import html
import os
import tempfile
from pathlib import Path
from urllib.parse import parse_qs


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def render_page(title: str, body: str, headers: tuple[str, ...] = ("Content-type:text/html",)) -> str:
    """生成 CGI 响应文本，保留 HTTP 头部、空行和 HTML 结构。"""
    header_text = "\n".join(headers)
    return f"""{header_text}

<html>
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
</head>
<body>
{body}
</body>
</html>"""


def demo_first_cgi() -> None:
    """复刻第一个 CGI 程序：输出 Content-type 头部、空行和 HTML。"""
    print(render_page("Hello Word - 我的第一个 CGI 程序！", "<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>"))


def demo_http_headers() -> None:
    """保留 HTTP 头部说明和常见头部示例。"""
    headers = [
        "Content-type:text/html",
        "Expires: Date",
        "Location: URL",
        "Set-Cookie: String",
    ]
    for header in headers:
        print(header)
    print("CGI 输出头部后必须打印一个空行，表示头部结束。")


def demo_environment_variables() -> None:
    """复刻显示环境变量的 CGI 示例，限制输出前几项避免过长。"""
    items = list(os.environ.items())[:8]
    body = "<b>环境变量</b><br><ul>"
    for key, value in items:
        body += "<li><span style='color:green'>%30s </span> : %s </li>" % (html.escape(key), html.escape(value))
    body += "</ul>"
    print(render_page("环境变量", body, ("Content-type: text/html",)))


def handle_site_form(query_string: str) -> str:
    """模拟 cgi.FieldStorage().getvalue('site') 处理 GET 表单。"""
    form = parse_qs(query_string)
    site = form.get("site", ["提交数据为空"])[0]
    return render_page("菜鸟教程 CGI 测试实例", "<h2> 选中的网站是 %s</h2>" % html.escape(site))


def demo_get_method() -> None:
    """保留 GET 方法说明，并执行 site 参数读取示例。"""
    print("GET 示例 URL: /cgi-bin/hello.py?key1=value1&key2=value2")
    notes = [
        "GET 请求可被缓存",
        "GET 请求保留在浏览器历史记录中",
        "GET 请求可被收藏为书签",
        "GET 请求不应处理敏感数据",
        "GET 请求有长度限制",
    ]
    for note in notes:
        print(note)
    print(handle_site_form("site=runoob"))
    print(handle_site_form(""))


def handle_textarea_form(query_string: str) -> str:
    """模拟 textarea.py 接收 textcontent 字段。"""
    form = parse_qs(query_string)
    content = form.get("textcontent", ["没有内容"])[0]
    return render_page("菜鸟教程 CGI 测试实例", "<h2> 输入的内容是：%s</h2>" % html.escape(content))


def demo_textarea() -> None:
    """保留 Textarea HTML 表单和 CGI 接收逻辑。"""
    form_html = """<form action="/cgi-bin/textarea.py" method="post" target="_blank">
<textarea name="textcontent" cols="40" rows="4">在这里输入内容...</textarea>
<input type="submit" value="提交" />
</form>"""
    print(form_html)
    print(handle_textarea_form("textcontent=Runoob%20Python"))


def handle_dropdown_form(query_string: str) -> str:
    """模拟 dropdown.py 接收 dropdown 字段。"""
    form = parse_qs(query_string)
    value = form.get("dropdown", ["没有内容"])[0]
    return render_page("菜鸟教程 CGI 测试实例", "<h2> 选中的选项是：%s</h2>" % html.escape(value))


def demo_dropdown() -> None:
    """保留下拉框 HTML 表单和 CGI 接收逻辑。"""
    form_html = """<form action="/cgi-bin/dropdown.py" method="post" target="_blank">
<select name="dropdown">
<option value="runoob" selected>菜鸟教程</option>
<option value="google">Google</option>
</select>
<input type="submit" value="提交"/>
</form>"""
    print(form_html)
    print(handle_dropdown_form("dropdown=google"))


def demo_cookie() -> None:
    """保留 Cookie 设置和读取的 CGI 响应形式。"""
    response = render_page("Cookie", "<h2>Cookie 设置成功</h2>", ("Content-Type: text/html", "Set-Cookie: name=Runoob"))
    print(response)
    cookie_header = "name=Runoob; site=www.runoob.com"
    cookies = dict(part.strip().split("=", 1) for part in cookie_header.split(";"))
    print("读取 Cookie:", cookies)


def demo_file_upload() -> None:
    """模拟文件上传保存逻辑，使用临时目录代替 /tmp。"""
    with tempfile.TemporaryDirectory() as directory:
        fake_filename = "upload.txt"
        data = b"Runoob upload demo"
        filename = os.path.basename(fake_filename.replace("\\", "/"))
        path = Path(directory) / filename
        path.write_bytes(data)
        message = '文件 "' + filename + '" 上传成功'
        print(render_page("菜鸟教程(runoob.com)", "<p>%s</p>" % html.escape(message)))
        print(path.read_bytes())


def demo_file_download() -> None:
    """复刻文件下载对话框：设置 Content-Disposition 并输出文件内容。"""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "foo.txt"
        path.write_text("Runoob download demo", encoding="utf-8")
        print('Content-Disposition: attachment; filename="foo.txt"')
        print()
        print(path.read_text(encoding="utf-8"))


def main() -> None:
    """按 CGI 编程页面顺序运行全部示例。"""
    print("Python3 CGI编程")
    show_section("1. 第一个 CGI 程序")
    demo_first_cgi()
    show_section("2. HTTP 头部")
    demo_http_headers()
    show_section("3. 环境变量")
    demo_environment_variables()
    show_section("4. GET 方法")
    demo_get_method()
    show_section("5. Textarea 数据")
    demo_textarea()
    show_section("6. 下拉数据")
    demo_dropdown()
    show_section("7. Cookie")
    demo_cookie()
    show_section("8. 文件上传")
    demo_file_upload()
    show_section("9. 文件下载")
    demo_file_download()


if __name__ == "__main__":
    main()
