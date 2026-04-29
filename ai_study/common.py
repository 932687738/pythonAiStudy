"""课程示例复用的轻量工具函数。

这些函数刻意只使用 Python 标准库，不依赖 NumPy、pandas、scikit-learn 或 PyTorch。
原因是本项目的第一目标是“跟着课程理解概念”，而不是一开始就被环境安装卡住。

文件里的工具大致分为四类：
1. 向量和矩阵基础运算：dot、norm、transpose、mat_mul 等。
2. 机器学习常用函数：sigmoid、softmax、标准化、训练集/测试集划分。
3. 简化版算法实现：线性回归、逻辑回归、KMeans。
4. 数学辅助：数值梯度、裁剪、二分类交叉熵。

这些实现不是为了替代成熟框架，而是把课程中出现的核心公式展开成可读代码。
"""

from __future__ import annotations

from math import exp, log, sqrt
from random import Random
from typing import Callable, Iterable, Sequence

Vector = list[float]
Matrix = list[list[float]]


def mean(values: Sequence[float]) -> float:
    """计算均值。

    机器学习中很多统计量都从均值开始，例如特征标准化、损失平均值和聚类中心。
    空列表没有数学意义，所以这里显式抛出异常，避免后续出现更难定位的除零错误。
    """
    if not values:
        raise ValueError("mean() needs at least one value")
    return sum(values) / len(values)


def dot(left: Sequence[float], right: Sequence[float]) -> float:
    """计算两个向量的点积。

    点积是线性模型、注意力分数、余弦相似度里的基础操作。
    例如线性回归的预测值就是 ``dot(weights, x) + bias``。
    """
    return sum(a * b for a, b in zip(left, right))


def add(left: Sequence[float], right: Sequence[float]) -> Vector:
    """逐元素相加，常用于向量状态更新。"""
    return [a + b for a, b in zip(left, right)]


def sub(left: Sequence[float], right: Sequence[float]) -> Vector:
    """逐元素相减，常用于计算误差向量或距离。"""
    return [a - b for a, b in zip(left, right)]


def scale(values: Sequence[float], factor: float) -> Vector:
    """把向量中的每个元素乘以同一个系数。"""
    return [factor * value for value in values]


def norm(values: Sequence[float]) -> float:
    """计算 L2 范数，也就是向量长度。"""
    return sqrt(dot(values, values))


def transpose(matrix: Matrix) -> Matrix:
    """矩阵转置。

    在标准化、矩阵乘法和按列统计时，经常需要把“按行组织”的数据转成“按列组织”。
    """
    return [list(col) for col in zip(*matrix)]


def mat_vec(matrix: Matrix, vector: Sequence[float]) -> Vector:
    """矩阵乘向量。

    可以理解为多输出线性层：每一行权重和输入向量做一次点积。
    """
    return [dot(row, vector) for row in matrix]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    """矩阵乘矩阵。

    LoRA、线性层组合、投影矩阵等都会用到矩阵乘法。
    这里先转置右矩阵，是为了把列向量变成列表，便于复用 ``dot``。
    """
    right_t = transpose(right)
    return [[dot(row, col) for col in right_t] for row in left]


def sigmoid(value: float) -> float:
    """逻辑函数，把任意实数压到 0 到 1 之间。

    逻辑回归会把线性分数通过 sigmoid 转成“属于正类的概率”。
    分支写法用于避免非常大的正数或负数导致指数计算溢出。
    """
    if value >= 0:
        z = exp(-value)
        return 1.0 / (1.0 + z)
    z = exp(value)
    return z / (1.0 + z)


def softmax(values: Sequence[float]) -> Vector:
    """把一组分数转成概率分布。

    注意力权重、多分类输出都常用 softmax。
    先减去最大值是经典的数值稳定技巧，不改变结果，但能降低指数溢出的风险。
    """
    peak = max(values)
    exps = [exp(value - peak) for value in values]
    total = sum(exps)
    return [value / total for value in exps]


def cosine(left: Sequence[float], right: Sequence[float]) -> float:
    """计算余弦相似度。

    Embedding 检索常用它衡量两个向量方向是否接近。
    如果某个向量长度为 0，直接返回 0，表示无法判断相似。
    """
    denom = norm(left) * norm(right)
    return 0.0 if denom == 0 else dot(left, right) / denom


def train_test_split(
    rows: Sequence[dict[str, float]],
    test_ratio: float = 0.25,
    seed: int = 42,
) -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    """把数据划分为训练集和测试集。

    ``seed`` 让每次打乱结果一致，教学和测试时更容易复现。
    返回顺序是 ``train, test``，和后续章节的机器学习流程保持一致。
    """
    shuffled = list(rows)
    Random(seed).shuffle(shuffled)
    test_size = max(1, int(len(shuffled) * test_ratio))
    return shuffled[test_size:], shuffled[:test_size]


def standardize_columns(rows: Sequence[Sequence[float]]) -> tuple[Matrix, Vector, Vector]:
    """按列做标准化：每列减均值，再除以标准差。

    许多模型对特征尺度敏感。比如面积是几十到几百，房间数是个位数，
    如果直接训练，面积会在梯度里占更大权重。标准化能让不同特征更公平地参与训练。

    返回三项：
    - 标准化后的数据；
    - 每一列的均值；
    - 每一列的标准差。

    保存均值和标准差是为了测试集、线上新样本必须使用训练集学到的同一套变换。
    """
    cols = transpose([list(row) for row in rows])
    centers = [mean(col) for col in cols]
    spreads = []
    for col, center in zip(cols, centers):
        variance = mean([(value - center) ** 2 for value in col])
        spreads.append(sqrt(variance) or 1.0)
    scaled = [
        [(value - centers[i]) / spreads[i] for i, value in enumerate(row)]
        for row in rows
    ]
    return scaled, centers, spreads


def apply_standardization(row: Sequence[float], centers: Sequence[float], spreads: Sequence[float]) -> Vector:
    """用训练集得到的均值和标准差，转换一个新样本。"""
    return [(value - centers[i]) / spreads[i] for i, value in enumerate(row)]


def linear_regression_gd(
    features: Sequence[Sequence[float]],
    targets: Sequence[float],
    epochs: int = 800,
    lr: float = 0.05,
) -> tuple[Vector, float]:
    """用梯度下降训练一个最小二乘线性回归模型。

    模型形式：``y = dot(weights, x) + bias``。
    损失函数：均方误差 MSE。
    这里手写训练循环，是为了对应第 3、4 课里的“训练-预测-评估”流程。
    """
    if not features:
        raise ValueError("features must not be empty")
    weights = [0.0 for _ in features[0]]
    bias = 0.0
    n = len(features)
    for _ in range(epochs):
        # 每个 epoch 都重新累计所有样本的梯度，然后做一次批量更新。
        grad_w = [0.0 for _ in weights]
        grad_b = 0.0
        for x, y in zip(features, targets):
            # 预测误差越大，梯度越大；梯度方向告诉我们参数该往哪边调整。
            err = dot(weights, x) + bias - y
            grad_b += err
            for i, value in enumerate(x):
                grad_w[i] += err * value
        # 除以样本数得到平均梯度，学习率 lr 控制每一步走多远。
        weights = [w - lr * grad_w[i] / n for i, w in enumerate(weights)]
        bias -= lr * grad_b / n
    return weights, bias


def logistic_regression_gd(
    features: Sequence[Sequence[float]],
    labels: Sequence[int],
    epochs: int = 600,
    lr: float = 0.15,
) -> tuple[Vector, float]:
    """用梯度下降训练二分类逻辑回归。

    模型先计算线性分数，再通过 sigmoid 得到概率。
    ``labels`` 使用 0/1，适合演示流失预测、是否点击、是否通过审核等分类任务。
    """
    weights = [0.0 for _ in features[0]]
    bias = 0.0
    n = len(features)
    for _ in range(epochs):
        grad_w = [0.0 for _ in weights]
        grad_b = 0.0
        for x, y in zip(features, labels):
            # pred 是正类概率，pred - y 是交叉熵损失对线性分数的梯度。
            pred = sigmoid(dot(weights, x) + bias)
            err = pred - y
            grad_b += err
            for i, value in enumerate(x):
                grad_w[i] += err * value
        weights = [w - lr * grad_w[i] / n for i, w in enumerate(weights)]
        bias -= lr * grad_b / n
    return weights, bias


def kmeans(
    points: Sequence[Sequence[float]],
    k: int,
    rounds: int = 20,
    seed: int = 42,
) -> tuple[Matrix, list[int]]:
    """简化版 KMeans 聚类。

    算法循环两步：
    1. 分配：每个点归到最近的中心。
    2. 更新：每个中心移动到本组样本的均值位置。

    这对应第 5 课无监督学习的核心思想：没有标签，模型只能根据样本之间的距离发现结构。
    """
    rng = Random(seed)
    centers = [list(point) for point in rng.sample(list(points), k)]
    labels = [0 for _ in points]
    for _ in range(rounds):
        labels = [
            min(range(k), key=lambda idx: norm(sub(point, centers[idx])))
            for point in points
        ]
        for idx in range(k):
            group = [point for point, label in zip(points, labels) if label == idx]
            if group:
                centers[idx] = [mean(col) for col in transpose([list(p) for p in group])]
    return centers, labels


def numerical_gradient(fn: Callable[[Vector], float], values: Sequence[float], eps: float = 1e-5) -> Vector:
    """用有限差分估计梯度。

    对第 2 课和第 26 课很有帮助：即使不写反向传播，也能直观看到
    “输入某一维轻微变化，函数输出会怎么变化”。
    """
    result = []
    for i in range(len(values)):
        left = list(values)
        right = list(values)
        left[i] -= eps
        right[i] += eps
        result.append((fn(right) - fn(left)) / (2.0 * eps))
    return result


def flatten(values: Iterable[Iterable[float]]) -> Vector:
    """把二维列表摊平成一维列表，方便做整体统计。"""
    return [item for row in values for item in row]


def clip(value: float, low: float, high: float) -> float:
    """把数值限制在指定范围内，常用于避免概率等于 0 或 1。"""
    return max(low, min(high, value))


def binary_cross_entropy(pred: float, label: int) -> float:
    """二分类交叉熵损失。

    ``pred`` 是模型给出的正类概率，``label`` 是真实标签 0 或 1。
    预测越接近真实标签，损失越小；预测越自信但越错，损失会变大。
    """
    pred = clip(pred, 1e-9, 1.0 - 1e-9)
    return -(label * log(pred) + (1 - label) * log(1 - pred))
