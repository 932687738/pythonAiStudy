"""19 Python3 循环语句

来源: https://www.runoob.com/python3/python3-loop.html
可单独运行: python 19_loops.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的循环关键字表。"""
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


def demo_loop_keywords() -> None:
    """保留循环控制关键字与方法表。"""
    show_table(
        ("关键字 / 函数", "说明", "示例"),
        [
            ("for", "遍历序列或可迭代对象", "for i in list:"),
            ("while", "条件为 True 时持续执行", "while x > 0:"),
            ("break", "立即终止当前循环", "break"),
            ("continue", "跳过本次剩余代码", "continue"),
            ("else", "循环未被 break 时执行", "for i in range(3): ... else: ..."),
            ("pass", "占位语句", "for i in range(5): pass"),
            ("range()", "生成整数序列", "range(0, 5)"),
            ("enumerate()", "同时获取索引和值", "for i, v in enumerate(list):"),
        ],
    )


def demo_while_sum() -> None:
    """复刻 while 计算 1 到 100 之和的示例。"""
    n = 100
    total = 0
    counter = 1
    while counter <= n:
        total = total + counter
        counter += 1
    print("1 到 %d 之和为: %d" % (n, total))


def demo_infinite_loop_simulation() -> None:
    """说明无限循环示例，并用有限数据模拟 input，避免脚本阻塞。"""
    print("原页面使用 while var == 1 配合 input 形成无限循环。")
    for num in [5, 8]:
        print("你输入的数字是: ", num)
    print("Good bye!")


def demo_while_else() -> None:
    """复刻 while...else 示例：条件变为 False 后执行 else。"""
    count = 0
    while count < 5:
        print(count, " 小于 5")
        count = count + 1
    else:
        print(count, " 大于或等于 5")


def demo_simple_statement_group() -> None:
    """保留简单语句组写法，用有限循环代替页面中的无限 while。"""
    flag = 0
    while flag < 3:
        print("欢迎访问菜鸟教程!")
        flag += 1
    print("Good bye!")


def demo_for_loop() -> None:
    """复刻 for 遍历列表、字符串和 range 的示例。"""
    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        print(site)

    word = "runoob"
    for letter in word:
        print(letter)

    for number in range(1, 6):
        print(number)


def demo_for_else() -> None:
    """演示 for...else 正常结束会执行 else，遇到 break 不执行 else。"""
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")

    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        if site == "Runoob":
            print("菜鸟教程!")
            break
        print("循环数据 " + site)
    else:
        print("没有循环数据!")
    print("完成循环!")


def demo_range() -> None:
    """演示 range() 的不同参数形式，以及结合 len() 遍历索引。"""
    print(list(range(5)))
    print(list(range(5, 9)))
    print(list(range(0, 10, 3)))
    print(list(range(-10, -100, -30)))

    sites = ["Google", "Baidu", "Runoob", "Taobao", "QQ"]
    for index in range(len(sites)):
        print(index, sites[index])


def demo_break_continue() -> None:
    """复刻 break 和 continue 在 while 与 for 中的示例。"""
    n = 5
    while n > 0:
        n -= 1
        if n == 2:
            break
        print(n)
    print("循环结束。")

    n = 5
    while n > 0:
        n -= 1
        if n == 2:
            continue
        print(n)
    print("循环结束。")

    for letter in "Runoob":
        if letter == "b":
            break
        print("当前字母为 :", letter)

    for letter in "Runoob":
        if letter == "o":
            continue
        print("当前字母 :", letter)


def demo_loop_else_prime() -> None:
    """复刻循环 else 子句查询质数的示例。"""
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, "等于", x, "*", n // x)
                break
        else:
            print(n, " 是质数")


def demo_pass() -> None:
    """演示 pass 作为占位语句，不执行任何动作但保持语法完整。"""
    class MyEmptyClass:
        """页面中的最小类示例。"""
        pass

    print(MyEmptyClass)
    for letter in "Runoob":
        if letter == "o":
            pass
            print("执行 pass 块")
        print("当前字母 :", letter)
    print("Good bye!")


def demo_enumerate_note() -> None:
    """保留页面笔记中的 enumerate 遍历索引和值示例。"""
    sequence = [12, 34, 34, 23, 45, 76, 89]
    for index, item in enumerate(sequence):
        print(index, item)


def main() -> None:
    """按循环语句页面顺序运行全部示例。"""
    print("Python3 循环语句")

    show_section("1. 循环关键字与方法")
    demo_loop_keywords()

    show_section("2. while 循环")
    demo_while_sum()

    show_section("3. 无限循环模拟")
    demo_infinite_loop_simulation()

    show_section("4. while...else")
    demo_while_else()

    show_section("5. 简单语句组")
    demo_simple_statement_group()

    show_section("6. for 语句")
    demo_for_loop()

    show_section("7. for...else")
    demo_for_else()

    show_section("8. range() 函数")
    demo_range()

    show_section("9. break 和 continue")
    demo_break_continue()

    show_section("10. 循环 else 查询质数")
    demo_loop_else_prime()

    show_section("11. pass 语句")
    demo_pass()

    show_section("12. enumerate 补充")
    demo_enumerate_note()


if __name__ == "__main__":
    main()
