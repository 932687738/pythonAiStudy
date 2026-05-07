"""59 Python random

来源: https://www.runoob.com/python3/python-random.html
可单独运行: python 59_random_module.py
"""

from __future__ import annotations

import random


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 random 方法表。"""
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


def demo_dir_random() -> None:
    """保留页面中 dir(random) 查看模块内容的逻辑。"""
    names = [name for name in dir(random) if not name.startswith("_")]
    print(names)


def demo_random_seed() -> None:
    """执行 random() 和 seed() 示例，用固定种子保证输出可复现。"""
    random.seed()
    print("使用默认种子生成随机数：", random.random())
    print("使用默认种子生成随机数：", random.random())
    random.seed(10)
    print("使用整数 10 种子生成随机数：", random.random())
    random.seed(10)
    print("使用整数 10 种子生成随机数：", random.random())
    random.seed("hello", 2)
    print("使用字符串种子生成随机数：", random.random())


def demo_integer_sequence_functions() -> None:
    """演示 randint、randrange、choice、choices、sample、shuffle。"""
    random.seed(7)
    values = [1, 2, 3, 4, 5]
    shuffled = values[:]
    random.shuffle(shuffled)
    show_table(
        ("函数", "说明", "结果"),
        [
            ("randint(0,9)", "返回闭区间整数", str(random.randint(0, 9))),
            ("randrange(0,10,2)", "按步长取随机整数", str(random.randrange(0, 10, 2))),
            ("choice(seq)", "从序列随机取一个元素", str(random.choice(values))),
            ("choices(seq,k=3)", "可重复抽样", str(random.choices(values, k=3))),
            ("sample(seq,k=3)", "不重复抽样", str(random.sample(values, 3))),
            ("shuffle(seq)", "原地打乱序列", str(shuffled)),
        ],
    )


def demo_float_distributions() -> None:
    """演示 uniform、triangular 和多种概率分布函数。"""
    random.seed(7)
    show_table(
        ("函数", "说明", "结果"),
        [
            ("uniform(1,5)", "均匀分布浮点数", str(round(random.uniform(1, 5), 4))),
            ("triangular(1,5,3)", "三角分布", str(round(random.triangular(1, 5, 3), 4))),
            ("normalvariate(0,1)", "正态分布", str(round(random.normalvariate(0, 1), 4))),
            ("gauss(0,1)", "高斯分布", str(round(random.gauss(0, 1), 4))),
            ("expovariate(1.5)", "指数分布", str(round(random.expovariate(1.5), 4))),
            ("betavariate(1,3)", "Beta 分布", str(round(random.betavariate(1, 3), 4))),
            ("gammavariate(2,2)", "Gamma 分布", str(round(random.gammavariate(2, 2), 4))),
        ],
    )


def demo_state_and_bytes() -> None:
    """演示 getstate、setstate、getrandbits 和 randbytes。"""
    random.seed(7)
    state = random.getstate()
    first = random.random()
    random.setstate(state)
    second = random.random()
    print(first == second)
    print(random.getrandbits(8))
    print(random.randbytes(4))


def main() -> None:
    """按 random 页面顺序运行全部示例。"""
    print("Python random")
    show_section("1. dir(random)")
    demo_dir_random()
    show_section("2. random() 和 seed()")
    demo_random_seed()
    show_section("3. 整数和序列函数")
    demo_integer_sequence_functions()
    show_section("4. 浮点分布")
    demo_float_distributions()
    show_section("5. 状态和字节")
    demo_state_and_bytes()


if __name__ == "__main__":
    main()
