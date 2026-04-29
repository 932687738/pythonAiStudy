"""第 21 课：状态空间模型、RWKV 与长上下文建模。

SSM 和 RWKV 都试图用递推状态承载长程信息。
相比标准注意力，它们的计算可以更接近线性复杂度。
"""

from __future__ import annotations

from math import exp

from ai_study.common import Vector

TITLE = "Advanced SSM and RWKV long context"


def ssm_recurrence(inputs: Vector, a: float, b: float, c: float) -> Vector:
    """离散状态空间模型递推。

    ``state = a * state + b * input`` 表示状态保留历史并吸收新输入；
    ``output = c * state`` 表示从状态读出当前输出。
    """
    state = 0.0
    outputs = []
    for value in inputs:
        state = a * state + b * value
        outputs.append(c * state)
    return outputs


def rwkv_time_mix(values: Vector, decay: float) -> Vector:
    """简化版 RWKV 时间混合。

    ``decay`` 控制历史状态衰减速度。衰减慢，模型保留更久历史；
    衰减快，模型更关注近期输入。
    """
    state = 0.0
    outputs = []
    alpha = exp(-decay)
    for value in values:
        state = alpha * state + (1 - alpha) * value
        outputs.append(state)
    return outputs


def run() -> dict[str, object]:
    """运行第 21 课演示：输出 SSM 和 RWKV 风格时间混合结果。"""
    return {
        "title": TITLE,
        "ssm": [round(v, 4) for v in ssm_recurrence([1, 2, 0, 1], 0.7, 0.5, 1.2)],
        "rwkv_mix": [round(v, 4) for v in rwkv_time_mix([1, 0, 3, 2], 0.4)],
    }

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()