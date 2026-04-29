"""第 24 课：LLM 推理系统优化。

本章关注 KV Cache、量化和投机解码。
这些技术直接影响长上下文推理的显存、吞吐和延迟。
"""

from __future__ import annotations

TITLE = "Advanced LLM inference systems"


def kv_cache_gib(layers: int, tokens: int, hidden_size: int, bytes_per_value: int = 2, batch: int = 1) -> float:
    """估算 KV Cache 显存占用，单位 GiB。

    每层、每个 token 都需要保存 key 和 value 两份向量，
    所以公式里有一个 ``* 2``。
    """
    bytes_total = batch * layers * tokens * hidden_size * 2 * bytes_per_value
    return bytes_total / (1024**3)


def quantized_cache_gib(fp_cache_gib: float, from_bits: int = 16, to_bits: int = 8) -> float:
    """估算量化后 KV Cache 的大小。"""
    return fp_cache_gib * to_bits / from_bits


def speculative_acceptance(draft_tokens: list[str], target_tokens: list[str]) -> float:
    """计算投机解码中 draft token 被目标模型接受的比例。

    draft 模型先快速生成若干 token，target 模型验证。
    接受率越高，投机解码越能提升速度。
    """
    accepted = 0
    for draft, target in zip(draft_tokens, target_tokens):
        if draft != target:
            break
        accepted += 1
    return accepted / max(1, len(draft_tokens))


def run() -> dict[str, object]:
    """运行第 24 课演示：输出 KV Cache 估算和投机接受率。"""
    cache = kv_cache_gib(layers=32, tokens=8192, hidden_size=4096)
    return {"title": TITLE, "kv_cache_gib": round(cache, 3), "int8_cache_gib": round(quantized_cache_gib(cache), 3), "acceptance": speculative_acceptance(["a", "b", "x"], ["a", "b", "c"])}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()