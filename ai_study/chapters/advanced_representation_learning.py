"""第 25 课：表示学习与自监督。

这里实现 InfoNCE 和线性 CKA 两个核心工具。
InfoNCE 用于对比学习，CKA 用于比较两组表示是否学到了相似结构。
"""

from __future__ import annotations

from math import exp, log

from ai_study.common import Matrix, cosine, flatten, mean

TITLE = "Advanced representation learning"


def info_nce(query: list[float], positive: list[float], negatives: Matrix, temperature: float = 0.1) -> float:
    """计算一个 query 的 InfoNCE 损失。

    损失鼓励 query 与 positive 更相似，同时远离 negatives。
    temperature 越小，模型越强调相似度差异。
    """
    scores = [cosine(query, positive) / temperature]
    scores.extend(cosine(query, negative) / temperature for negative in negatives)
    denom = sum(exp(score) for score in scores)
    return -log(exp(scores[0]) / denom)


def centered(matrix: Matrix) -> Matrix:
    """对矩阵每一列去均值，CKA 计算前通常需要中心化。"""
    cols = list(zip(*matrix))
    centers = [mean(list(col)) for col in cols]
    return [[value - centers[i] for i, value in enumerate(row)] for row in matrix]


def linear_cka(x: Matrix, y: Matrix) -> float:
    """计算简化版线性 CKA 相似度。

    CKA 越接近 1，说明两组表示的几何结构越相似。
    这里使用小矩阵展开公式，便于理解表示比较的直觉。
    """
    xc = centered(x)
    yc = centered(y)
    xy = sum(a * b for a, b in zip(flatten(xc), flatten(yc)))
    xx = sum(a * a for a in flatten(xc))
    yy = sum(b * b for b in flatten(yc))
    return (xy * xy) / max(1e-12, xx * yy)


def run() -> dict[str, object]:
    """运行第 25 课演示：输出 InfoNCE 和 CKA。"""
    return {
        "title": TITLE,
        "info_nce": round(info_nce([1, 0], [0.9, 0.1], [[0, 1], [-1, 0]]), 4),
        "cka": round(linear_cka([[1, 2], [2, 3], [3, 4]], [[2, 1], [3, 2], [4, 3]]), 4),
    }
