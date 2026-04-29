"""第 20 课：稀疏专家模型 MoE。

MoE 的关键是路由器：每个 token 只发送给少量专家，而不是所有专家。
这样可以增加模型容量，同时控制每次推理的计算量。
"""

from __future__ import annotations

from ai_study.common import Matrix, softmax

TITLE = "Advanced MoE routing and load balancing"


def top_k_router(logits: Matrix, k: int = 2) -> list[list[int]]:
    """根据路由分数为每个 token 选择 top-k 专家。"""
    routes = []
    for row in logits:
        ranked = sorted(range(len(row)), key=lambda idx: row[idx], reverse=True)
        routes.append(ranked[:k])
    return routes


def load_balance(routes: list[list[int]], expert_count: int) -> list[float]:
    """统计专家负载比例。

    如果所有 token 都路由到同一个专家，会导致负载不均和专家退化。
    负载均衡指标用于观察路由是否过度集中。
    """
    counts = [0 for _ in range(expert_count)]
    for token_routes in routes:
        for expert in token_routes:
            counts[expert] += 1
    total = sum(counts) or 1
    return [count / total for count in counts]


def router_probabilities(logits: Matrix) -> Matrix:
    """把专家 logits 转成概率分布，便于观察路由偏好。"""
    return [softmax(row) for row in logits]


def run() -> dict[str, object]:
    """运行第 20 课演示：输出路由结果和负载比例。"""
    logits = [[2.0, 0.1, 1.0], [0.2, 2.5, 1.2], [0.4, 1.1, 2.2]]
    routes = top_k_router(logits)
    return {"title": TITLE, "routes": routes, "load": [round(v, 4) for v in load_balance(routes, 3)]}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()