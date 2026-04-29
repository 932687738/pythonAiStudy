"""第 7 课：CNN、RNN 与 Transformer 入门。

本章不用完整深度学习框架，而是把三类结构拆成最小可读函数：
卷积看局部模式，RNN 维护历史状态，注意力根据相似度选择信息。
"""

from __future__ import annotations

from math import tanh

from ai_study.common import Matrix, Vector, dot, softmax

TITLE = "CNN, RNN, and Transformer intro"


def conv1d(signal: Vector, kernel: Vector) -> Vector:
    """一维卷积。

    卷积核在输入序列上滑动，每个位置计算一次点积。
    这可以理解为检测局部模式，例如边缘、峰值或短语片段。
    """
    width = len(kernel)
    return [dot(signal[i : i + width], kernel) for i in range(len(signal) - width + 1)]


def rnn_step(x: Vector, hidden: Vector, wx: Matrix, wh: Matrix, bias: Vector) -> Vector:
    """执行一个 RNN 时间步。

    新状态同时依赖当前输入 ``x`` 和上一个隐藏状态 ``hidden``，
    这就是 RNN 能处理序列历史信息的原因。
    """
    result = []
    for i in range(len(hidden)):
        value = dot(wx[i], x) + dot(wh[i], hidden) + bias[i]
        result.append(tanh(value))
    return result


def self_attention(query: Vector, keys: Matrix, values: Matrix) -> Vector:
    """最小自注意力计算。

    查询向量 query 与每个 key 做点积得到相关性分数，
    softmax 把分数转为权重，再对 value 加权求和。
    """
    scores = softmax([dot(query, key) for key in keys])
    return [sum(score * value[i] for score, value in zip(scores, values)) for i in range(len(values[0]))]


def run() -> dict[str, object]:
    """运行第 7 课演示：分别输出卷积、RNN 和注意力结果。"""
    return {
        "title": TITLE,
        "cnn": conv1d([0, 1, 3, 2, 0], [1, 0, -1]),
        "rnn": [round(v, 4) for v in rnn_step([1, 0], [0.2, -0.1], [[0.4, 0.1], [0.2, 0.5]], [[0.3, 0.1], [0.0, 0.2]], [0, 0])],
        "attention": [round(v, 4) for v in self_attention([1, 0], [[1, 0], [0, 1]], [[10, 0], [0, 10]])],
    }

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()