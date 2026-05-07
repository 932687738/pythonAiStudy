"""46 Python3 SMTP发送邮件

来源: https://www.runoob.com/python3/python3-smtp.html
可单独运行: python 46_smtp_email.py
"""

from __future__ import annotations

import smtplib
import tempfile
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 SMTP 对象参数和发送流程。"""
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


class DummySMTP:
    """模拟 smtplib.SMTP，保留 sendmail 调用逻辑但不连接真实服务器。"""

    def __init__(self, host: str = "localhost", port: int = 25) -> None:
        """保存模拟 SMTP 地址。"""
        self.host = host
        self.port = port
        self.sent_messages: list[tuple[str, list[str], str]] = []

    def connect(self, host: str, port: int) -> None:
        """模拟连接 SMTP 服务器。"""
        self.host = host
        self.port = port
        print(f"connect({host}, {port})")

    def login(self, user: str, password: str) -> None:
        """模拟登录 SMTP 服务。"""
        print(f"login({user}, {'*' * len(password)})")

    def sendmail(self, from_addr: str, to_addrs: list[str], msg: str) -> None:
        """记录发送参数，模拟 sendmail。"""
        self.sent_messages.append((from_addr, to_addrs, msg))
        print("邮件发送成功")

    def quit(self) -> None:
        """模拟关闭连接。"""
        print("quit()")


def demo_smtp_object_table() -> None:
    """保留 SMTP 对象创建和 sendmail 参数说明。"""
    show_table(
        ("参数", "说明"),
        [
            ("host", "SMTP 服务器主机，如 localhost 或 smtp.qq.com"),
            ("port", "SMTP 服务端口，常见为 25，SSL 常见为 465"),
            ("local_hostname", "本地主机名，可选"),
            ("from_addr", "发件人地址"),
            ("to_addrs", "收件人地址列表"),
            ("msg", "符合邮件格式的字符串"),
        ],
    )


def build_plain_message() -> MIMEText:
    """复刻纯文本邮件示例，构造 MIMEText、From、To 和 Subject。"""
    message = MIMEText("Python 邮件发送测试...", "plain", "utf-8")
    message["From"] = Header("菜鸟教程", "utf-8")
    message["To"] = Header("测试", "utf-8")
    message["Subject"] = Header("Python SMTP 邮件测试", "utf-8")
    return message


def demo_plain_email() -> None:
    """执行纯文本邮件构造和模拟发送。"""
    sender = "from@runoob.com"
    receivers = ["to@runoob.com"]
    message = build_plain_message()
    smtp_obj = DummySMTP("localhost")
    smtp_obj.sendmail(sender, receivers, message.as_string())
    print(message.as_string().splitlines()[:6])


def demo_third_party_smtp() -> None:
    """保留第三方 SMTP 服务发送流程：connect、login、sendmail。"""
    mail_host = "smtp.XXX.com"
    mail_user = "XXXX"
    mail_pass = "XXXXXX"
    sender = "from@runoob.com"
    receivers = ["to@runoob.com"]
    message = build_plain_message()
    smtp_obj = DummySMTP()
    smtp_obj.connect(mail_host, 25)
    smtp_obj.login(mail_user, mail_pass)
    smtp_obj.sendmail(sender, receivers, message.as_string())
    smtp_obj.quit()


def demo_html_email() -> None:
    """复刻发送 HTML 格式邮件示例。"""
    sender = "from@runoob.com"
    receivers = ["to@runoob.com"]
    mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
    message = MIMEText(mail_msg, "html", "utf-8")
    message["From"] = Header("菜鸟教程", "utf-8")
    message["To"] = Header("测试", "utf-8")
    message["Subject"] = Header("Python SMTP 邮件测试", "utf-8")
    DummySMTP("localhost").sendmail(sender, receivers, message.as_string())
    print(message.get_content_subtype())


def demo_qq_smtp_flow() -> None:
    """保留 QQ SMTP SSL 发送流程，用 DummySMTP 模拟真实连接。"""
    my_sender = "from@runoob.com"
    my_pass = "xxxxxxxxxx"
    my_user = "to@runoob.com"
    msg = MIMEText("填写邮件内容", "plain", "utf-8")
    msg["From"] = formataddr(["FromRunoob", my_sender])
    msg["To"] = formataddr(["FK", my_user])
    msg["Subject"] = "菜鸟教程发送邮件测试"
    server = DummySMTP("smtp.qq.com", 465)
    server.login(my_sender, my_pass)
    server.sendmail(my_sender, [my_user], msg.as_string())
    server.quit()


def demo_attachment_email() -> None:
    """复刻带附件邮件：MIMEMultipart + 多个附件。"""
    sender = "from@runoob.com"
    receivers = ["to@runoob.com"]
    message = MIMEMultipart()
    message["From"] = Header("菜鸟教程", "utf-8")
    message["To"] = Header("测试", "utf-8")
    message["Subject"] = Header("Python SMTP 邮件测试", "utf-8")
    message.attach(MIMEText("这是菜鸟教程Python 邮件发送测试……", "plain", "utf-8"))

    with tempfile.TemporaryDirectory() as directory:
        first = Path(directory) / "test.txt"
        second = Path(directory) / "runoob.txt"
        first.write_text("test attachment", encoding="utf-8")
        second.write_text("runoob attachment", encoding="utf-8")
        for path in [first, second]:
            attachment = MIMEText(path.read_bytes(), "base64", "utf-8")
            attachment["Content-Type"] = "application/octet-stream"
            attachment["Content-Disposition"] = f'attachment; filename="{path.name}"'
            message.attach(attachment)
    DummySMTP("localhost").sendmail(sender, receivers, message.as_string())
    print("附件数量:", len(message.get_payload()) - 1)


def demo_smtp_exception_note() -> None:
    """保留 smtplib.SMTPException 处理方式。"""
    try:
        raise smtplib.SMTPException("模拟无法发送邮件")
    except smtplib.SMTPException as exc:
        print("Error: 无法发送邮件")
        print(exc)


def main() -> None:
    """按 SMTP 页面顺序运行全部示例。"""
    print("Python3 SMTP发送邮件")
    show_section("1. SMTP 对象和 sendmail")
    demo_smtp_object_table()
    show_section("2. 纯文本邮件")
    demo_plain_email()
    show_section("3. 第三方 SMTP")
    demo_third_party_smtp()
    show_section("4. HTML 邮件")
    demo_html_email()
    show_section("5. QQ SMTP 流程")
    demo_qq_smtp_flow()
    show_section("6. 附件邮件")
    demo_attachment_email()
    show_section("7. 异常处理")
    demo_smtp_exception_note()


if __name__ == "__main__":
    main()
