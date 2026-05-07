"""54 Python uWSGI 安装配置

来源: https://www.runoob.com/python3/python-uwsgi.html
可单独运行: python 54_uwsgi_installation.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 uWSGI 安装、命令和配置说明。"""
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


def application(env: dict[str, str], start_response) -> list[bytes]:
    """页面第一个 WSGI 应用：返回 Hello World。"""
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"Hello World"]


def demo_install_commands() -> None:
    """保留 Ubuntu/Debian 依赖安装和三种 uWSGI 安装方式。"""
    commands = [
        "apt-get install build-essential python-dev",
        "pip install uwsgi",
        "curl http://uwsgi.it/install | bash -s default /tmp/uwsgi",
        "wget http://projects.unbit.it/downloads/uwsgi-latest.tar.gz",
        "tar zxvf uwsgi-latest.tar.gz",
        "cd uwsgi-latest",
        "make",
    ]
    for command in commands:
        print(command)


def demo_wsgi_application() -> None:
    """执行 WSGI application 函数，模拟 uWSGI Python 加载器调用。"""
    status_headers: list[object] = []

    def start_response(status: str, headers: list[tuple[str, str]]) -> None:
        """记录 WSGI 响应状态和响应头。"""
        status_headers.append((status, headers))

    body = application({}, start_response)
    print(status_headers)
    print(body)
    print(body[0].decode("utf-8"))


def demo_uwsgi_commands() -> None:
    """保留启动 HTTP 服务、并发、监控、socket/http-socket 命令。"""
    show_table(
        ("场景", "命令"),
        [
            ("HTTP 端口 9090", "uwsgi --http :9090 --wsgi-file foobar.py"),
            ("进程和线程", "uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2"),
            ("stats 监控", "uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191"),
            ("uwsgi 协议 socket", "uwsgi --socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 --threads 2"),
            ("HTTP socket", "uwsgi --http-socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 --threads 2"),
        ],
    )


def demo_nginx_config() -> None:
    """保留 Nginx 与 uWSGI 结合的配置片段。"""
    config = """location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:3031;
}"""
    print(config)


def demo_django_flask_commands() -> None:
    """保留 Django 和 Flask 部署命令与 ini 配置。"""
    django_command = (
        "uwsgi --socket 127.0.0.1:3031 --chdir /home/foobar/myproject/ "
        "--wsgi-file myproject/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191"
    )
    ini_config = """[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/foobar/myproject/
wsgi-file = myproject/wsgi.py
processes = 4
threads = 2
stats = 127.0.0.1:9191"""
    flask_app = """from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"
"""
    flask_command = (
        "uwsgi --socket 127.0.0.1:3031 --wsgi-file myflaskapp.py "
        "--callable app --processes 4 --threads 2 --stats 127.0.0.1:9191"
    )
    print(django_command)
    print(ini_config)
    print("uwsgi yourfile.ini")
    print(flask_app)
    print(flask_command)


def main() -> None:
    """按 uWSGI 安装配置页面顺序运行全部示例。"""
    print("Python uWSGI 安装配置")
    show_section("1. 安装命令")
    demo_install_commands()
    show_section("2. 第一个 WSGI 应用")
    demo_wsgi_application()
    show_section("3. uWSGI 启动命令")
    demo_uwsgi_commands()
    show_section("4. Nginx 配置")
    demo_nginx_config()
    show_section("5. Django 和 Flask 部署")
    demo_django_flask_commands()


if __name__ == "__main__":
    main()
