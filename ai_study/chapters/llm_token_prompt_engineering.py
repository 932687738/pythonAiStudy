"""第 8 课：大模型基础、Token 与 Prompt Engineering。

这里不调用真实模型，而是实现 Prompt 组织、粗略 token 估算和质量检查。
这些是接入任意大模型 API 前都应该先做好的工程基本功。
"""

from __future__ import annotations

TITLE = "LLM token and prompt engineering"


def rough_token_count(text: str) -> int:
    """粗略估算 token 数。

    真正的 token 数需要使用对应模型的 tokenizer。
    这里用“英文按词、中文按字符”的简化策略，只用于帮助理解输入长度会影响成本和上下文窗口。
    """
    ascii_words = text.replace("\n", " ").split()
    non_ascii = sum(1 for char in text if ord(char) > 127)
    return len(ascii_words) + non_ascii


def build_prompt(task: str, context: str, output_format: str) -> str:
    """构造结构化 Prompt。

    一个稳定 Prompt 通常至少包含任务、上下文和输出格式。
    这比把所有内容随意拼成一句话更容易复用、测试和迭代。
    """
    return (
        f"Task:\n{task}\n\n"
        f"Context:\n{context}\n\n"
        f"Output format:\n{output_format}\n\n"
        "Answer only with information supported by the context."
    )


def prompt_quality_checks(prompt: str) -> dict[str, bool]:
    """检查 Prompt 是否包含关键段落。

    这是非常轻量的规则检查，但能演示 Prompt 工程里的“可测试”思想。
    """
    lower = prompt.lower()
    return {
        "has_task": "task:" in lower,
        "has_context": "context:" in lower,
        "has_output_format": "output format:" in lower,
    }


def run() -> dict[str, object]:
    """运行第 8 课演示：构造 Prompt 并估算 token。"""
    prompt = build_prompt("Summarize the policy", "Refunds are allowed within 7 days.", "three bullets")
    return {"title": TITLE, "tokens": rough_token_count(prompt), "checks": prompt_quality_checks(prompt)}
