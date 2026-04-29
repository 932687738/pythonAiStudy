"""第 6 课：深度学习与训练循环基础。

课程原本会引入 PyTorch。为了让项目在无第三方依赖时也能运行，
这里手写一个极小神经网络，展示前向计算、损失、梯度和参数更新的骨架。
"""

from __future__ import annotations

from math import tanh

TITLE = "Deep learning and training loops"


def tiny_network_forward(x: float, params: dict[str, float]) -> float:
    """执行一次前向传播。

    结构是：输入 x -> 一个 tanh 隐藏单元 -> 一个线性输出。
    虽然模型很小，但已经包含神经网络的基本组成。
    """
    hidden = tanh(params["w1"] * x + params["b1"])
    return params["w2"] * hidden + params["b2"]


def train_tiny_network(epochs: int = 200, lr: float = 0.03) -> dict[str, object]:
    """训练一个拟合 ``y = x^2`` 的小网络。

    训练循环包含深度学习代码最常见的步骤：
    1. 前向传播得到预测；
    2. 计算误差和损失；
    3. 根据链式法则计算梯度；
    4. 用学习率更新参数。
    """
    data = [(-2.0, 4.0), (-1.0, 1.0), (0.0, 0.0), (1.0, 1.0), (2.0, 4.0)]
    params = {"w1": 0.4, "b1": 0.0, "w2": 0.8, "b2": 0.0}
    for _ in range(epochs):
        # 每轮先把梯度清零，避免上一轮的梯度残留影响本轮更新。
        grads = {key: 0.0 for key in params}
        loss = 0.0
        for x, y in data:
            h = tanh(params["w1"] * x + params["b1"])
            pred = params["w2"] * h + params["b2"]
            err = pred - y
            loss += err * err
            # 下面是手写反向传播：从输出层梯度一路传回隐藏层。
            grads["w2"] += 2 * err * h
            grads["b2"] += 2 * err
            dh = 2 * err * params["w2"] * (1 - h * h)
            grads["w1"] += dh * x
            grads["b1"] += dh
        for key in params:
            params[key] -= lr * grads[key] / len(data)
    return {
        "params": {key: round(value, 4) for key, value in params.items()},
        "sample_prediction": round(tiny_network_forward(1.5, params), 4),
    }


def run() -> dict[str, object]:
    """运行第 6 课演示：返回训练后的参数和一个样本预测。"""
    return {"title": TITLE, "training_loop": train_tiny_network()}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()