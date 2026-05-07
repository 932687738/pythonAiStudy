"""60 Python OpenAI

来源: https://www.runoob.com/python3/python-openai.html
可单独运行: python 60_openai_tutorial.py
"""

from __future__ import annotations

import asyncio
import base64
import json
import os
import tempfile
from pathlib import Path


def show_section(title: str) -> None:
    """打印章节标题，让运行输出按页面小节分组。"""
    print()
    print(title)
    print("-" * len(title))


def show_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """用纯文本表格保留 OpenAI 参数和功能说明。"""
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


class FakeResponse:
    """模拟 OpenAI SDK 响应对象。"""

    def __init__(self, output_text: str) -> None:
        """保存模型输出文本。"""
        self.output_text = output_text


class FakeResponses:
    """模拟 client.responses 资源。"""

    def create(self, **kwargs) -> FakeResponse:
        """模拟 responses.create，返回组合后的文本。"""
        return FakeResponse("模拟响应: " + str(kwargs.get("input", "")))


class FakeImages:
    """模拟 client.images 资源。"""

    def generate(self, **kwargs) -> dict[str, object]:
        """模拟图像生成接口。"""
        return {"data": [{"url": "https://example.com/fake-image.png"}], "request": kwargs}


class FakeEmbeddings:
    """模拟 client.embeddings 资源。"""

    def create(self, **kwargs) -> dict[str, object]:
        """模拟嵌入接口。"""
        return {"data": [{"embedding": [0.1, 0.2, 0.3]}], "request": kwargs}


class FakeOpenAI:
    """模拟 OpenAI 客户端，避免真实 API 调用和 API Key 依赖。"""

    def __init__(self, api_key: str | None = None, **kwargs) -> None:
        """保存客户端配置并挂载资源对象。"""
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY")
        self.options = kwargs
        self.responses = FakeResponses()
        self.images = FakeImages()
        self.embeddings = FakeEmbeddings()


def demo_install_and_features() -> None:
    """保留安装方式、环境要求和主要功能列表。"""
    print("pip install openai")
    print("pip3 install openai")
    show_table(
        ("功能", "说明"),
        [
            ("文本生成", "生成文章、代码、摘要、对话等"),
            ("图像生成", "根据文本描述创建图像"),
            ("Embeddings", "将文本转换成向量表示"),
            ("语音转文本", "将音频文件转录成文本"),
            ("微调", "基于自有数据训练更有针对性的模型"),
            ("Assistants API", "构建可调用工具和长期交互的应用"),
        ],
    )


def demo_basic_responses() -> None:
    """复刻 OpenAI 客户端初始化和 responses.create 文本生成示例。"""
    client = FakeOpenAI(api_key="你申请的 API key")
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a coding assistant that talks like a pirate.",
        input="How do I check if a Python object is an instance of a class?",
    )
    print(response.output_text)
    show_table(
        ("参数名", "是否必填", "类型", "作用说明"),
        [
            ("api_key", "是", "str", "申请的 OpenAI key"),
            ("model", "是", "str", "指定使用的模型"),
            ("instructions", "否", "str", "系统级指令"),
            ("input", "是", "str/list", "用户输入内容"),
        ],
    )


def demo_vision_payloads() -> None:
    """保留图片 URL 输入和 Base64 图片输入请求结构。"""
    client = FakeOpenAI()
    prompt = "What is in this image?"
    img_url = "https://example.com/image.png"
    response = client.responses.create(
        model="gpt-5.2",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url": img_url},
                ],
            }
        ],
    )
    print(response.output_text)
    with tempfile.TemporaryDirectory() as directory:
        image_path = Path(directory) / "image.png"
        image_path.write_bytes(b"fake image bytes")
        b64_image = base64.b64encode(image_path.read_bytes()).decode("utf-8")
        payload = {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"}
        print(payload)


async def fake_async_response() -> str:
    """模拟 AsyncOpenAI 的 await 调用。"""
    await asyncio.sleep(0)
    return "模拟异步响应"


def demo_async_usage() -> None:
    """保留异步调用结构，用本地 coroutine 模拟 API 调用。"""
    print(asyncio.run(fake_async_response()))
    print("pip install openai[aiohttp]")


def demo_reference_operations() -> None:
    """保留参考手册中的文本、图像、嵌入、文件和微调请求形状。"""
    client = FakeOpenAI(timeout=30, max_retries=2)
    text_response = client.responses.create(model="gpt-5.2", input="用一句话解释什么是 Python")
    image_response = client.images.generate(model="gpt-image-1", prompt="一只在写代码的猫", size="1024x1024")
    embedding_response = client.embeddings.create(model="text-embedding-3-small", input="Hello world")
    examples = {
        "text": text_response.output_text,
        "image": image_response,
        "embedding": embedding_response,
        "files_create": {"file": "data.jsonl", "purpose": "fine-tune"},
        "fine_tuning_job": {"training_file": "file-xxx", "model": "gpt-3.5-turbo"},
    }
    print(json.dumps(examples, ensure_ascii=False, indent=2))


def main() -> None:
    """按 OpenAI 页面顺序运行全部示例。"""
    print("Python OpenAI")
    show_section("1. 安装和主要功能")
    demo_install_and_features()
    show_section("2. Responses API")
    demo_basic_responses()
    show_section("3. Vision 输入")
    demo_vision_payloads()
    show_section("4. 异步使用")
    demo_async_usage()
    show_section("5. 参考手册请求形状")
    demo_reference_operations()


if __name__ == "__main__":
    main()
