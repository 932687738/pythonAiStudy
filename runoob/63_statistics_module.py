"""63 Python statistics

来源: https://www.runoob.com/python3/python-statistics.html
可单独运行: python 63_statistics_module.py
"""

from __future__ import annotations

import statistics


def show_section(title: str) -> None:
    """打印章节标题，让输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 statistics 函数表。"""
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


def demo_dir_statistics() -> None:
    """保留 dir(statistics) 查看模块内容的逻辑。"""
    names = [name for name in dir(statistics) if not name.startswith("_")]
    print(names)


def demo_common_statistics() -> None:
    """执行均值、中位数、众数、方差、标准差等页面示例。"""
    data = [1, 2, 3, 4, 5]
    even_data = [1, 2, 3, 4]
    mode_data = [1, 2, 2, 3, 4]
    show_table(
        ("函数", "说明", "结果"),
        [
            ("mean(data)", "均值", str(statistics.mean(data))),
            ("median(data)", "中位数", str(statistics.median(data))),
            ("median(even_data)", "偶数长度中位数", str(statistics.median(even_data))),
            ("mode(mode_data)", "众数", str(statistics.mode(mode_data))),
            ("variance(data)", "样本方差", str(statistics.variance(data))),
            ("stdev(data)", "样本标准差", str(statistics.stdev(data))),
            ("harmonic_mean([1,2,4])", "调和平均数", str(statistics.harmonic_mean([1, 2, 4]))),
            ("geometric_mean([1,2,4])", "几何平均数", str(statistics.geometric_mean([1, 2, 4]))),
        ],
    )


def demo_other_functions() -> None:
    """执行 median_low、median_high、quantiles、pstdev、pvariance、multimode 示例。"""
    data = [1, 2, 3, 4]
    repeated = [1, 2, 2, 3, 3, 4]
    show_table(
        ("函数", "说明", "结果"),
        [
            ("median_low(data)", "低中位数", str(statistics.median_low(data))),
            ("median_high(data)", "高中位数", str(statistics.median_high(data))),
            ("quantiles([1,2,3,4,5], n=4)", "四分位数", str(statistics.quantiles([1, 2, 3, 4, 5], n=4))),
            ("pvariance([1,2,3,4,5])", "总体方差", str(statistics.pvariance([1, 2, 3, 4, 5]))),
            ("pstdev([1,2,3,4,5])", "总体标准差", str(statistics.pstdev([1, 2, 3, 4, 5]))),
            ("multimode(repeated)", "多个众数", str(statistics.multimode(repeated))),
        ],
    )


def demo_error_handling() -> None:
    """演示 statistics 在空数据上会抛出 StatisticsError。"""
    try:
        statistics.mean([])
    except statistics.StatisticsError as exc:
        print(f"StatisticsError: {exc}")


def main() -> None:
    """按 statistics 页面顺序运行全部示例。"""
    print("Python statistics")
    show_section("1. dir(statistics)")
    demo_dir_statistics()
    show_section("2. 常用统计函数")
    demo_common_statistics()
    show_section("3. 其他常用函数")
    demo_other_functions()
    show_section("4. 异常处理")
    demo_error_handling()


if __name__ == "__main__":
    main()
