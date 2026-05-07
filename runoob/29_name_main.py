"""29 Python __name__

来源: https://www.runoob.com/python3/python3-name-main.html
可单独运行: python 29_name_main.py
"""

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def greet() -> None:
    """页面 example.py 中的 greet 函数。"""
    print("来自 example 模块的问候！")


def demo_current_name() -> None:
    """展示当前脚本直接运行时 __name__ 的值。"""
    print(f"当前文件中的 __name__ 值: {__name__}")
    if __name__ == "__main__":
        print("当前文件作为主程序运行。")


def demo_main_guard_pattern() -> None:
    """保留 if __name__ == '__main__': main() 的常见模式说明和逻辑。"""
    print("常见模式:")
    print('if __name__ == "__main__":')
    print("    main()")
    print("该代码块只会在模块直接运行时执行。")


def demo_imported_module_name() -> None:
    """动态创建 example.py 并导入，复刻直接运行和被导入时的差异。"""
    source = '''\
def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")
'''
    with tempfile.TemporaryDirectory() as directory:
        module_path = Path(directory) / "example.py"
        module_path.write_text(source, encoding="utf-8")
        spec = importlib.util.spec_from_file_location("example", module_path)
        if spec is None or spec.loader is None:
            raise RuntimeError("无法创建模块加载器")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.greet()
        print(f"导入模块的 __name__: {module.__name__}")


def demo_summary() -> None:
    """保留页面总结要点。"""
    points = [
        "__name__ 是内置变量，表示当前模块名称。",
        "模块作为主程序运行时，__name__ 的值是 '__main__'。",
        "模块被导入时，__name__ 的值是模块名。",
        "使用 if __name__ == '__main__' 可避免导入时执行脚本入口代码。",
    ]
    for point in points:
        print(point)


def main() -> None:
    """按 __name__ 页面顺序运行全部示例。"""
    print("Python __name__ 与 __main__")

    show_section("1. 当前模块 __name__")
    demo_current_name()

    show_section("2. main guard 模式")
    demo_main_guard_pattern()

    show_section("3. 导入模块时的 __name__")
    demo_imported_module_name()

    show_section("4. 总结")
    demo_summary()


if __name__ == "__main__":
    main()
