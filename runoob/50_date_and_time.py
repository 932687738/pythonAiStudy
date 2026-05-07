"""50 Python3 日期和时间

来源: https://www.runoob.com/python3/python3-date-time.html
可单独运行: python 50_date_and_time.py
"""

from __future__ import annotations

import calendar
import time


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留时间格式化符号和模块函数表。"""
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


def demo_current_time() -> None:
    """复刻获取当前时间示例：time.time、localtime 和 asctime。"""
    ticks = time.time()
    print("当前时间戳为:", ticks)
    localtime = time.localtime(ticks)
    print("本地时间为 :", localtime)
    readable = time.asctime(localtime)
    print("本地时间为 :", readable)


def demo_format_time() -> None:
    """复刻 strftime 和 strptime/mktime 格式化与解析示例。"""
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    text = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(text, "%a %b %d %H:%M:%S %Y")))


def demo_format_symbols() -> None:
    """保留页面中的时间日期格式化符号表。"""
    show_table(
        ("符号", "含义"),
        [
            ("%y", "两位数年份"),
            ("%Y", "四位数年份"),
            ("%m", "月份"),
            ("%d", "月内日期"),
            ("%H", "24 小时制小时"),
            ("%I", "12 小时制小时"),
            ("%M", "分钟"),
            ("%S", "秒"),
            ("%a", "本地简化星期名称"),
            ("%A", "本地完整星期名称"),
            ("%b", "本地简化月份名称"),
            ("%B", "本地完整月份名称"),
            ("%c", "本地日期和时间"),
            ("%j", "年内第几天"),
            ("%p", "AM/PM"),
            ("%U", "一年中星期数，星期天为开始"),
            ("%w", "星期，0 为星期天"),
            ("%W", "一年中星期数，星期一为开始"),
            ("%x", "本地日期"),
            ("%X", "本地时间"),
            ("%Z", "时区名称"),
            ("%%", "百分号本身"),
        ],
    )


def demo_calendar_month() -> None:
    """复刻打印某月日历示例。"""
    cal = calendar.month(2016, 1)
    print("以下输出2016年1月份的日历:")
    print(cal)


def demo_time_module_table() -> None:
    """保留 Time 模块常用函数表，并执行代表性示例。"""
    show_table(
        ("函数/属性", "描述", "示例结果"),
        [
            ("time.altzone", "夏令时地区偏移秒数", str(time.altzone)),
            ("time.asctime()", "时间元组转可读字符串", time.asctime(time.localtime())),
            ("time.clock()", "Python3.8 已移除", "使用 time.perf_counter()"),
            ("time.ctime()", "时间戳转可读字符串", time.ctime()),
            ("time.gmtime()", "时间戳转 UTC 时间元组", str(time.gmtime(0))),
            ("time.localtime()", "时间戳转本地时间元组", str(time.localtime(0))),
            ("time.mktime()", "时间元组转时间戳", str(time.mktime(time.localtime(0)))),
            ("time.sleep()", "推迟线程运行", "本示例不等待 5 秒"),
            ("time.strftime()", "格式化时间", time.strftime("%Y-%m-%d", time.localtime())),
            ("time.strptime()", "解析时间字符串", str(time.strptime("30 Nov 00", "%d %b %y"))),
            ("time.time()", "当前时间戳", str(round(time.time(), 3))),
            ("time.tzset()", "Unix 可重置时区规则", "Windows 不一定支持"),
        ],
    )


def demo_calendar_functions() -> None:
    """保留 Calendar 模块常用函数，并执行闰年、月历、星期等示例。"""
    show_table(
        ("函数", "描述", "示例结果"),
        [
            ("calendar.calendar(year)", "返回全年日历字符串", calendar.calendar(2026)[:20] + "..."),
            ("calendar.firstweekday()", "返回每周起始日期设置", str(calendar.firstweekday())),
            ("calendar.isleap(year)", "判断是否闰年", str(calendar.isleap(2000))),
            ("calendar.leapdays(y1,y2)", "返回区间闰年数", str(calendar.leapdays(2000, 2026))),
            ("calendar.month(year,month)", "返回某月日历", calendar.month(2026, 5).splitlines()[0]),
            ("calendar.monthrange(year,month)", "返回月首星期和天数", str(calendar.monthrange(2026, 5))),
            ("calendar.weekday(year,month,day)", "返回星期几", str(calendar.weekday(2026, 5, 7))),
        ],
    )


def main() -> None:
    """按日期和时间页面顺序运行全部示例。"""
    print("Python3 日期和时间")
    show_section("1. 获取当前时间")
    demo_current_time()
    show_section("2. 格式化时间")
    demo_format_time()
    show_section("3. 格式化符号")
    demo_format_symbols()
    show_section("4. 获取某月日历")
    demo_calendar_month()
    show_section("5. Time 模块")
    demo_time_module_table()
    show_section("6. Calendar 模块")
    demo_calendar_functions()


if __name__ == "__main__":
    main()
