"""77 Python datetime 模块

来源: https://www.runoob.com/python3/python-datetime.html
可单独运行: python 77_datetime_module.py
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 datetime 核心类、方法和格式化符号表。"""
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


def demo_core_classes() -> None:
    """保留 datetime 模块核心类表。"""
    show_table(
        ("类", "说明", "示例"),
        [
            ("datetime.date", "日期类", "date(2023, 5, 15)"),
            ("datetime.time", "时间类", "time(14, 30, 0)"),
            ("datetime.datetime", "日期时间类", "datetime(2023, 5, 15, 14, 30)"),
            ("datetime.timedelta", "时间间隔类", "timedelta(days=5)"),
            ("datetime.tzinfo", "时区信息基类", "自定义或 zoneinfo"),
        ],
    )


def demo_now_create_format() -> None:
    """执行获取当前时间、创建特定日期时间和格式化输出示例。"""
    now = datetime.now()
    print("当前时间:", now)
    specific_time = datetime(2025, 4, 22, 15, 30, 0)
    print("特定时间:", specific_time)
    print("格式化时间:", now.strftime("%Y-%m-%d %H:%M:%S"))


def demo_date_time_methods() -> None:
    """演示 date、time、datetime 常用属性和方法。"""
    current_date = date.today()
    parsed_date = date.fromisoformat("2023-05-15")
    current_time = time(14, 30, 0)
    current_datetime = datetime(2023, 5, 15, 14, 30, 0)
    print(current_date.isoformat(), current_date.year, current_date.month, current_date.day)
    print(parsed_date.weekday())
    print(current_time.hour, current_time.minute, current_time.isoformat())
    print(current_datetime.timestamp())
    print(current_datetime.date())
    print(current_datetime.time())


def demo_timedelta() -> None:
    """执行时间差、日期差和时间加减示例。"""
    now = datetime.now()
    future_time = now + timedelta(days=10)
    print("10 天后的时间:", future_time)
    d1 = date(2023, 5, 15)
    d2 = date(2023, 6, 1)
    delta = d2 - d1
    print("两个日期之间的天数差:", delta.days)
    future = datetime(2023, 5, 15, 14, 30) + timedelta(days=3, hours=2)
    print(future.strftime("%Y-%m-%d %H:%M"))


def demo_timezone() -> None:
    """演示原生 timezone 和 Python 3.9+ zoneinfo 时区转换。"""
    utc_time = datetime.now(timezone.utc)
    print("UTC:", utc_time)
    beijing_time = utc_time.astimezone(ZoneInfo("Asia/Shanghai"))
    print("上海当前时间:", beijing_time)


def demo_format_symbols() -> None:
    """保留常用 strftime 格式化符号表。"""
    show_table(
        ("符号", "说明", "示例输出"),
        [
            ("%Y", "四位年份", "2023"),
            ("%m", "两位月份", "05"),
            ("%d", "两位日", "15"),
            ("%H", "24 小时制小时", "14"),
            ("%M", "分钟", "30"),
            ("%S", "秒", "00"),
            ("%A", "完整星期名", "Monday"),
            ("%a", "缩写星期名", "Mon"),
            ("%B", "完整月份名", "May"),
            ("%b", "缩写月份名", "May"),
        ],
    )


def demo_parse_and_invalid_date() -> None:
    """演示 strptime 字符串解析和非法日期 ValueError。"""
    dt = datetime.strptime("2023-05-15 14:30", "%Y-%m-%d %H:%M")
    print(dt.year)
    try:
        date(2023, 2, 30)
    except ValueError as exc:
        print(f"非法日期: {exc.__class__.__name__}: {exc}")


def main() -> None:
    """按 datetime 页面顺序运行全部示例。"""
    print("Python datetime 模块")
    show_section("1. 核心类")
    demo_core_classes()
    show_section("2. 当前时间、创建和格式化")
    demo_now_create_format()
    show_section("3. date/time/datetime 方法")
    demo_date_time_methods()
    show_section("4. timedelta")
    demo_timedelta()
    show_section("5. 时区")
    demo_timezone()
    show_section("6. 格式化符号")
    demo_format_symbols()
    show_section("7. 解析和非法日期")
    demo_parse_and_invalid_date()


if __name__ == "__main__":
    main()
