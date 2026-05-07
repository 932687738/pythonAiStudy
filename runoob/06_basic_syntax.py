"""06 Python3 基础语法

来源: https://www.runoob.com/python3/python3-basic-syntax.html
可单独运行: python 06_basic_syntax.py
"""

from __future__ import annotations

import sys
from keyword import iskeyword, kwlist


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的表格信息。"""
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


def demo_encoding() -> None:
    """说明 Python3 默认编码，并验证中文内容可直接运行输出。"""
    print("Python3 源码默认使用 UTF-8 编码。")
    print("本文件本身也保留了中文内容，运行时不会依赖特殊编码处理。")


def demo_identifier() -> None:
    """演示标识符规则、合法标识符赋值，以及非法标识符编译错误。"""
    print("标识符规则：")
    rules = [
        "只能以字母或下划线开头",
        "后面可以接字母、数字或下划线",
        "标识符区分大小写",
        "不能使用关键字",
    ]
    for item in rules:
        print(f"- {item}")

    print("合法标识符示例：")
    legal_names = ["age", "user_name", "_total", "StudentInfo"]
    namespace: dict[str, object] = {}
    for name in legal_names:
        exec(f"{name} = 1", {}, namespace)
        print(f"  {name!r} -> isidentifier={name.isidentifier()}, keyword={iskeyword(name)}, value={namespace[name]}")

    print("非法标识符示例：")
    illegal_names = ["2name", "class", "user-name"]
    for name in illegal_names:
        print(f"  {name!r} -> isidentifier={name.isidentifier()}, keyword={iskeyword(name)}")
        try:
            compile(f"{name} = 1", "<identifier-demo>", "exec")
            print("    unexpectedly compilable")
        except SyntaxError as exc:
            print(f"    SyntaxError: {exc.msg}")


def demo_keywords() -> None:
    """展示 Python 关键字列表，并用 iskeyword 判断名称是否为关键字。"""
    print(f"Python 当前版本关键字数量: {len(kwlist)}")
    print(f"前 10 个关键字: {', '.join(kwlist[:10])}")
    print(f"'if' 是否为关键字: {iskeyword('if')}")
    print(f"'runoob' 是否为关键字: {iskeyword('runoob')}")

    show_table(
        ("类别", "代表关键字"),
        [
            ("条件判断", "if, elif, else"),
            ("循环", "for, while, break, continue"),
            ("函数和类", "def, class, return, lambda"),
            ("异常处理", "try, except, finally, raise"),
            ("逻辑与导入", "and, or, not, import, from"),
        ],
    )


def demo_indent_and_blocks() -> None:
    """演示 Python 使用缩进表达 if/else 代码块。"""
    print("Python 用缩进表示代码块，缩进风格要统一。")
    value = 5
    if value > 3:
        print("  这里的输出属于 if 代码块")
    else:
        print("  这里的输出属于 else 代码块")


def demo_multiline_statements() -> None:
    """演示反斜杠续行和括号内自然换行两种多行语句写法。"""
    print("多行语句可以用反斜杠继续，也可以写在圆括号里。")
    total = 1 + 2 + 3 + \
        4 + 5
    print(f"反斜杠续行结果: {total}")

    total_in_parens = (
        1
        + 2
        + 3
        + 4
        + 5
    )
    print(f"圆括号续行结果: {total_in_parens}")


def demo_comments() -> None:
    """演示单行注释和多行字符串形式的说明文本。"""
    print("单行注释使用 #；多行注释通常使用多行字符串。")
    code = """\
# 这是单行注释
value = 3
text = \"\"\"这是一段多行说明\"\"\"
print(value)
print(text)
"""
    print("运行一个包含注释和多行字符串的示例：")
    exec(code, {})


def demo_numbers() -> None:
    """保留 Number 类型表，并执行 int、bool、float、complex 示例。"""
    rows = [
        ("int", "整数", "123"),
        ("bool", "布尔值", "True / False"),
        ("float", "浮点数", "3.14"),
        ("complex", "复数", "1 + 2j"),
    ]
    show_table(("类型", "说明", "示例"), rows)
    values = {
        "int": 123,
        "bool": True,
        "float": 3.14,
        "complex": 1 + 2j,
    }
    for name, value in values.items():
        print(f"{name}: {value!r} -> type={type(value).__name__}")


def demo_strings() -> None:
    """保留字符串写法表，并执行切片、拼接和重复示例。"""
    rows = [
        ("单引号", "简单字符串", "'hello'"),
        ("双引号", "简单字符串", '"world"'),
        ("三引号", "多行文本", '"""line1\\nline2"""'),
        ("原始字符串", "保留转义符号", r"r'hello\nrunoob'"),
    ]
    show_table(("写法", "说明", "示例"), rows)

    text = "Python3"
    print(f"字符串切片: {text[0:6]}")
    print(f"字符串拼接: {'Hello' + ' ' + 'Runoob'}")
    print(f"重复字符串: {'ha' * 3}")


def demo_empty_line() -> None:
    """说明空行只用于分隔逻辑区块，不影响程序执行。"""
    print("空行用于分隔逻辑区块，程序会忽略空行本身。")


def demo_input() -> None:
    """说明 input() 的用途，并用固定值模拟输入以避免脚本阻塞。"""
    print("input() 会等待用户输入。这里用一个固定值模拟，不阻塞脚本。")
    simulated_input = "Python3"
    print(f"模拟输入结果: {simulated_input}")


def demo_one_line_statements() -> None:
    """演示用分号在一行中编写多条简单语句。"""
    print("Python 允许在一行写多个语句，但通常只在简单场景使用。")
    a = 1; b = 2; c = a + b
    print(f"a={a}, b={b}, c={c}")


def demo_statement_groups() -> None:
    """演示冒号和缩进形成一个完整语句组。"""
    print("冒号后面的缩进代码块构成一个代码组。")
    condition = True
    if condition:
        print("  这是一个完整的代码组")


def demo_print() -> None:
    """演示 print 输出普通内容，以及 end 参数控制换行行为。"""
    print("print() 是最常见的输出方式。")
    print("它可以输出字符串、数字、变量和表达式结果。")
    print("同一条 print 也可以控制 end 参数：", end="")
    print("这里没有换行")


def demo_import() -> None:
    """演示 import 和 from...import 两种导入模块或对象的方式。"""
    print("import 用于导入模块。")
    print(f"sys.version: {sys.version.split()[0]}")
    print("from ... import ... 用于导入指定对象。")
    print(f"iskeyword('while') -> {iskeyword('while')}")


def demo_command_line_args() -> None:
    """演示脚本可通过 sys.argv 读取命令行参数。"""
    print("Python 脚本可以从命令行接收参数。")
    print(f"当前 sys.argv: {sys.argv}")


def main() -> None:
    """按基础语法页面顺序运行全部示例。"""
    print("Python3 基础语法")
    show_section("1. 编码")
    demo_encoding()

    show_section("2. 标识符")
    demo_identifier()

    show_section("3. 关键字")
    demo_keywords()

    show_section("4. 行和缩进")
    demo_indent_and_blocks()

    show_section("5. 多行语句")
    demo_multiline_statements()

    show_section("6. 注释")
    demo_comments()

    show_section("7. 数字(Number)")
    demo_numbers()

    show_section("8. 字符串")
    demo_strings()

    show_section("9. 空行")
    demo_empty_line()

    show_section("10. 等待用户输入")
    demo_input()

    show_section("11. 同一行显示多条语句")
    demo_one_line_statements()

    show_section("12. 多个语句构成代码组")
    demo_statement_groups()

    show_section("13. print 输出")
    demo_print()

    show_section("14. import 与 from...import")
    demo_import()

    show_section("15. 命令行参数")
    demo_command_line_args()


if __name__ == "__main__":
    main()
