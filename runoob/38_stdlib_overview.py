"""38 Python3 标准库概览

来源: https://www.runoob.com/python3/python3-stdlib.html
可单独运行: python 38_stdlib_overview.py
"""

from __future__ import annotations

import datetime
import glob
import math
import os
import random
import re
import statistics
import string
import sys
import tempfile
import urllib.parse
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def demo_file_wildcards() -> None:
    """复刻 glob 模块文件通配符搜索示例。"""
    with tempfile.TemporaryDirectory() as directory:
        Path(directory, "primes.py").write_text("", encoding="utf-8")
        Path(directory, "random.py").write_text("", encoding="utf-8")
        Path(directory, "quote.py").write_text("", encoding="utf-8")
        print([Path(path).name for path in glob.glob(os.path.join(directory, "*.py"))])


def demo_command_line_arguments() -> None:
    """复刻 sys.argv 命令行参数示例。"""
    print(sys.argv)


def demo_stderr_and_exit_note() -> None:
    """演示 stderr 输出，并说明 sys.exit 常用于脚本终止。"""
    written = sys.stderr.write("Warning, log file not found starting a new one\n")
    print("stderr 写入字符数:", written)
    print("sys.exit() 可用于定向终止脚本，本示例不实际退出。")


def demo_re_module() -> None:
    """复刻 re 模块查找和替换示例，并对比字符串 replace。"""
    print(re.findall(r"\bf[a-z]*", "which foot or hand fell fastest"))
    print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat"))
    print("tea for too".replace("too", "two"))


def demo_math_random() -> None:
    """复刻 math 和 random 模块示例，用固定随机种子保证输出稳定。"""
    print(math.cos(math.pi / 4))
    print(math.log(1024, 2))
    random.seed(7)
    print(random.choice(["apple", "pear", "banana"]))
    print(random.sample(range(100), 10))
    print(round(random.random(), 6))
    print(random.randrange(6))


def demo_internet_note() -> None:
    """保留 urllib 和 smtplib 网络通信说明，使用 URL 解析避免真实联网。"""
    parsed = urllib.parse.urlparse("https://www.runoob.com/python3/")
    print(parsed.scheme)
    print(parsed.netloc)
    print("smtplib.SMTP('localhost') 需要本地邮件服务器，本示例不实际连接。")


def demo_datetime_module() -> None:
    """复刻 datetime 日期时间处理示例。"""
    now = datetime.date.today()
    print(now)
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
    birthday = datetime.date(1964, 7, 31)
    age = now - birthday
    print(age.days)


def demo_data_compression_note() -> None:
    """保留数据压缩模块说明。"""
    modules = ["zlib", "gzip", "bz2", "lzma", "zipfile", "tarfile"]
    print("压缩相关模块:", ", ".join(modules))


def demo_performance_measurement_note() -> None:
    """保留性能度量模块说明。"""
    import timeit

    print(timeit.timeit("'Python'.replace('P', 'J')", number=1000))


def demo_quality_control_note() -> None:
    """保留 doctest 和 unittest 质量控制模块说明。"""
    modules = ["doctest", "unittest"]
    print("测试相关模块:", ", ".join(modules))


def demo_batteries_included() -> None:
    """保留标准库其他常用模块示例：statistics、string。"""
    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print(statistics.mean(data))
    print(statistics.median(data))
    print(statistics.variance(data))
    template = string.Template("$name is learning $language")
    print(template.substitute(name="Runoob", language="Python"))


def main() -> None:
    """按标准库概览页面顺序运行全部示例。"""
    print("Python3 标准库概览")

    show_section("1. 文件通配符")
    demo_file_wildcards()

    show_section("2. 命令行参数")
    demo_command_line_arguments()

    show_section("3. 错误输出和程序终止")
    demo_stderr_and_exit_note()

    show_section("4. 正则匹配")
    demo_re_module()

    show_section("5. 数学和随机数")
    demo_math_random()

    show_section("6. 访问互联网")
    demo_internet_note()

    show_section("7. 日期和时间")
    demo_datetime_module()

    show_section("8. 数据压缩")
    demo_data_compression_note()

    show_section("9. 性能度量")
    demo_performance_measurement_note()

    show_section("10. 质量控制")
    demo_quality_control_note()

    show_section("11. 其他标准库")
    demo_batteries_included()


if __name__ == "__main__":
    main()
