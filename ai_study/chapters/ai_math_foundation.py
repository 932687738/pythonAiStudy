"""第 2 课：AI 数学基础。

课程里的向量、矩阵、概率分布和梯度，在这里都用很小的函数展开。
重点不是追求高性能，而是让公式和代码一一对应，方便调试 shape 和理解数据流。
"""

from __future__ import annotations

from ai_study.common import Matrix, Vector, dot, mat_vec, mean, numerical_gradient, softmax

TITLE = "AI math foundation"


def vector_similarity(a: Vector, b: Vector) -> dict[str, float]:
    """计算两个向量的简单相似信息。

    点积越大，通常表示两个向量在方向和长度上越“同向”。
    """
    return {"dot": dot(a, b), "mean_a": mean(a), "mean_b": mean(b)}


def linear_layer(x: Vector, weights: Matrix, bias: Vector) -> Vector:
    """实现一个最小线性层。

    ``weights`` 的每一行对应一个输出神经元的权重。
    输出公式是 ``weights @ x + bias``，这也是神经网络线性层的核心。
    """
    return [value + bias[i] for i, value in enumerate(mat_vec(weights, x))]


def squared_loss_gradient(prediction: Vector, target: Vector) -> Vector:
    """均方误差对预测值的梯度。

    如果预测值高于真实值，梯度为正，参数更新会推动预测下降；反之亦然。
    """
    return [2.0 * (p - t) / len(prediction) for p, t in zip(prediction, target)]


def run() -> dict[str, object]:
    """运行第 2 课演示：线性层、softmax 概率和数值梯度。"""
    x = [1.0, 2.0, 3.0]
    weights = [[0.2, 0.5, -0.1], [0.0, 0.3, 0.8]]
    logits = linear_layer(x, weights, [0.1, -0.2])
    grad = numerical_gradient(lambda values: sum(v * v for v in values), [3.0, 4.0])
    return {
        "title": TITLE,
        "shape": {"x": [3], "weights": [2, 3]},
        "logits": [round(v, 4) for v in logits],
        "probabilities": [round(v, 4) for v in softmax(logits)],
        "gradient_of_x2_plus_y2": [round(v, 4) for v in grad],
    }
