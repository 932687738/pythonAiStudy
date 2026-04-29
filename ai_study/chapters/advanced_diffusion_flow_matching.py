"""第 22 课：扩散模型、Score-based SDE 与 Flow Matching。

扩散模型通过逐步加噪和去噪学习生成分布。
Flow Matching 则学习从简单分布流向数据分布的速度场。
"""

from __future__ import annotations

from math import sqrt

TITLE = "Advanced diffusion and flow matching"


def ddpm_noisy_sample(x0: float, noise: float, alpha_bar: float) -> float:
    """DDPM 前向加噪公式。

    ``x0`` 是干净样本，``noise`` 是高斯噪声，
    ``alpha_bar`` 控制当前时间步保留多少原始信号。
    """
    return sqrt(alpha_bar) * x0 + sqrt(1 - alpha_bar) * noise


def predict_x0_from_noise(xt: float, predicted_noise: float, alpha_bar: float) -> float:
    """根据噪声预测反推出干净样本估计值。"""
    return (xt - sqrt(1 - alpha_bar) * predicted_noise) / sqrt(alpha_bar)


def flow_matching_target(x0: float, x1: float) -> float:
    """Flow Matching 中从起点到终点的目标速度。"""
    return x1 - x0


def interpolate_flow(x0: float, x1: float, t: float) -> float:
    """在起点和终点之间做线性插值，表示流路径上的中间状态。"""
    return (1 - t) * x0 + t * x1


def run() -> dict[str, object]:
    """运行第 22 课演示：加噪、还原和 flow target。"""
    xt = ddpm_noisy_sample(2.0, -0.3, 0.81)
    return {"title": TITLE, "noisy_sample": round(xt, 4), "recovered_x0": round(predict_x0_from_noise(xt, -0.3, 0.81), 4), "flow_target": flow_matching_target(0.2, 1.0)}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()