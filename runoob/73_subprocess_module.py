"""73 Python subprocess 模块

来源: https://www.runoob.com/python3/python-subprocess.html
可单独运行: python 73_subprocess_module.py
"""

from __future__ import annotations

import subprocess
import sys


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 subprocess 方法、属性和参数表。"""
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


def demo_core_methods_table() -> None:
    """保留 subprocess 核心方法表。"""
    show_table(
        ("方法", "说明", "示例"),
        [
            ("subprocess.run()", "执行命令并等待完成，推荐使用", "subprocess.run([...])"),
            ("subprocess.Popen()", "创建子进程，底层控制", "subprocess.Popen([...])"),
            ("subprocess.call()", "执行命令并返回退出码", "subprocess.call([...])"),
            ("subprocess.check_call()", "失败时抛出异常", "subprocess.check_call([...])"),
            ("subprocess.check_output()", "执行命令并返回输出", "subprocess.check_output([...])"),
        ],
    )


def demo_run_capture_output() -> None:
    """执行 subprocess.run 捕获输出示例，使用当前 Python 保持跨平台。"""
    result = subprocess.run([sys.executable, "-c", "print('Hello')"], capture_output=True, text=True)
    print("args:", result.args)
    print("returncode:", result.returncode)
    print("stdout:", result.stdout.strip())
    print("stderr:", result.stderr.strip())


def demo_input_output() -> None:
    """演示向子进程传入标准输入并读取标准输出。"""
    code = "import sys; data=sys.stdin.read(); print(data.upper())"
    result = subprocess.run([sys.executable, "-c", code], input="hello\npython", capture_output=True, text=True)
    print(result.stdout.strip())


def demo_error_handling() -> None:
    """演示 check=True 时非零退出码会抛出 CalledProcessError。"""
    try:
        subprocess.run([sys.executable, "-c", "import sys; sys.exit(2)"], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with return code {exc.returncode}")


def demo_popen_communicate() -> None:
    """演示 Popen 和 communicate 获取输出。"""
    process = subprocess.Popen([sys.executable, "-c", "print('Popen demo')"], stdout=subprocess.PIPE, text=True)
    output, _ = process.communicate()
    print(output.strip())
    print("returncode:", process.returncode)


def demo_timeout() -> None:
    """演示 timeout 超时控制。"""
    try:
        subprocess.run([sys.executable, "-c", "import time; time.sleep(2)"], timeout=0.1)
    except subprocess.TimeoutExpired:
        print("命令超时！")


def demo_parameters_table() -> None:
    """保留 run/Popen 常用参数表。"""
    show_table(
        ("参数", "说明", "示例值"),
        [
            ("args", "命令参数", "['python', '-V']"),
            ("stdin", "标准输入配置", "subprocess.PIPE"),
            ("stdout", "标准输出配置", "subprocess.PIPE"),
            ("stderr", "标准错误配置", "subprocess.STDOUT"),
            ("shell", "是否通过 Shell 执行", "False"),
            ("cwd", "子进程工作目录", "'.'"),
            ("env", "自定义环境变量", "{'PATH': '...'}"),
            ("timeout", "超时时间", "30"),
            ("text", "输入输出是否为字符串", "True"),
        ],
    )


def main() -> None:
    """按 subprocess 页面顺序运行全部示例。"""
    print("Python subprocess 模块")
    show_section("1. 核心方法")
    demo_core_methods_table()
    show_section("2. run 捕获输出")
    demo_run_capture_output()
    show_section("3. 输入输出")
    demo_input_output()
    show_section("4. 错误处理")
    demo_error_handling()
    show_section("5. Popen")
    demo_popen_communicate()
    show_section("6. timeout")
    demo_timeout()
    show_section("7. 常用参数")
    demo_parameters_table()


if __name__ == "__main__":
    main()
