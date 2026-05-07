"""57 Python math

来源: https://www.runoob.com/python3/python-math.html
可单独运行: python 57_math_module.py
"""

from __future__ import annotations

import math


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 math 常量和函数表。"""
    widths = [len(item) for item in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def format_row(values: tuple[str, ...]) -> str:
        """格式化表格行。"""
        return " | ".join(values[index].ljust(widths[index]) for index in range(len(values)))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


def demo_dir_math() -> None:
    """保留页面中 dir(math) 查看模块内容的逻辑。"""
    names = [name for name in dir(math) if not name.startswith("_")]
    print(names)


def demo_constants() -> None:
    """保留 math 模块常量表。"""
    show_table(
        ("常量", "描述", "值"),
        [
            ("math.pi", "圆周率", str(math.pi)),
            ("math.e", "自然常数", str(math.e)),
            ("math.tau", "2π", str(math.tau)),
            ("math.inf", "正无穷大", str(math.inf)),
            ("math.nan", "非数字", str(math.nan)),
        ],
    )


def demo_number_theory() -> None:
    """演示 factorial、gcd、lcm、comb、perm、isqrt、prod 等函数。"""
    show_table(
        ("函数", "说明", "结果"),
        [
            ("factorial(5)", "阶乘", str(math.factorial(5))),
            ("gcd(12,18)", "最大公约数", str(math.gcd(12, 18))),
            ("lcm(12,18)", "最小公倍数", str(math.lcm(12, 18))),
            ("comb(5,2)", "组合数", str(math.comb(5, 2))),
            ("perm(5,2)", "排列数", str(math.perm(5, 2))),
            ("isqrt(10)", "整数平方根", str(math.isqrt(10))),
            ("prod([1,2,3,4])", "乘积", str(math.prod([1, 2, 3, 4]))),
        ],
    )


def demo_power_log() -> None:
    """演示 sqrt、pow、exp、log、log10、log2 等幂和对数函数。"""
    show_table(
        ("函数", "说明", "结果"),
        [
            ("sqrt(16)", "平方根", str(math.sqrt(16))),
            ("pow(2,3)", "幂", str(math.pow(2, 3))),
            ("exp(1)", "e 的 1 次幂", str(math.exp(1))),
            ("expm1(1)", "e**x - 1", str(math.expm1(1))),
            ("log(e)", "自然对数", str(math.log(math.e))),
            ("log10(100)", "10 为底对数", str(math.log10(100))),
            ("log2(8)", "2 为底对数", str(math.log2(8))),
        ],
    )


def demo_rounding_and_float() -> None:
    """演示 ceil、floor、trunc、fabs、fmod、modf、fsum、isclose 等函数。"""
    show_table(
        ("函数", "说明", "结果"),
        [
            ("ceil(4.1)", "向上取整", str(math.ceil(4.1))),
            ("floor(4.9)", "向下取整", str(math.floor(4.9))),
            ("trunc(4.9)", "截断小数", str(math.trunc(4.9))),
            ("fabs(-3)", "浮点绝对值", str(math.fabs(-3))),
            ("fmod(7,3)", "浮点取模", str(math.fmod(7, 3))),
            ("modf(3.14)", "小数和整数部分", str(math.modf(3.14))),
            ("fsum([0.1]*10)", "高精度求和", str(math.fsum([0.1] * 10))),
            ("isclose(0.1+0.2,0.3)", "浮点近似比较", str(math.isclose(0.1 + 0.2, 0.3))),
        ],
    )


def demo_trigonometry() -> None:
    """演示三角函数和角度/弧度转换。"""
    show_table(
        ("函数", "说明", "结果"),
        [
            ("sin(pi/2)", "正弦", str(math.sin(math.pi / 2))),
            ("cos(0)", "余弦", str(math.cos(0))),
            ("tan(pi/4)", "正切", str(round(math.tan(math.pi / 4), 10))),
            ("asin(1)", "反正弦", str(math.asin(1))),
            ("acos(1)", "反余弦", str(math.acos(1))),
            ("atan(1)", "反正切", str(math.atan(1))),
            ("atan2(1,1)", "坐标反正切", str(math.atan2(1, 1))),
            ("degrees(pi)", "弧度转角度", str(math.degrees(math.pi))),
            ("radians(180)", "角度转弧度", str(math.radians(180))),
            ("hypot(3,4)", "欧几里得距离", str(math.hypot(3, 4))),
        ],
    )


def demo_special_values() -> None:
    """演示 inf、nan 相关判断函数。"""
    print(math.isfinite(1.0))
    print(math.isinf(math.inf))
    print(math.isnan(math.nan))


def main() -> None:
    """按 math 页面顺序运行全部示例。"""
    print("Python math")
    show_section("1. dir(math)")
    demo_dir_math()
    show_section("2. 常量")
    demo_constants()
    show_section("3. 数论函数")
    demo_number_theory()
    show_section("4. 幂和对数")
    demo_power_log()
    show_section("5. 舍入和浮点")
    demo_rounding_and_float()
    show_section("6. 三角函数")
    demo_trigonometry()
    show_section("7. 特殊值")
    demo_special_values()


if __name__ == "__main__":
    main()
