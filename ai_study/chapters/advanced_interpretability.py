"""第 26 课：可解释性、探针、因果干预与模型行为分析。

本模块包含三个常见方向：
1. integrated gradients：解释输入维度对输出的贡献；
2. linear probe：检查表示中是否线性可读出某类信息；
3. activation patch：模拟因果干预。
"""

from __future__ import annotations

from typing import Callable

from ai_study.common import Vector, numerical_gradient

TITLE = "Advanced interpretability"


def integrated_gradients(fn: Callable[[Vector], float], x: Vector, baseline: Vector | None = None, steps: int = 32) -> Vector:
    """计算 Integrated Gradients 归因。

    从 baseline 到输入 x 走一条直线路径，在路径上累计梯度。
    这比只看单点梯度更稳定，也更符合“从无信息输入逐渐变成真实输入”的解释方式。
    """
    baseline = baseline or [0.0 for _ in x]
    total = [0.0 for _ in x]
    for step in range(1, steps + 1):
        # alpha 从 0 到 1，表示沿着 baseline -> x 的路径逐步前进。
        alpha = step / steps
        point = [b + alpha * (value - b) for value, b in zip(x, baseline)]
        grad = numerical_gradient(fn, point)
        total = [current + g for current, g in zip(total, grad)]
    return [(value - b) * total[i] / steps for i, (value, b) in enumerate(zip(x, baseline))]


def linear_probe(features: list[Vector], labels: list[int]) -> dict[str, float]:
    """训练一个极简线性探针并返回准确率。

    这里不做梯度训练，而是用正负样本中心差作为分类方向。
    它足以演示探针思想：检查表示里是否存在可线性读出的信息。
    """
    positives = [feature for feature, label in zip(features, labels) if label == 1]
    negatives = [feature for feature, label in zip(features, labels) if label == 0]
    direction = [sum(col) / len(positives) for col in zip(*positives)]
    neg_center = [sum(col) / len(negatives) for col in zip(*negatives)]
    weights = [p - n for p, n in zip(direction, neg_center)]
    scores = [sum(w * value for w, value in zip(weights, feature)) for feature in features]
    threshold = sum(scores) / len(scores)
    accuracy = sum((score >= threshold) == bool(label) for score, label in zip(scores, labels)) / len(labels)
    return {"accuracy": accuracy, "threshold": threshold}


def activation_patch(clean: Vector, corrupted: Vector, index: int) -> Vector:
    """把 corrupted 激活中的某一维替换为 clean 激活。

    如果替换后模型行为恢复，说明该位置/维度可能对任务有因果作用。
    真实 mechanistic interpretability 会在层、头、token 位置上做类似干预。
    """
    patched = list(corrupted)
    patched[index] = clean[index]
    return patched


def run() -> dict[str, object]:
    """运行第 26 课演示：输出归因、探针准确率和一次激活替换。"""
    attrs = integrated_gradients(lambda values: values[0] ** 2 + 3 * values[1], [2.0, 1.0])
    probe = linear_probe([[1, 1], [1.2, 0.9], [-1, -1], [-0.8, -1.2]], [1, 1, 0, 0])
    return {"title": TITLE, "attribution": [round(v, 4) for v in attrs], "probe_accuracy": probe["accuracy"], "patched": activation_patch([1, 2, 3], [9, 9, 9], 1)}
