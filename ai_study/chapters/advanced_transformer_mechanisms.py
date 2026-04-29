"""第 19 课：Transformer 深层机理、缩放定律与电路分析。

这里用注意力熵和归纳头分数做两个小指标。
它们帮助观察注意力是分散还是集中，以及模型是否学到复制/续写类模式。
"""

from __future__ import annotations

from math import log

from ai_study.common import Matrix

TITLE = "Advanced Transformer mechanisms"


def attention_entropy(attention: Matrix) -> list[float]:
    """计算每个 token 的注意力熵。

    熵越低，注意力越集中；熵越高，注意力越分散。
    这可以作为理解注意力信息路由的一个小观察窗口。
    """
    result = []
    for row in attention:
        result.append(-sum(p * log(p + 1e-12) for p in row))
    return result


def induction_head_score(tokens: list[str], attended_tokens: list[str]) -> float:
    """估计一个简化归纳头匹配分数。

    归纳头常被用来解释 Transformer 如何发现重复模式并预测后续 token。
    这里用相邻位置匹配比例做一个玩具指标。
    """
    hits = sum(1 for token, attended in zip(tokens[1:], attended_tokens[:-1]) if token == attended)
    return hits / max(1, len(tokens) - 1)


def run() -> dict[str, object]:
    """运行第 19 课演示：输出注意力熵和归纳头分数。"""
    attn = [[0.8, 0.2], [0.5, 0.5]]
    return {"title": TITLE, "entropy": [round(v, 4) for v in attention_entropy(attn)], "induction_score": induction_head_score(["A", "B", "A", "B"], ["X", "A", "B", "A"])}
