"""第 16 课：张量分解、低秩结构与参数高效训练。

LoRA 的核心是假设任务需要的权重更新可以用低秩矩阵表示。
本模块用小矩阵展示 ``Delta W = B @ A`` 这个结构。
"""

from __future__ import annotations

from ai_study.common import Matrix, mat_mul

TITLE = "Advanced low-rank PEFT"


def lora_update(a: Matrix, b: Matrix, alpha: float) -> Matrix:
    """计算 LoRA 的低秩权重更新。

    ``A`` 把输入投影到低维任务子空间，``B`` 再映射回输出空间。
    ``alpha / rank`` 是 LoRA 常见缩放项，用来控制更新幅度。
    """
    rank = len(a)
    raw = mat_mul(b, a)
    scale = alpha / rank
    return [[scale * value for value in row] for row in raw]


def count_trainable_lora_params(in_features: int, out_features: int, rank: int) -> int:
    """计算 LoRA 需要训练的参数量。

    全量线性层参数是 ``in_features * out_features``；
    LoRA 只训练 ``rank * (in_features + out_features)``，通常小很多。
    """
    return rank * (in_features + out_features)


def run() -> dict[str, object]:
    """运行第 16 课演示：输出 LoRA 参数量和一个玩具更新矩阵。"""
    update = lora_update([[0.2, -0.1], [0.0, 0.3]], [[1.0, 0.5], [-0.4, 0.2]], alpha=8.0)
    return {
        "title": TITLE,
        "trainable_params": count_trainable_lora_params(4096, 4096, 8),
        "toy_update": [[round(v, 4) for v in row] for row in update],
    }

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()