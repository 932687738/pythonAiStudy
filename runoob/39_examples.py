"""39 Python3 实例

来源: https://www.runoob.com/python3/python3-examples.html
可单独运行: python 39_examples.py
"""

from __future__ import annotations

import calendar
import math
import random
import re
from datetime import date, datetime, timedelta
from functools import reduce


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留实例页目录信息。"""
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


def demo_examples_catalog() -> None:
    """保留页面实例目录，方便按主题理解后续示例覆盖范围。"""
    rows = [
        ("基础", "Hello World、数字求和、平方根、二次方程、三角形/圆面积"),
        ("判断", "if、数字字符串、奇偶、闰年、最大值、质数"),
        ("循环", "范围素数、阶乘、九九乘法表、斐波那契、阿姆斯特朗数"),
        ("转换", "进制转换、ASCII 与字符转换、温度转换、时间转换"),
        ("算法", "最大公约数、最小公倍数、二分查找、线性查找、排序"),
        ("列表", "求和、求积、翻转、去重、复制、最大最小、计数"),
        ("字符串", "判断、大小写、删除指定位置字符、子串、长度、反转、URL 提取"),
        ("字典", "排序、求值之和、删除键值对、合并字典"),
        ("应用", "简单计算器、日历、文件 IO、秒表、任务清单、银行系统"),
    ]
    show_table(("分类", "页面实例"), rows)


def demo_basic_math_examples() -> None:
    """执行页面基础实例：求和、平方根、二次方程、三角形面积、圆面积和随机数。"""
    print("Hello World!")
    print("数字求和:", 1.5 + 6.3)
    print("平方根:", math.sqrt(8))

    a, b, c = 1, 5, 6
    discriminant = b**2 - 4 * a * c
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("二次方程根:", root1, root2)

    side_a, side_b, side_c = 5, 6, 7
    semi = (side_a + side_b + side_c) / 2
    area = math.sqrt(semi * (semi - side_a) * (semi - side_b) * (semi - side_c))
    print("三角形面积:", area)
    print("圆面积:", math.pi * 3**2)

    random.seed(7)
    print("随机数:", random.randint(0, 9))


def demo_conversion_and_swap() -> None:
    """执行温度转换、交换变量、进制转换和 ASCII 转换示例。"""
    celsius = 37.5
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} 摄氏度转为华氏温度为 {fahrenheit}")

    x, y = 5, 10
    x, y = y, x
    print("交换后 x,y:", x, y)

    decimal = 344
    print(bin(decimal), oct(decimal), hex(decimal))
    print("A ->", ord("A"))
    print("65 ->", chr(65))


def is_number(value: str) -> bool:
    """判断字符串是否可以转换为数字。"""
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_leap_year(year: int) -> bool:
    """判断闰年。"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_prime(number: int) -> bool:
    """判断一个数字是否为质数。"""
    if number <= 1:
        return False
    for factor in range(2, int(math.sqrt(number)) + 1):
        if number % factor == 0:
            return False
    return True


def demo_judgement_examples() -> None:
    """执行数字判断、奇偶、闰年、最大值、质数和范围素数示例。"""
    print("is_number('123.4'):", is_number("123.4"))
    number = 7
    print("奇偶:", "偶数" if number % 2 == 0 else "奇数")
    print("闰年:", is_leap_year(2024))
    print("最大值:", max(10, 14, 12))
    print("17 是否质数:", is_prime(17))
    print("10 到 30 内的素数:", [item for item in range(10, 31) if is_prime(item)])


def factorial(number: int) -> int:
    """计算阶乘。"""
    return 1 if number <= 1 else number * factorial(number - 1)


def fibonacci(limit: int) -> list[int]:
    """生成小于 limit 的斐波那契数列。"""
    result: list[int] = []
    a, b = 0, 1
    while b < limit:
        result.append(b)
        a, b = b, a + b
    return result


def is_armstrong(number: int) -> bool:
    """判断阿姆斯特朗数。"""
    digits = [int(char) for char in str(number)]
    power = len(digits)
    return number == sum(digit**power for digit in digits)


def demo_loop_examples() -> None:
    """执行阶乘、九九乘法表、斐波那契和阿姆斯特朗数示例。"""
    print("5!:", factorial(5))
    for i in range(1, 4):
        row = []
        for j in range(1, i + 1):
            row.append(f"{j}x{i}={i*j}")
        print(" ".join(row))
    print("斐波那契:", fibonacci(100))
    print("153 是否阿姆斯特朗数:", is_armstrong(153))


def gcd(a: int, b: int) -> int:
    """使用欧几里得算法计算最大公约数。"""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """计算最小公倍数。"""
    return abs(a * b) // gcd(a, b)


def simple_calculator(a: float, b: float, operator: str) -> float:
    """实现简单计算器。"""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b
    raise ValueError("未知运算符")


def demo_algorithm_examples() -> None:
    """执行最大公约数、最小公倍数、简单计算器和日历示例。"""
    print("gcd(54, 24):", gcd(54, 24))
    print("lcm(4, 6):", lcm(4, 6))
    print("计算器 10 / 2:", simple_calculator(10, 2, "/"))
    print(calendar.month(2026, 5))


def demo_list_string_dict_examples() -> None:
    """执行列表、字符串和字典相关实例。"""
    values = [1, 2, 3, 4]
    print("数组元素之和:", sum(values))
    print("数组元素之积:", reduce(lambda a, b: a * b, values))
    print("翻转列表:", list(reversed(values)))
    print("去重:", list(dict.fromkeys([1, 2, 2, 3])))
    print("元素 3 是否存在:", 3 in values)

    text = "https://www.runoob.com/python3/"
    print("字符串反转:", text[::-1])
    print("包含 runoob:", "runoob" in text)
    print("URL 提取:", re.findall(r"https?://[^\s]+", f"visit {text} now"))

    dictionary = {"a": 3, "b": 1, "c": 2}
    print("按键排序:", dict(sorted(dictionary.items())))
    print("按值排序:", dict(sorted(dictionary.items(), key=lambda item: item[1])))
    print("字典值之和:", sum(dictionary.values()))
    merged = dictionary | {"d": 4}
    print("合并字典:", merged)


def binary_search(values: list[int], target: int) -> int:
    """二分查找，返回目标索引，找不到返回 -1。"""
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def quick_sort(values: list[int]) -> list[int]:
    """快速排序。"""
    if len(values) <= 1:
        return values
    pivot = values[0]
    left = [item for item in values[1:] if item <= pivot]
    right = [item for item in values[1:] if item > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def demo_search_sort_examples() -> None:
    """执行二分查找、线性查找、快速排序和冒泡排序代表示例。"""
    values = [1, 3, 5, 7, 9]
    print("二分查找 7:", binary_search(values, 7))
    print("线性查找 5:", values.index(5) if 5 in values else -1)
    print("快速排序:", quick_sort([3, 6, 1, 8, 2]))
    bubble = [64, 34, 25, 12]
    for i in range(len(bubble)):
        for j in range(0, len(bubble) - i - 1):
            if bubble[j] > bubble[j + 1]:
                bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
    print("冒泡排序:", bubble)


def demo_date_time_examples() -> None:
    """执行时间字符串、时间戳、昨天日期和每月天数示例。"""
    moment = datetime.strptime("2026-05-07 12:00:00", "%Y-%m-%d %H:%M:%S")
    print("时间戳:", int(moment.timestamp()))
    print("格式化:", datetime.fromtimestamp(moment.timestamp()).strftime("%Y-%m-%d"))
    print("昨天:", date.today() - timedelta(days=1))
    print("2026 年 5 月天数:", calendar.monthrange(2026, 5)[1])


def main() -> None:
    """按实例页主题运行一组代表性可执行示例。"""
    print("Python3 实例")
    show_section("1. 实例目录")
    demo_examples_catalog()
    show_section("2. 基础数学")
    demo_basic_math_examples()
    show_section("3. 转换和变量交换")
    demo_conversion_and_swap()
    show_section("4. 判断类实例")
    demo_judgement_examples()
    show_section("5. 循环类实例")
    demo_loop_examples()
    show_section("6. 算法类实例")
    demo_algorithm_examples()
    show_section("7. 列表、字符串和字典")
    demo_list_string_dict_examples()
    show_section("8. 查找和排序")
    demo_search_sort_examples()
    show_section("9. 日期时间")
    demo_date_time_examples()


if __name__ == "__main__":
    main()
