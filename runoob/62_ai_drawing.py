"""62 Python AI 绘画

来源: https://www.runoob.com/python3/python-ai-drawing.html
可单独运行: python 62_ai_drawing.py
"""

from __future__ import annotations

import base64
import json
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 AI 绘画流程。"""
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


def demo_ai_drawing_flow() -> None:
    """保留 AI 绘画的一般流程：准备提示词、调用模型、保存图片。"""
    show_table(
        ("步骤", "说明"),
        [
            ("准备 API Key", "真实调用需要平台密钥"),
            ("安装依赖", "pip install openai 或对应图像模型 SDK"),
            ("编写 prompt", "描述图片主体、风格、尺寸和细节"),
            ("调用接口", "发送 prompt 并获取图片 URL 或 base64"),
            ("保存图片", "把返回内容写入本地文件"),
        ],
    )


def build_image_request(prompt: str, size: str = "1024x1024") -> dict[str, object]:
    """构造图像生成请求体，保留页面中根据文本生成图片的核心逻辑。"""
    return {
        "model": "gpt-image-1",
        "prompt": prompt,
        "size": size,
        "response_format": "b64_json",
    }


def demo_generate_payload() -> None:
    """执行图像生成请求体构造示例，不发起真实网络请求。"""
    payload = build_image_request("一只正在学习 Python 的机器人，赛博朋克风格")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def demo_save_base64_image() -> None:
    """模拟保存接口返回的 base64 图片数据，生成一个可写入文件。"""
    fake_png_header = b"\x89PNG\r\n\x1a\n"
    b64_json = base64.b64encode(fake_png_header).decode("utf-8")
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "ai_drawing.png"
        path.write_bytes(base64.b64decode(b64_json))
        print("保存路径:", path)
        print("文件大小:", path.stat().st_size)


def demo_prompt_examples() -> None:
    """保留提示词示例，方便理解 AI 绘画输入重点。"""
    prompts = [
        "中国水墨风格的山水画，薄雾，清晨光线",
        "未来城市中的 Python 程序员，电影感，超写实",
        "可爱的机器人在黑板前解释递归，儿童绘本风",
    ]
    for prompt in prompts:
        print(prompt)


def main() -> None:
    """按 AI 绘画页面顺序运行全部示例。"""
    print("Python AI 绘画")
    show_section("1. AI 绘画流程")
    demo_ai_drawing_flow()
    show_section("2. 构造请求体")
    demo_generate_payload()
    show_section("3. 保存 base64 图片")
    demo_save_base64_image()
    show_section("4. prompt 示例")
    demo_prompt_examples()


if __name__ == "__main__":
    main()
