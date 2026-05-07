"""20 Python3 编程第一步

来源: https://www.runoob.com/python3/python3-step1.html
可单独运行: python 20_first_steps.py
"""

from __future__ import annotations


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def demo_print_string() -> None:
    """复刻页面第一个示例：打印字符串。"""
    print("Hello, world!")


def demo_print_variable() -> None:
    """复刻输出变量值示例：先计算表达式，再打印变量。"""
    i = 256 * 256
    print("i 的值为：", i)


def demo_simple_math() -> None:
    """复刻定义变量并进行简单数学运算的示例。"""
    x = 3
    y = 2
    z = x + y
    print(z)


def demo_list_access() -> None:
    """复刻定义列表并按索引打印元素的示例。"""
    my_list = ["google", "runoob", "taobao"]
    print(my_list[0])
    print(my_list[1])
    print(my_list[2])


def demo_for_range() -> None:
    """复刻 for 循环打印数字 0 到 4 的示例。"""
    for index in range(5):
        print(index)


def demo_if_else() -> None:
    """复刻根据条件输出不同结果的示例。"""
    x = 6
    if x > 10:
        print("x 大于 10")
    else:
        print("x 小于或等于 10")


def demo_fibonacci_while() -> None:
    """复刻 while 版本斐波那契数列，保留同时赋值逻辑 a, b = b, a+b。"""
    a, b = 0, 1
    while b < 10:
        print(b)
        a, b = b, a + b


def demo_parallel_assignment_explanation() -> None:
    """保留页面对 a, b = b, a+b 的执行顺序解释，并用等价写法验证。"""
    a, b = 0, 1
    n = b
    m = a + b
    a = n
    b = m
    print(f"等价写法执行后: a={a}, b={b}")


def demo_fibonacci_for() -> None:
    """复刻 for 循环版本斐波那契数列。"""
    n = 10
    a, b = 0, 1
    for _ in range(n):
        print(b)
        a, b = b, a + b


def demo_print_end() -> None:
    """复刻 end 关键字示例：把斐波那契结果输出到同一行。"""
    a, b = 0, 1
    while b < 1000:
        print(b, end=",")
        a, b = b, a + b
    print()


def demo_print_sep_note() -> None:
    """保留页面笔记中的 print sep 参数示例。"""
    a = 10
    b = 388
    c = 98
    print(a, b, c, sep="@")


def recursive_fibonacci(n: int) -> int:
    """保留页面笔记中的递归斐波那契逻辑。"""
    if n < 1:
        raise ValueError("输入有误！")
    if n == 1 or n == 2:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def demo_recursive_fibonacci_note() -> None:
    """执行递归方式求斐波那契数列的补充示例。"""
    for number in [1, 2, 6]:
        print(f"recursive_fibonacci({number}) -> {recursive_fibonacci(number)}")


def main() -> None:
    """按编程第一步页面顺序运行全部示例。"""
    print("Python3 编程第一步")

    show_section("1. 打印字符串")
    demo_print_string()

    show_section("2. 输出变量值")
    demo_print_variable()

    show_section("3. 简单数学运算")
    demo_simple_math()

    show_section("4. 列表元素访问")
    demo_list_access()

    show_section("5. for 循环")
    demo_for_range()

    show_section("6. 条件判断")
    demo_if_else()

    show_section("7. while 斐波那契")
    demo_fibonacci_while()

    show_section("8. 同时赋值解释")
    demo_parallel_assignment_explanation()

    show_section("9. for 斐波那契")
    demo_fibonacci_for()

    show_section("10. print end 参数")
    demo_print_end()

    show_section("11. print sep 参数补充")
    demo_print_sep_note()

    show_section("12. 递归斐波那契补充")
    demo_recursive_fibonacci_note()


if __name__ == "__main__":
    main()
