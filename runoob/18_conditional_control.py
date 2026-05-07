"""18 Python3 条件控制

来源: https://www.runoob.com/python3/python3-conditional-statements.html
可单独运行: python 18_conditional_control.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的关键字和操作符表。"""
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


def demo_keywords_table() -> None:
    """保留条件判断关键字表。"""
    show_table(
        ("关键字 / 函数", "说明", "示例"),
        [
            ("if", "条件为 True 时执行代码块", "if x > 0:"),
            ("elif", "多条件判断分支", "elif x == 0:"),
            ("else", "所有条件不满足时执行", "else:"),
            ("pass", "空语句，占位用", "if x > 0: pass"),
            ("match", "结构化模式匹配", "match x: case 1: ..."),
        ],
    )


def demo_basic_if() -> None:
    """执行页面中的简单 if 示例，展示 0 会被视为 False。"""
    var1 = 100
    if var1:
        print("1 - if 表达式条件为 true")
        print(var1)

    var2 = 0
    if var2:
        print("2 - if 表达式条件为 true")
        print(var2)

    print("Good bye!")


def dog_age_message(age: int) -> str:
    """复刻狗狗年龄换算示例，把 input 改为参数以便脚本可直接运行。"""
    if age <= 0:
        return "你是在逗我吧!"
    if age == 1:
        return "相当于 14 岁的人。"
    if age == 2:
        return "相当于 22 岁的人。"
    human = 22 + (age - 2) * 5
    return f"对应人类年龄: {human}"


def demo_dog_age() -> None:
    """演示 dog.py 逻辑，避免真正等待用户输入。"""
    for age in [0, 1, 2, 5]:
        print(f"狗狗年龄 {age}: {dog_age_message(age)}")


def demo_comparison_operators() -> None:
    """保留 if 常用比较操作符表，并执行 == 示例。"""
    show_table(
        ("操作符", "描述"),
        [
            ("<", "小于"),
            ("<=", "小于或等于"),
            (">", "大于"),
            (">=", "大于或等于"),
            ("==", "等于，比较两个值是否相等"),
            ("!=", "不等于"),
        ],
    )
    print(5 == 6)
    x = 5
    y = 8
    print(x == y)


def guess_number(number: int, guesses: list[int]) -> None:
    """复刻数字猜谜游戏逻辑，用预设猜测值替代 input。"""
    print("数字猜谜游戏!")
    for guess in guesses:
        print(f"请输入你猜的数字：{guess}")
        if guess == number:
            print("恭喜，你猜对了！")
            break
        if guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")


def demo_guess_number() -> None:
    """执行页面中的 high_low.py 猜数字示例。"""
    guess_number(7, [1, 9, 7])


def divisibility_message(num: int) -> str:
    """复刻嵌套 if：判断数字是否能被 2 和 3 整除。"""
    if num % 2 == 0:
        if num % 3 == 0:
            return "你输入的数字可以整除 2 和 3"
        return "你输入的数字可以整除 2，但不能整除 3"
    if num % 3 == 0:
        return "你输入的数字可以整除 3，但不能整除 2"
    return "你输入的数字不能整除 2 和 3"


def demo_nested_if() -> None:
    """执行页面中的 if 嵌套示例，覆盖多个分支。"""
    for number in [6, 4, 9, 5]:
        print(f"{number}: {divisibility_message(number)}")


def http_error(status: int) -> str:
    """复刻 match...case 示例：根据 HTTP 状态码返回描述。"""
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


def check_permission(status: int) -> str:
    """复刻一个 case 匹配多个条件的示例。"""
    match status:
        case 200:
            return "OK - 请求成功"
        case 301 | 302:
            return "Redirect - 重定向"
        case 401 | 403 | 404:
            return "Not allowed - 无权限或未找到"
        case 500 | 502 | 503:
            return "Server Error - 服务器错误"
        case _:
            return "Unknown status - 未知状态码"


def demo_match_case() -> None:
    """执行页面中的 match...case 两组状态码示例。"""
    for code in [400, 404, 418, 500]:
        print(http_error(code))
    for code in [200, 301, 403, 500, 418]:
        print(f"状态码 {code}: {check_permission(code)}")


def main() -> None:
    """按条件控制页面顺序运行全部示例。"""
    print("Python3 条件控制")

    show_section("1. 条件判断关键字")
    demo_keywords_table()

    show_section("2. if 语句")
    demo_basic_if()

    show_section("3. 狗狗年龄判断")
    demo_dog_age()

    show_section("4. 比较操作符")
    demo_comparison_operators()

    show_section("5. 数字猜谜游戏")
    demo_guess_number()

    show_section("6. if 嵌套")
    demo_nested_if()

    show_section("7. match...case")
    demo_match_case()


if __name__ == "__main__":
    main()
