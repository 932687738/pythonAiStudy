"""课程示例的命令行入口。

这个文件只负责两件事：
1. 不传章节号时，列出当前项目已经实现的全部课程章节。
2. 传入章节号时，调用对应章节模块里的 ``run()``，输出该章节的演示结果。

具体算法和业务示例都放在 ``ai_study/chapters`` 目录下，避免入口文件变得臃肿。
"""

from __future__ import annotations

import argparse
import json
from typing import Any

from ai_study.chapters import list_chapters, run_chapter


def build_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器。

    ``argparse`` 是 Python 标准库，适合做这种轻量命令行入口。
    这里没有引入额外依赖，是为了让项目在初始 Python 环境中也能运行。
    """
    parser = argparse.ArgumentParser(description="Run AI study examples by chapter.")
    parser.add_argument(
        "chapter",
        nargs="?",
        help="Chapter number to run, for example: 03. Omit it to list chapters.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available chapters.",
    )
    return parser


def print_json(value: Any) -> None:
    """以 JSON 形式打印结果。

    ``ensure_ascii=False`` 用于保留中文标题，不把中文转义成反斜杠 u 形式的编码。
    ``indent=2`` 让输出便于阅读，适合教学项目查看每一步结果。
    """
    print(json.dumps(value, ensure_ascii=False, indent=2))


def main() -> None:
    """根据用户输入决定是列出章节，还是运行某一章。"""
    args = build_parser().parse_args()

    # 没有传章节号时，默认展示目录。这样直接运行 ``python main.py`` 也有可读输出。
    if args.list or not args.chapter:
        print_json([{"chapter": key, "title": title} for key, title in list_chapters()])
        return

    # 传入章节号时，把具体执行交给章节注册表。入口不关心每章内部细节。
    print_json(run_chapter(args.chapter))


if __name__ == "__main__":
    main()
