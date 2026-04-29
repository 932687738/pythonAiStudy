"""第 23 课：大模型对齐，RLHF、DPO、RLAIF 与偏好优化。

偏好优化的核心是让模型更偏向被选择的回答，而不是被拒绝的回答。
本模块实现 DPO 损失和 GRPO 风格优势归一化的玩具版本。
"""

from __future__ import annotations

from math import exp, log

from ai_study.common import Vector, mean

TITLE = "Advanced LLM alignment"


def dpo_loss(chosen_logp: float, rejected_logp: float, ref_chosen_logp: float, ref_rejected_logp: float, beta: float = 0.1) -> float:
    """计算一对偏好样本的 DPO 损失。

    chosen 是人类或规则偏好的回答，rejected 是较差回答。
    参考模型 logp 用来约束策略不要偏离原模型太远。
    """
    margin = beta * ((chosen_logp - rejected_logp) - (ref_chosen_logp - ref_rejected_logp))
    return -log(1.0 / (1.0 + exp(-margin)))


def grpo_advantages(rewards: Vector, eps: float = 1e-8) -> Vector:
    """对同组 reward 做标准化，得到相对优势。

    组内标准化可以减少奖励尺度差异，让优化更关注“同组谁更好”。
    """
    center = mean(rewards)
    variance = mean([(reward - center) ** 2 for reward in rewards])
    scale = variance**0.5 + eps
    return [(reward - center) / scale for reward in rewards]


def run() -> dict[str, object]:
    """运行第 23 课演示：输出 DPO 损失和优势值。"""
    return {"title": TITLE, "dpo_loss": round(dpo_loss(-1.0, -2.2, -1.1, -1.9), 4), "advantages": [round(v, 4) for v in grpo_advantages([1.0, 0.5, 2.0])]}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()