"""41 Python3 正则表达式

来源: https://www.runoob.com/python3/python3-reg-expressions.html
可单独运行: python 41_regex.py
"""

from __future__ import annotations

import re


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的参数、标志和正则模式表。"""
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


def demo_match() -> None:
    """执行 re.match 示例，展示从字符串起始位置匹配。"""
    print(re.match("www", "www.runoob.com").span())
    result = re.match("com", "www.runoob.com")
    print(result)


def demo_search_groups() -> None:
    """执行 re.search 分组示例，提取 Cats 和 smarter。"""
    line = "Cats are smarter than dogs"
    search_obj = re.search(r"(.*) are (.*?) .*", line, re.M | re.I)
    if search_obj:
        print("searchObj.group() : ", search_obj.group())
        print("searchObj.group(1) : ", search_obj.group(1))
        print("searchObj.group(2) : ", search_obj.group(2))
    else:
        print("Nothing found!!")


def demo_match_search_difference() -> None:
    """复刻 re.match 与 re.search 的区别示例。"""
    line = "Cats are smarter than dogs"
    match_obj = re.match(r"dogs", line, re.M | re.I)
    if match_obj:
        print("match --> matchObj.group() : ", match_obj.group())
    else:
        print("No match!!")
    search_obj = re.search(r"dogs", line, re.M | re.I)
    if search_obj:
        print("search --> searchObj.group() : ", search_obj.group())
    else:
        print("No match!!")


def demo_substitution() -> None:
    """执行 re.sub 替换示例，去除 Python 注释和替换 phone。"""
    phone = "2004-959-559 # 这是一个电话号码"
    num = re.sub(r"#.*$", "", phone)
    print("电话号码 : ", num)
    num = re.sub(r"\D", "", phone)
    print("电话号码 : ", num)

    def double(matched: re.Match[str]) -> str:
        """把匹配到的数字乘二。"""
        value = int(matched.group("value"))
        return str(value * 2)

    text = "A23G4HFD567"
    print(re.sub(r"(?P<value>\d+)", double, text))


def demo_findall_finditer() -> None:
    """执行 findall、compile、finditer 和多分组匹配示例。"""
    result1 = re.findall(r"\d+", "runoob 123 google 456")
    pattern = re.compile(r"\d+")
    result2 = pattern.findall("runoob 123 google 456")
    result3 = pattern.findall("run88oob123google456", 0, 10)
    print(result1)
    print(result2)
    print(result3)
    print(re.findall(r"(\w+)=(\d+)", "set width=20 and height=10"))
    for match in re.finditer(r"\d+", "12a32bc43jf3"):
        print(match.group(), match.span())


def demo_split_compile_match_object() -> None:
    """执行 split、compile 和 MatchObject 的 group/start/end/span 示例。"""
    print(re.split(r"\W+", "runoob, runoob, runoob."))
    pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)
    match = pattern.match("Hello World Wide Web")
    if match:
        print(match.group())
        print(match.group(1))
        print(match.group(2))
        print(match.start())
        print(match.end())
        print(match.span())


def demo_flags_table_and_examples() -> None:
    """保留正则修饰符表，并执行 IGNORECASE、MULTILINE、DOTALL、ASCII、VERBOSE 示例。"""
    show_table(
        ("修饰符", "描述", "示例结果"),
        [
            ("re.I / IGNORECASE", "大小写不敏感", re.compile(r"apple", re.I).match("Apple").group()),
            ("re.M / MULTILINE", "^ 和 $ 匹配每一行", str(re.compile(r"^\\d+", re.M).findall("123\n456\n789"))),
            ("re.S / DOTALL", ". 匹配换行符", repr(re.compile(r"a.b", re.S).match("a\nb").group())),
            ("re.ASCII", "\\w 等仅匹配 ASCII", re.compile(r"\w+", re.ASCII).match("Hello123").group()),
            ("re.X / VERBOSE", "忽略空格和注释", re.compile(r"""\d+ [a-z]+""", re.X).match("123abc").group()),
        ],
    )


def demo_pattern_tables() -> None:
    """保留正则表达式实例表中的字符类、特殊类、重复和边界模式。"""
    show_table(
        ("模式", "描述", "示例匹配"),
        [
            ("python", '匹配 "python"', str(bool(re.search("python", "python")))),
            ("[Pp]ython", "匹配 Python 或 python", str(re.findall("[Pp]ython", "Python python"))),
            ("[0-9]", "匹配数字", str(re.findall("[0-9]", "a1b2"))),
            ("[^0-9]", "匹配非数字", str(re.findall("[^0-9]", "a1"))),
            (".", "匹配除换行外任意字符", re.findall(".", "ab")[0]),
            ("\\d", "数字字符", str(re.findall(r"\d", "a1b2"))),
            ("\\D", "非数字字符", str(re.findall(r"\D", "a1"))),
            ("\\s", "空白字符", str(re.findall(r"\s", "a b"))),
            ("\\w", "单词字符", str(re.findall(r"\w+", "abc_123"))),
            ("a*", "0 次或多次", str(re.findall(r"ab*", "ab abb a"))),
            ("a+", "1 次或多次", str(re.findall(r"ab+", "ab abb a"))),
            ("a?", "0 次或 1 次", str(re.findall(r"colou?r", "color colour"))),
            ("^", "匹配开头", str(bool(re.search(r"^cat", "cat dog")))),
            ("$", "匹配结尾", str(bool(re.search(r"dog$", "cat dog")))),
        ],
    )


def main() -> None:
    """按正则表达式页面顺序运行全部示例。"""
    print("Python3 正则表达式")
    show_section("1. re.match")
    demo_match()
    show_section("2. re.search 和分组")
    demo_search_groups()
    show_section("3. match 与 search 区别")
    demo_match_search_difference()
    show_section("4. re.sub")
    demo_substitution()
    show_section("5. findall 与 finditer")
    demo_findall_finditer()
    show_section("6. split、compile 和 MatchObject")
    demo_split_compile_match_object()
    show_section("7. 修饰符")
    demo_flags_table_and_examples()
    show_section("8. 正则模式表")
    demo_pattern_tables()


if __name__ == "__main__":
    main()
