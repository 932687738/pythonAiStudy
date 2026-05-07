"""32 Python3 OS

来源: https://www.runoob.com/python3/python3-os-file-methods.html
可单独运行: python 32_os_module.py
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留页面中的 os 常用功能表。"""
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


def demo_os_functions_table() -> None:
    """保留 os 模块常用功能列表。"""
    show_table(
        ("函数", "描述"),
        [
            ("os.getcwd()", "获取当前工作目录"),
            ("os.chdir(path)", "改变当前工作目录"),
            ("os.listdir(path)", "列出目录内容"),
            ("os.mkdir(path)", "创建目录"),
            ("os.makedirs(path)", "递归创建目录"),
            ("os.remove(path)", "删除文件"),
            ("os.rmdir(path)", "删除空目录"),
            ("os.rename(src, dst)", "重命名文件或目录"),
            ("os.path.exists(path)", "判断路径是否存在"),
            ("os.path.isfile(path)", "判断是否为文件"),
            ("os.path.isdir(path)", "判断是否为目录"),
            ("os.path.join(...)", "拼接路径"),
            ("os.environ", "访问环境变量"),
            ("os.system(cmd)", "执行系统命令"),
        ],
    )


def demo_getcwd_chdir_listdir() -> None:
    """演示获取当前目录、切换目录和列出目录内容。"""
    original = os.getcwd()
    print("当前工作目录:", original)
    with tempfile.TemporaryDirectory() as directory:
        Path(directory, "sample.txt").write_text("Runoob", encoding="utf-8")
        os.chdir(directory)
        print("新的工作目录:", os.getcwd())
        print("目录内容:", os.listdir("."))
    os.chdir(original)
    print("恢复工作目录:", os.getcwd())


def demo_create_and_remove_directory() -> None:
    """演示 mkdir、makedirs、rmdir 删除空目录。"""
    with tempfile.TemporaryDirectory() as directory:
        single = Path(directory) / "single"
        nested = Path(directory) / "a" / "b" / "c"
        os.mkdir(single)
        os.makedirs(nested)
        print(os.listdir(directory))
        os.rmdir(single)
        os.rmdir(nested)
        print("删除部分目录后:", os.listdir(directory))


def demo_file_remove_and_rename() -> None:
    """演示 remove 删除文件和 rename 重命名文件。"""
    with tempfile.TemporaryDirectory() as directory:
        old_path = Path(directory) / "old.txt"
        new_path = Path(directory) / "new.txt"
        old_path.write_text("Runoob", encoding="utf-8")
        os.rename(old_path, new_path)
        print("重命名后存在:", new_path.exists())
        os.remove(new_path)
        print("删除后存在:", new_path.exists())


def demo_os_path() -> None:
    """演示 os.path 中的路径拼接、存在性判断、文件/目录判断和拆分。"""
    with tempfile.TemporaryDirectory() as directory:
        file_path = os.path.join(directory, "runoob.txt")
        Path(file_path).write_text("Runoob", encoding="utf-8")
        print("路径:", file_path)
        print("exists:", os.path.exists(file_path))
        print("isfile:", os.path.isfile(file_path))
        print("isdir:", os.path.isdir(directory))
        print("basename:", os.path.basename(file_path))
        print("dirname:", os.path.dirname(file_path))
        print("splitext:", os.path.splitext(file_path))


def demo_environment_variables() -> None:
    """演示读取和设置环境变量。"""
    print("PATH 是否存在:", "PATH" in os.environ)
    old_value = os.environ.get("RUNOOB_DEMO")
    os.environ["RUNOOB_DEMO"] = "Python3"
    print("RUNOOB_DEMO:", os.environ["RUNOOB_DEMO"])
    if old_value is None:
        del os.environ["RUNOOB_DEMO"]
    else:
        os.environ["RUNOOB_DEMO"] = old_value


def demo_system_note() -> None:
    """说明 os.system 可执行系统命令，这里使用跨平台且无副作用的 echo 示例。"""
    exit_code = os.system("echo Runoob OS demo")
    print("命令退出码:", exit_code)


def main() -> None:
    """按 OS 文件/目录方法页面顺序运行全部示例。"""
    print("Python3 OS")

    show_section("1. os 常用功能表")
    demo_os_functions_table()

    show_section("2. getcwd、chdir、listdir")
    demo_getcwd_chdir_listdir()

    show_section("3. 创建和删除目录")
    demo_create_and_remove_directory()

    show_section("4. 删除和重命名文件")
    demo_file_remove_and_rename()

    show_section("5. os.path")
    demo_os_path()

    show_section("6. 环境变量")
    demo_environment_variables()

    show_section("7. os.system")
    demo_system_note()


if __name__ == "__main__":
    main()
