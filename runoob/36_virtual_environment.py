"""36 Python 虚拟环境的创建

来源: https://www.runoob.com/python3/python-venv.html
可单独运行: python 36_virtual_environment.py
"""

from __future__ import annotations

import os
import sys


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的命令和目录结构说明。"""
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


def demo_why_venv() -> None:
    """保留虚拟环境用途：项目隔离、避免污染、依赖可控、安全测试。"""
    show_table(
        ("原因", "说明"),
        [
            ("项目隔离", "不同项目可使用不同版本的 Python 和第三方库"),
            ("避免污染", "安装包只影响当前环境，不污染全局 Python"),
            ("依赖可控", "requirements.txt 可记录并复现环境"),
            ("安全测试", "可以安全升级或试用新包"),
        ],
    )


def demo_create_commands() -> None:
    """保留创建虚拟环境的命令，不实际创建目录。"""
    commands = [
        "mkdir my_project && cd my_project",
        "python3 -m venv .venv",
        "python -m venv .venv",
    ]
    for command in commands:
        print(command)


def demo_directory_structure() -> None:
    """保留创建后的虚拟环境目录结构。"""
    structure = [
        ".venv/",
        "├── bin/            # Unix/Linux",
        "│   ├── activate",
        "│   ├── python",
        "│   └── pip",
        "├── Scripts/        # Windows",
        "│   ├── activate",
        "│   ├── python.exe",
        "│   └── pip.exe",
        "└── Lib/            # 安装的第三方库",
    ]
    for line in structure:
        print(line)


def demo_activate_commands() -> None:
    """保留不同平台激活虚拟环境的命令。"""
    show_table(
        ("平台", "激活命令", "验证命令"),
        [
            ("macOS/Linux", "source .venv/bin/activate", "which python"),
            ("Windows CMD/PowerShell", r".venv\Scripts\activate", "where python"),
        ],
    )
    print("当前 Python:", sys.executable)
    print("当前是否像虚拟环境:", sys.prefix != sys.base_prefix)


def demo_pip_commands() -> None:
    """保留 pip 安装、查看、升级、导出和恢复依赖命令。"""
    commands = [
        "pip install package_name",
        "pip install django==3.2.12",
        "pip install requests pandas",
        "pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple",
        "pip list",
        "pip show django",
        "pip install --upgrade pip",
        "pip freeze > requirements.txt",
        "pip install -r requirements.txt",
    ]
    for command in commands:
        print(command)


def demo_requirements_example() -> None:
    """保留 requirements.txt 示例内容。"""
    requirements = ["Django==3.2.12", "requests==2.26.0", "pandas==1.3.3"]
    for requirement in requirements:
        print(requirement)


def demo_deactivate_and_delete() -> None:
    """保留退出和删除虚拟环境的命令，并提示 .venv 不应提交。"""
    print("deactivate")
    print("macOS/Linux 删除: rm -rf .venv")
    print(r"Windows 删除: rmdir /s /q .venv")
    print("建议把 .venv/ 加入 .gitignore，只提交 requirements.txt。")
    print("当前目录:", os.getcwd())


def main() -> None:
    """按虚拟环境页面顺序运行全部示例。"""
    print("Python 虚拟环境的创建")

    show_section("1. 为什么需要虚拟环境")
    demo_why_venv()

    show_section("2. 创建命令")
    demo_create_commands()

    show_section("3. 目录结构")
    demo_directory_structure()

    show_section("4. 激活和验证")
    demo_activate_commands()

    show_section("5. pip 使用")
    demo_pip_commands()

    show_section("6. requirements.txt")
    demo_requirements_example()

    show_section("7. 退出和删除")
    demo_deactivate_and_delete()


if __name__ == "__main__":
    main()
