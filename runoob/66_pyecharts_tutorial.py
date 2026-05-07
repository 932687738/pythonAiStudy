"""66 Python pyecharts

来源: https://www.runoob.com/python3/python-pyecharts.html
可单独运行: python 66_pyecharts_tutorial.py
"""

from __future__ import annotations

import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 pyecharts 图表类型和配置说明。"""
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


def demo_install_and_features() -> None:
    """保留 pyecharts 安装命令、特点与功能。"""
    print("pip install pyecharts")
    print("源码安装: git clone https://github.com/pyecharts/pyecharts.git")
    show_table(
        ("特点", "说明"),
        [
            ("简单易用", "提供直观友好的 API"),
            ("丰富图表", "支持折线图、柱状图、散点图、饼图、地图等"),
            ("数据格式", "支持列表、字典、Pandas DataFrame 等"),
            ("交互性", "生成图表可悬停、缩放和交互"),
            ("配置项", "可配置标题、坐标轴、图例、工具箱、提示框等"),
            ("主题", "支持 LIGHT、DARK 等主题"),
        ],
    )


def demo_chart_types() -> None:
    """保留页面中的 pyecharts 图表类型表。"""
    show_table(
        ("图表类型", "pyecharts 类", "包引入"),
        [
            ("折线图", "Line", "from pyecharts.charts import Line"),
            ("柱状图", "Bar", "from pyecharts.charts import Bar"),
            ("散点图", "Scatter", "from pyecharts.charts import Scatter"),
            ("饼图", "Pie", "from pyecharts.charts import Pie"),
            ("雷达图", "Radar", "from pyecharts.charts import Radar"),
            ("热力图", "HeatMap", "from pyecharts.charts import HeatMap"),
            ("K 线图", "Kline", "from pyecharts.charts import Kline"),
            ("箱线图", "Boxplot", "from pyecharts.charts import Boxplot"),
            ("地图", "Map", "from pyecharts.charts import Map"),
            ("词云图", "WordCloud", "from pyecharts.charts import WordCloud"),
            ("仪表盘", "Gauge", "from pyecharts.charts import Gauge"),
            ("漏斗图", "Funnel", "from pyecharts.charts import Funnel"),
            ("时间线图", "Timeline", "from pyecharts.charts import Timeline"),
            ("3D 散点图", "Scatter3D", "from pyecharts.charts import Scatter3D"),
        ],
    )


def render_simple_bar_html(path: Path) -> None:
    """生成一个无第三方依赖的等价 HTML 柱状图，模拟 pyecharts render 输出。"""
    x_data = ["一月", "二月", "三月", "四月", "五月"]
    y_data = [10, 20, 15, 25, 30]
    bars = "\n".join(
        f"<div><span>{month}</span><div style='background:#4e79a7;width:{value * 10}px;color:white'>{value}</div></div>"
        for month, value in zip(x_data, y_data)
    )
    html = f"""<!doctype html>
<html lang="zh-CN">
<meta charset="utf-8">
<title>月度销售额柱状图</title>
<body>
<h1>月度销售额柱状图</h1>
{bars}
</body>
</html>"""
    path.write_text(html, encoding="utf-8")


def demo_bar_chart() -> None:
    """保留 Bar/add_xaxis/add_yaxis/render 流程，并生成一个本地 HTML 替代文件。"""
    print("from pyecharts.charts import Bar")
    print("bar_chart = Bar()")
    print("bar_chart.add_xaxis(['一月', '二月', '三月', '四月', '五月'])")
    print("bar_chart.add_yaxis('销售额', [10, 20, 15, 25, 30])")
    print("bar_chart.render('bar_chart.html')")
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "bar_chart.html"
        render_simple_bar_html(path)
        print("生成文件:", path)
        print(path.read_text(encoding="utf-8")[:120])


def demo_global_options_and_themes() -> None:
    """保留 set_global_opts 和主题配置说明。"""
    show_table(
        ("配置项", "说明"),
        [
            ("title_opts", "标题和副标题"),
            ("xaxis_opts", "x 轴名称和样式"),
            ("yaxis_opts", "y 轴名称和样式"),
            ("legend_opts", "图例位置和样式"),
            ("toolbox_opts", "保存图片、数据视图等工具"),
            ("tooltip_opts", "提示框触发方式和样式"),
        ],
    )
    themes = ["LIGHT", "WESTEROS", "CHALK", "ESSOS", "INFOGRAPHIC", "MACARONS", "DARK", "PURPLE-PASSION", "SHINE", "VINTAGE", "ROMA", "WALDEN"]
    print("主题列表:", themes)


def main() -> None:
    """按 pyecharts 页面顺序运行全部示例。"""
    print("Python pyecharts")
    show_section("1. 安装与特点")
    demo_install_and_features()
    show_section("2. 图表类型")
    demo_chart_types()
    show_section("3. 创建第一个柱状图")
    demo_bar_chart()
    show_section("4. 全局配置和主题")
    demo_global_options_and_themes()


if __name__ == "__main__":
    main()
