"""45 Python3 网络编程

来源: https://www.runoob.com/python3/python3-socket.html
可单独运行: python 45_network_programming.py
"""

from __future__ import annotations

import socket
import threading


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 socket 对象方法和互联网协议表。"""
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


def demo_socket_intro() -> None:
    """保留 Socket 基本概念和 socket() 函数参数。"""
    show_table(
        ("参数", "说明"),
        [
            ("family", "套接字家族，如 AF_INET 或 AF_UNIX"),
            ("type", "套接字类型，如 SOCK_STREAM 或 SOCK_DGRAM"),
            ("proto", "协议号，通常为 0"),
        ],
    )


def demo_socket_methods_table() -> None:
    """保留服务器端和客户端 socket 对象主要方法。"""
    show_table(
        ("方法", "描述"),
        [
            ("bind()", "绑定地址到套接字"),
            ("listen()", "开始 TCP 监听"),
            ("accept()", "被动接受 TCP 客户端连接"),
            ("connect()", "主动初始化 TCP 连接"),
            ("recv()", "接收数据"),
            ("send()/sendall()", "发送数据"),
            ("close()", "关闭套接字"),
            ("settimeout()", "设置超时时间"),
        ],
    )


def run_local_server(port_holder: list[int], ready: threading.Event) -> None:
    """启动本地 TCP 服务端，发送页面示例中的欢迎消息后关闭。"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        port_holder.append(server.getsockname()[1])
        ready.set()
        connection, address = server.accept()
        with connection:
            print("连接地址：", address)
            connection.sendall("欢迎访问菜鸟教程！".encode("utf-8"))


def demo_local_socket_client_server() -> None:
    """复刻 server.py/client.py 逻辑，使用本地回环地址和随机端口避免外部依赖。"""
    port_holder: list[int] = []
    ready = threading.Event()
    server_thread = threading.Thread(target=run_local_server, args=(port_holder, ready), daemon=True)
    server_thread.start()
    ready.wait(timeout=5)
    host = "127.0.0.1"
    port = port_holder[0]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        message = client.recv(1024)
    server_thread.join(timeout=5)
    print(message.decode("utf-8"))


def demo_udp_note() -> None:
    """补充演示 UDP 套接字创建，保留网络编程低级服务概念。"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        print("UDP socket type:", sock.type == socket.SOCK_DGRAM)


def demo_internet_modules_table() -> None:
    """保留页面中的 Python Internet 模块表。"""
    show_table(
        ("协议", "功能用处", "端口号", "Python 模块"),
        [
            ("HTTP", "网页访问", "80", "http.client, urllib, xmlrpc"),
            ("NNTP", "阅读和张贴新闻文章", "119", "nntplib"),
            ("FTP", "文件传输", "20", "ftplib, urllib"),
            ("SMTP", "发送邮件", "25", "smtplib"),
            ("POP3", "接收邮件", "110", "poplib"),
            ("IMAP4", "获取邮件", "143", "imaplib"),
            ("Telnet", "命令行", "23", "telnetlib"),
            ("Gopher", "信息查找", "70", "gopherlib, urllib"),
        ],
    )


def main() -> None:
    """按网络编程页面顺序运行全部示例。"""
    print("Python3 网络编程")
    show_section("1. Socket 概念")
    demo_socket_intro()
    show_section("2. Socket 方法")
    demo_socket_methods_table()
    show_section("3. 本地 TCP 服务端与客户端")
    demo_local_socket_client_server()
    show_section("4. UDP 套接字")
    demo_udp_note()
    show_section("5. Python Internet 模块")
    demo_internet_modules_table()


if __name__ == "__main__":
    main()
