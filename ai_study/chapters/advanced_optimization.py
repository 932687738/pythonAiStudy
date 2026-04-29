"""第 18 课：大规模优化，AdamW、自然梯度、SAM 与分布式优化。

本模块实现 AdamW 的单参数更新和 SAM 的扰动方向。
它们是现代深度学习训练中非常常见的优化技巧。
"""

from __future__ import annotations

from math import sqrt

from ai_study.common import Vector, norm, scale

TITLE = "Advanced large-scale optimization"


def adamw_step(param: float, grad: float, m: float, v: float, step: int, lr: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, weight_decay: float = 0.01) -> tuple[float, float, float]:
    """执行一次 AdamW 更新。

    ``m`` 是一阶动量，类似梯度的指数滑动平均；
    ``v`` 是二阶动量，类似平方梯度的指数滑动平均；
    AdamW 把 weight decay 从梯度更新中解耦出来，通常比 Adam + L2 更稳定。
    """
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * grad * grad
    m_hat = m / (1 - beta1**step)
    v_hat = v / (1 - beta2**step)
    param = param - lr * (m_hat / (sqrt(v_hat) + 1e-8) + weight_decay * param)
    return param, m, v


def sam_perturbation(grads: Vector, rho: float = 0.05) -> Vector:
    """计算 SAM 的参数扰动方向。

    SAM 会先沿梯度方向走到邻域中损失更高的位置，再在那里计算更新，
    目标是找到更平坦、更泛化的解。
    """
    length = norm(grads) or 1.0
    return scale(grads, rho / length)


def run() -> dict[str, object]:
    """运行第 18 课演示：输出 AdamW 更新和 SAM 扰动。"""
    param, m, v = adamw_step(param=1.0, grad=0.25, m=0.0, v=0.0, step=1)
    return {"title": TITLE, "adamw_param": round(param, 6), "moments": [round(m, 6), round(v, 6)], "sam": [round(x, 6) for x in sam_perturbation([3.0, 4.0])]}
