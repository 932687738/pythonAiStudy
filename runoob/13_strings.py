"""13 Python3 字符串

来源: https://www.runoob.com/python3/python3-string.html
可单独运行: python 13_strings.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的字符串表格。"""
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


def demo_create_string() -> None:
    """演示使用单引号和双引号创建字符串。"""
    var1 = "Hello World!"
    var2 = "Runoob"
    print(var1)
    print(var2)


def demo_access_string() -> None:
    """演示通过索引和切片访问字符串，复刻页面 var1/var2 示例。"""
    var1 = "Hello World!"
    var2 = "Runoob"
    print("var1[0]: ", var1[0])
    print("var2[1:5]: ", var2[1:5])
    print("索引从 0 开始，-1 表示末尾位置。")


def demo_update_string() -> None:
    """演示字符串不可原地修改，但可以通过切片拼接生成新字符串。"""
    var1 = "Hello World!"
    updated = var1[:6] + "Runoob!"
    print("已更新字符串 : ", updated)


def demo_escape_table() -> None:
    """保留页面中的常见转义字符表。"""
    show_table(
        ("转义字符", "描述", "示例结果"),
        [
            ("\\\\", "反斜杠", "\\"),
            ("\\'", "单引号", "'"),
            ('\\"', "双引号", '"'),
            ("\\n", "换行", "line1 / line2"),
            ("\\t", "横向制表符", "Hello    World"),
            ("\\r", "回车覆盖开头内容", "World!"),
            ("\\b", "退格", "Hello World"),
            ("\\f", "换页", "Hello / World"),
            ("\\ooo", "八进制字符", "\\110 -> H"),
            ("\\xhh", "十六进制字符", "\\x48 -> H"),
        ],
    )


def demo_escape_examples() -> None:
    """执行页面中不同转义字符的代表性示例。"""
    print("'Hello, world!'")
    print("Hello, world!\n How are you?")
    print("Hello, world!\t How are you?")
    print("Hello,\b world!")
    print("Hello,\f world!")
    print("A 对应的 ASCII 值为：", ord("A"))
    print("\x41 为 A 的 ASCII 代码")

    decimal_number = 42
    binary_number = bin(decimal_number)
    octal_number = oct(decimal_number)
    hexadecimal_number = hex(decimal_number)
    print("转换为二进制:", binary_number)
    print("转换为八进制:", octal_number)
    print("转换为十六进制:", hexadecimal_number)

    bar = "[" + "=" * 5 + " " * 5 + "]"
    print(f"页面的 \\r 进度条示例缩短展示: {bar}  10%")


def demo_string_operators_table() -> None:
    """保留字符串运算符表。"""
    show_table(
        ("操作符", "描述", "示例"),
        [
            ("+", "字符串连接", "a + b"),
            ("*", "重复输出字符串", "a * 2"),
            ("[]", "通过索引获取字符", "a[1]"),
            ("[:]", "截取字符串一部分，左闭右开", "a[1:4]"),
            ("in", "成员运算符", "'H' in a"),
            ("not in", "非成员运算符", "'M' not in a"),
            ("r/R", "原始字符串", "r'\\n'"),
            ("%", "格式字符串", "'%s' % name"),
        ],
    )


def demo_string_operators() -> None:
    """执行页面中 a='Hello'、b='Python' 的字符串运算符示例。"""
    a = "Hello"
    b = "Python"
    print("a + b 输出结果：", a + b)
    print("a * 2 输出结果：", a * 2)
    print("a[1] 输出结果：", a[1])
    print("a[1:4] 输出结果：", a[1:4])
    if "H" in a:
        print("H 在变量 a 中")
    else:
        print("H 不在变量 a 中")
    if "M" not in a:
        print("M 不在变量 a 中")
    else:
        print("M 在变量 a 中")
    print(r"\n")
    print(R"\n")


def demo_percent_formatting() -> None:
    """演示页面中的 % 字符串格式化，以及格式化符号表。"""
    print("我叫 %s 今年 %d 岁!" % ("小明", 10))
    show_table(
        ("符号", "描述", "示例"),
        [
            ("%c", "格式化字符及其 ASCII 码", "%c" % 65),
            ("%s", "格式化字符串", "%s" % "Runoob"),
            ("%d", "格式化整数", "%d" % 10),
            ("%o", "格式化无符号八进制数", "%o" % 10),
            ("%x", "格式化无符号十六进制数", "%x" % 255),
            ("%X", "格式化无符号十六进制数(大写)", "%X" % 255),
            ("%f", "格式化浮点数字", "%.2f" % 3.14159),
            ("%e", "科学计数法", "%e" % 1000),
            ("%g", "%f 和 %e 的简写", "%g" % 1000.0),
            ("%%", "输出百分号", "%%" % ()),
        ],
    )
    show_table(
        ("辅助符号", "功能", "示例"),
        [
            ("*", "定义宽度或精度", "%*.*f" % (8, 2, 3.14159)),
            ("-", "左对齐", "'%-8s'" % "hi"),
            ("+", "正数前显示加号", "%+d" % 10),
            ("空格", "正数前显示空格", "% d" % 10),
            ("#", "显示进制前缀", "%#x" % 255),
            ("0", "用 0 填充", "%05d" % 12),
            ("m.n", "宽度和精度", "%8.2f" % 3.14159),
        ],
    )


def demo_triple_quotes() -> None:
    """演示三引号字符串可以跨多行并保留格式。"""
    para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [
 ]。
"""
    print(para_str)

    err_html = """
<HTML><HEAD><TITLE> Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>示例错误信息</B><P>
</BODY></HTML>
"""
    sql = """
CREATE TABLE users (
    login VARCHAR(8),
    uid INTEGER,
    prid INTEGER
)
"""
    print("HTML 多行字符串片段:")
    print(err_html.strip())
    print("SQL 多行字符串片段:")
    print(sql.strip())


def demo_f_string() -> None:
    """演示 f-string 的变量替换、表达式计算和 Python 3.8 的调试写法。"""
    name = "Runoob"
    print("Hello %s" % name)
    print(f"Hello {name}")
    print(f"{1 + 2}")

    website = {"name": "Runoob", "url": "www.runoob.com"}
    print(f'{website["name"]}: {website["url"]}')

    x = 1
    print(f"{x + 1}")
    print(f"{x + 1=}")


def demo_unicode_string() -> None:
    """说明 Python3 中所有字符串都是 Unicode 字符串。"""
    text = "菜鸟教程 Runoob"
    print(text)
    print([hex(ord(char)) for char in text[:4]])


def demo_string_methods() -> None:
    """保留页面常见字符串内建函数，并执行代表性示例。"""
    text = " hello Runoob, hello Python "
    encoded = "中文".encode("utf-8")
    show_table(
        ("方法", "描述", "示例结果"),
        [
            ("capitalize()", "首字符大写", text.strip().capitalize()),
            ("center(width, fillchar)", "居中填充", "hi".center(8, "*")),
            ("count(str)", "统计出现次数", str(text.count("hello"))),
            ("bytes.decode()", "bytes 解码", encoded.decode("utf-8")),
            ("encode()", "字符串编码", str(encoded)),
            ("endswith()", "检查结尾", str(text.endswith(" "))),
            ("expandtabs()", "tab 转空格", "a\tb".expandtabs(4)),
            ("find()", "查找子串位置", str(text.find("Runoob"))),
            ("index()", "查找子串位置，找不到报错", str(text.index("Runoob"))),
            ("isalnum()", "是否字母数字", str("Runoob123".isalnum())),
            ("isalpha()", "是否全字母", str("Runoob".isalpha())),
            ("isdigit()", "是否全数字", str("123".isdigit())),
            ("islower()", "是否全小写", str("abc".islower())),
            ("lower()", "转小写", "Runoob".lower()),
            ("upper()", "转大写", "Runoob".upper()),
            ("strip()", "移除首尾空白", text.strip()),
            ("replace()", "替换字符串", text.replace("hello", "hi").strip()),
            ("split()", "分割字符串", str("a,b,c".split(","))),
            ("join()", "连接序列", "-".join(["a", "b", "c"])),
        ],
    )


def main() -> None:
    """按字符串页面顺序运行全部示例。"""
    print("Python3 字符串")

    show_section("1. 创建字符串")
    demo_create_string()

    show_section("2. 访问字符串中的值")
    demo_access_string()

    show_section("3. 字符串更新")
    demo_update_string()

    show_section("4. 转义字符表")
    demo_escape_table()

    show_section("5. 转义字符示例")
    demo_escape_examples()

    show_section("6. 字符串运算符表")
    demo_string_operators_table()

    show_section("7. 字符串运算符示例")
    demo_string_operators()

    show_section("8. 字符串格式化")
    demo_percent_formatting()

    show_section("9. 三引号")
    demo_triple_quotes()

    show_section("10. f-string")
    demo_f_string()

    show_section("11. Unicode 字符串")
    demo_unicode_string()

    show_section("12. 字符串内建函数")
    demo_string_methods()


if __name__ == "__main__":
    main()
