"""78 Python re 模块

来源: https://www.runoob.com/python3/python-re.html
可单独运行: python 78_re_module.py
"""

from __future__ import annotations

import re


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 re 核心函数、匹配对象和注意事项。"""
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


def demo_basic_functions() -> None:
    """执行 match、search、findall、sub、split、finditer、fullmatch 示例。"""
    print(re.match(r"hello", "hello world").group())
    print(re.search(r"world", "hello world").group())
    print(re.findall(r"\d+", "There are 3 apples and 5 oranges."))
    print(re.sub(r"\d+", "X", "a1b22c"))
    print(re.split(r"\d+", "Apple1Banana2Cherry3Date"))
    print(re.fullmatch(r"\d+", "123").group())
    for match in re.finditer(r"\d+", "a1b22c333"):
        print(match.group(), match.span())


def demo_core_table() -> None:
    """保留 re 核心函数表。"""
    show_table(
        ("方法", "说明", "示例"),
        [
            ("re.compile(pattern)", "预编译正则表达式", "pat = re.compile(r'\\d+')"),
            ("re.search(pattern,string)", "搜索第一个匹配项", "re.search(r'\\d+', 'a1b2')"),
            ("re.match(pattern,string)", "从字符串起始位置匹配", "re.match(r'\\d+', '123a')"),
            ("re.fullmatch(pattern,string)", "整个字符串完全匹配", "re.fullmatch(r'\\d+', '123')"),
            ("re.findall(pattern,string)", "返回所有匹配列表", "re.findall(r'\\d+', 'a1b22c')"),
            ("re.finditer(pattern,string)", "返回匹配迭代器", "for m in re.finditer(...)"),
            ("re.sub(pattern,repl,string)", "替换匹配项", "re.sub(r'\\d+', 'X', 'a1b2')"),
            ("re.split(pattern,string)", "按匹配项分割", "re.split(r'\\d+', 'a1b2c')"),
            ("re.escape()", "转义特殊字符", "re.escape('C:\\\\Users')"),
            ("re.purge()", "清除缓存", "re.purge()"),
        ],
    )


def demo_match_object() -> None:
    """演示匹配对象 group、groups、groupdict、start、end、span。"""
    pattern = re.compile(r"(?P<username>\w+):(?P<password>\S+)@(?P<domain>\w+\.\w+)")
    match = pattern.match("john:pass123@example.com")
    if match:
        print(match.group())
        print(match.group(1))
        print(match.groups())
        print(match.groupdict())
        print(match.start(), match.end(), match.span())


def demo_practice_examples() -> None:
    """执行页面中的邮箱验证、电话提取、日期替换和复杂分组示例。"""
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    email = "test@example.com"
    print("有效的电子邮件地址" if re.match(email_pattern, email) else "无效的电子邮件地址")
    phone_text = "My phone number is 123-456-7890."
    match = re.search(r"\d{3}-\d{3}-\d{4}", phone_text)
    print(match.group() if match else "未找到")
    date_str = "Today is 05-15-2023"
    print(re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3年\1月\2日", date_str))
    text = "Contact: alice@example.com, bob@example.org"
    print(re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text))


def demo_flags_and_notes() -> None:
    """保留正则使用注意事项和常用标志示例。"""
    show_table(
        ("主题", "说明", "示例结果"),
        [
            ("原始字符串", "建议使用 r'\\d' 避免转义冲突", r"\d"),
            ("贪婪匹配", ".* 默认尽可能多匹配", re.findall(r"<.*>", "<a>1</a><b>2</b>")[0]),
            ("非贪婪匹配", ".*? 尽可能少匹配", str(re.findall(r"<.*?>", "<a>1</a><b>2</b>"))),
            ("re.I", "忽略大小写", re.search("python", "Python", re.I).group()),
            ("re.M", "多行模式", str(re.findall(r"^\d+", "1\n2", re.M))),
            ("re.S", ". 可匹配换行", repr(re.search(r"a.b", "a\nb", re.S).group())),
            ("预编译", "频繁使用的正则应 compile", "re.compile(pattern)"),
            ("回溯问题", "避免复杂嵌套量词导致性能问题", "(a+)+"),
        ],
    )


def main() -> None:
    """按 re 模块页面顺序运行全部示例。"""
    print("Python re 模块")
    show_section("1. 基础函数")
    demo_basic_functions()
    show_section("2. 核心函数表")
    demo_core_table()
    show_section("3. Match 对象")
    demo_match_object()
    show_section("4. 实践练习")
    demo_practice_examples()
    show_section("5. 标志和注意事项")
    demo_flags_and_notes()


if __name__ == "__main__":
    main()
