"""第 5 课：无监督学习、特征工程与模型评估。

这里用 KMeans 演示“没有标签时如何根据样本距离发现结构”。
同时保留标准化步骤，强调特征工程对传统机器学习的重要性。
"""

from __future__ import annotations

from ai_study.common import kmeans, mean, norm, standardize_columns, sub

TITLE = "Unsupervised learning and feature engineering"


def customer_points() -> list[list[float]]:
    """构造客户行为特征。

    每个点包含两个维度，例如消费金额和访问次数。
    聚类不需要标签，模型只根据点之间的距离分组。
    """
    return [
        [12, 40],
        [15, 43],
        [11, 38],
        [80, 5],
        [75, 8],
        [82, 6],
        [35, 20],
        [38, 18],
    ]


def cluster_customers() -> dict[str, object]:
    """对客户做聚类，并返回简单评估指标。

    ``mean_distance_to_center`` 越小，说明样本越靠近各自簇中心。
    这不是唯一指标，但能帮助理解聚类紧凑度。
    """
    scaled, _, _ = standardize_columns(customer_points())
    centers, labels = kmeans(scaled, k=3)
    distances = [norm(sub(point, centers[label])) for point, label in zip(scaled, labels)]
    return {
        "feature_engineering": ["standardize amount and visit count"],
        "labels": labels,
        "centers": [[round(v, 3) for v in row] for row in centers],
        "mean_distance_to_center": round(mean(distances), 4),
    }


def run() -> dict[str, object]:
    """运行第 5 课演示：输出聚类标签和簇中心。"""
    return {"title": TITLE, "clustering": cluster_customers()}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()