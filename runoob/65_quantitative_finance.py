"""65 Python 量化

来源: https://www.runoob.com/python3/python-qt.html
可单独运行: python 65_quantitative_finance.py
"""

from __future__ import annotations

from statistics import mean


def show_section(title: str) -> None:
    """打印章节标题，让输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留量化交易流程和策略结果。"""
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


def demo_quant_intro() -> None:
    """保留 Python 量化的定义、常用库和移动平均策略说明。"""
    show_table(
        ("主题", "说明"),
        [
            ("定义", "利用 Python 进行金融市场数据分析、策略开发和交易执行"),
            ("优势", "语法简洁、生态丰富、适合数据分析"),
            ("常用库", "pandas, yfinance, matplotlib"),
            ("示例策略", "短期均线突破长期均线买入，跌破卖出"),
            ("安装命令", "pip install pandas yfinance matplotlib"),
        ],
    )


def moving_average(values: list[float], window: int) -> list[float | None]:
    """计算移动平均线，前 window-1 个位置返回 None。"""
    result: list[float | None] = []
    for index in range(len(values)):
        if index + 1 < window:
            result.append(None)
        else:
            result.append(mean(values[index + 1 - window : index + 1]))
    return result


def generate_signals(prices: list[float], short_window: int, long_window: int) -> list[str]:
    """根据短期均线和长期均线生成买入、卖出、持有信号。"""
    short_ma = moving_average(prices, short_window)
    long_ma = moving_average(prices, long_window)
    signals: list[str] = []
    previous = "HOLD"
    for short, long in zip(short_ma, long_ma):
        if short is None or long is None:
            signals.append("HOLD")
            continue
        current = "BUY" if short > long else "SELL"
        signals.append(current if current != previous else "HOLD")
        previous = current
    return signals


def demo_moving_average_strategy() -> None:
    """执行移动平均策略示例，不依赖 pandas/yfinance/matplotlib。"""
    prices = [10, 10.5, 10.8, 10.6, 11, 11.4, 11.1, 10.9, 10.7, 11.2, 11.8, 12.1]
    short_ma = moving_average(prices, 3)
    long_ma = moving_average(prices, 5)
    signals = generate_signals(prices, 3, 5)
    rows = []
    for index, price in enumerate(prices):
        rows.append(
            (
                str(index + 1),
                str(price),
                "-" if short_ma[index] is None else f"{short_ma[index]:.2f}",
                "-" if long_ma[index] is None else f"{long_ma[index]:.2f}",
                signals[index],
            )
        )
    show_table(("日序号", "收盘价", "短期均线", "长期均线", "信号"), rows)


def demo_backtest() -> None:
    """用简单资金模型演示买入卖出回测逻辑。"""
    prices = [10, 10.5, 10.8, 10.6, 11, 11.4, 11.1, 10.9, 10.7, 11.2, 11.8, 12.1]
    signals = generate_signals(prices, 3, 5)
    cash = 1000.0
    shares = 0.0
    for price, signal in zip(prices, signals):
        if signal == "BUY" and cash > 0:
            shares = cash / price
            cash = 0
        elif signal == "SELL" and shares > 0:
            cash = shares * price
            shares = 0
    final_value = cash + shares * prices[-1]
    print(f"最终资产: {final_value:.2f}")


def main() -> None:
    """按 Python 量化页面顺序运行全部示例。"""
    print("Python 量化")
    show_section("1. 量化简介")
    demo_quant_intro()
    show_section("2. 移动平均策略")
    demo_moving_average_strategy()
    show_section("3. 简单回测")
    demo_backtest()


if __name__ == "__main__":
    main()
