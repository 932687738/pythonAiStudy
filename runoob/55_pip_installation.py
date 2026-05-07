"""55 Python3 pip

来源: https://www.runoob.com/python3/python3-pip.html
可单独运行: python 55_pip_installation.py
"""

from __future__ import annotations

import sys


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 pip 命令说明。"""
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


def demo_pip_intro() -> None:
    """保留 pip 的作用说明和 PyPI 地址。"""
    print("pip 是 Python 包管理工具，用于查找、下载、安装、卸载 Python 包。")
    print("软件包也可以在 https://pypi.org/ 中找到。")
    print("Python 2.7.9+ 或 Python 3.4+ 通常自带 pip。")
    print("当前 Python:", sys.version.split()[0])


def demo_common_commands() -> None:
    """保留页面中的 pip 查看、安装、卸载和列出包命令。"""
    show_table(
        ("命令", "说明"),
        [
            ("pip --version", "查看是否已经安装 pip"),
            ("pip install some-package-name", "下载安装包"),
            ("pip install numpy", "安装 numpy 包示例"),
            ("pip uninstall some-package-name", "移除软件包"),
            ("pip uninstall numpy", "移除 numpy 包示例"),
            ("pip list", "查看已经安装的软件包"),
        ],
    )


def demo_requirements_commands() -> None:
    """保留 pip freeze 导出和按 requirements.txt 重建环境流程。"""
    show_table(
        ("命令", "说明"),
        [
            ("pip freeze > requirements.txt", "导出当前环境依赖及版本"),
            ("pip install -r requirements.txt", "根据依赖文件重新安装环境"),
        ],
    )
    requirements = ["requests==2.32.3", "numpy==2.1.0", "pandas==2.2.2"]
    print("requirements.txt 示例:")
    for item in requirements:
        print(item)


def demo_anaconda_note() -> None:
    """保留 Anaconda 和 conda 与 pip 的关系说明。"""
    print("Anaconda 包含 Python 解释器和大量数据科学库。")
    print("conda 更擅长环境管理和跨环境切换；pip 主要管理 Python 包。")
    print("两者都常用于 Python 项目依赖管理。")


def main() -> None:
    """按 pip 页面顺序运行全部示例。"""
    print("Python3 pip")
    show_section("1. pip 简介")
    demo_pip_intro()
    show_section("2. 常用命令")
    demo_common_commands()
    show_section("3. 导出和恢复环境")
    demo_requirements_commands()
    show_section("4. Anaconda 扩展")
    demo_anaconda_note()


if __name__ == "__main__":
    main()
