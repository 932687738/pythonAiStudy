"""第 4 课：监督学习，回归与分类。

本章同时给出两个监督学习例子：
1. 回归：预测连续数值，例如房价；
2. 分类：预测离散类别，例如用户是否流失。
"""

from __future__ import annotations

from ai_study.common import binary_cross_entropy, logistic_regression_gd, sigmoid, standardize_columns
from ai_study.chapters.machine_learning_workflow import train_price_model

TITLE = "Supervised learning: regression and classification"


def churn_rows() -> tuple[list[list[float]], list[int]]:
    """构造一个极小的用户流失数据集。

    特征含义：
    - months_active：活跃月数；
    - support_tickets：客服工单数量。

    标签 ``1`` 表示流失，``0`` 表示未流失。
    """
    features = [
        [3, 18],
        [4, 15],
        [12, 1],
        [10, 2],
        [2, 20],
        [8, 3],
        [11, 0],
        [5, 10],
    ]
    labels = [1, 1, 0, 0, 1, 0, 0, 1]
    return features, labels


def train_churn_classifier() -> dict[str, object]:
    """训练一个逻辑回归分类器。

    逻辑回归适合做二分类 baseline。它可解释、训练快，也是很多分类任务的第一版模型。
    """
    features, labels = churn_rows()
    scaled, centers, spreads = standardize_columns(features)
    weights, bias = logistic_regression_gd(scaled, labels)
    probs = [sigmoid(sum(w * x for w, x in zip(weights, row)) + bias) for row in scaled]
    # 交叉熵衡量概率预测质量；准确率衡量最终分类是否正确。
    loss = sum(binary_cross_entropy(prob, label) for prob, label in zip(probs, labels)) / len(labels)
    accuracy = sum((prob >= 0.5) == bool(label) for prob, label in zip(probs, labels)) / len(labels)
    return {
        "features": ["months_active", "support_tickets"],
        "weights": [round(w, 3) for w in weights],
        "bias": round(bias, 3),
        "loss": round(loss, 4),
        "accuracy": round(accuracy, 3),
        "centers": [round(v, 3) for v in centers],
        "spreads": [round(v, 3) for v in spreads],
    }


def run() -> dict[str, object]:
    """运行第 4 课演示：同时返回回归和分类结果。"""
    return {
        "title": TITLE,
        "regression": train_price_model(),
        "classification": train_churn_classifier(),
    }
