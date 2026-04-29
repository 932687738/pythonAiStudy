"""第 17 课：变分推断、归一化流与贝叶斯深度学习。

这一章的代码把 KL、ELBO 和可逆变换拆成小函数。
它们是理解 VAE、Bayes by Backprop 和 Normalizing Flow 的基础构件。
"""

from __future__ import annotations

from math import exp, log

TITLE = "Advanced variational inference and flows"


def gaussian_kl_to_standard_normal(mu: float, sigma: float) -> float:
    """计算一维高斯分布到标准正态分布的 KL 散度。

    KL 越小，说明近似后验越接近先验；在 VAE/贝叶斯模型里常作为正则项。
    """
    return 0.5 * (mu * mu + sigma * sigma - 1.0 - log(sigma * sigma))


def affine_coupling_forward(x1: float, x2: float, shift: float, log_scale: float) -> tuple[tuple[float, float], float]:
    """一个极简 affine coupling layer 的前向变换。

    ``x1`` 保持不变，``x2`` 做可逆仿射变换。
    返回的 ``log_det`` 是流模型计算概率密度时需要的雅可比行列式对数。
    """
    y1 = x1
    y2 = x2 * exp(log_scale) + shift
    return (y1, y2), log_scale


def elbo(reconstruction_log_prob: float, kl: float, beta: float = 1.0) -> float:
    """计算 ELBO。

    ELBO = 重构对数似然 - beta * KL。
    训练时通常最大化 ELBO，等价于同时追求重构质量和后验正则化。
    """
    return reconstruction_log_prob - beta * kl


def run() -> dict[str, object]:
    """运行第 17 课演示：输出 KL 和一次 flow 变换结果。"""
    kl = gaussian_kl_to_standard_normal(mu=0.2, sigma=0.8)
    flow_y, log_det = affine_coupling_forward(1.0, 2.0, shift=0.3, log_scale=-0.1)
    return {"title": TITLE, "kl": round(kl, 4), "flow_y": tuple(round(v, 4) for v in flow_y), "log_det": log_det}
