"""第 15 课：数值线性代数、随机矩阵理论与谱分析。

谱分析关注矩阵的特征值和特征向量。深度学习里可以用它观察权重矩阵、
Hessian 或表示协方差是否出现强方向，也就是课程中提到的 outlier。
"""

from __future__ import annotations

from ai_study.common import Matrix, Vector, dot, mat_vec, norm, scale

TITLE = "Advanced numerical linear algebra and spectral analysis"


def power_iteration(matrix: Matrix, rounds: int = 30) -> tuple[float, Vector]:
    """用幂迭代估计最大特征值和对应特征向量。

    思路：不断用矩阵乘当前向量，向量会逐渐朝最大特征值对应的方向靠拢。
    这是大矩阵谱分析中非常常见的近似方法。
    """
    vector = [1.0 for _ in matrix]
    for _ in range(rounds):
        # 每次乘矩阵后做归一化，避免向量长度指数级变大或变小。
        vector = mat_vec(matrix, vector)
        length = norm(vector) or 1.0
        vector = scale(vector, 1.0 / length)
    eigenvalue = dot(vector, mat_vec(matrix, vector))
    return eigenvalue, vector


def spectral_outlier_score(eigenvalues: Vector) -> float:
    """计算最大特征值相对 bulk 均值的突出程度。

    分数越大，说明最大特征值越像一个 outlier，可能对应模型学到的结构化方向。
    """
    bulk = sorted(eigenvalues)[:-1]
    top = max(eigenvalues)
    center = sum(bulk) / len(bulk)
    return top / center if center else 0.0


def run() -> dict[str, object]:
    """运行第 15 课演示：估计一个 2x2 矩阵的主特征方向。"""
    eigenvalue, vector = power_iteration([[2.0, 0.4], [0.4, 1.0]])
    return {
        "title": TITLE,
        "top_eigenvalue": round(eigenvalue, 4),
        "top_eigenvector": [round(v, 4) for v in vector],
        "outlier_score": round(spectral_outlier_score([0.9, 1.0, 1.1, eigenvalue]), 4),
    }
