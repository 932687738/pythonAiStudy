"""第 3 课：机器学习完整流程。

本模块把“加载数据 -> 划分训练/测试 -> 特征标准化 -> 训练模型 -> 评估误差”
串成一个完整小流程。课程中的很多算法都会复用这条主线。
"""

from __future__ import annotations

from ai_study.common import apply_standardization, linear_regression_gd, mean, standardize_columns, train_test_split

TITLE = "Machine learning workflow"


def housing_rows() -> list[dict[str, float]]:
    """构造一个小型房价数据集。

    每一行代表一个样本，``area``、``rooms``、``age`` 是特征，``price`` 是监督学习标签。
    真实项目通常来自 CSV、数据库或接口；这里直接写在代码里，便于专注流程本身。
    """
    return [
        {"area": 65, "rooms": 2, "age": 12, "price": 302},
        {"area": 80, "rooms": 2, "age": 9, "price": 365},
        {"area": 95, "rooms": 3, "age": 7, "price": 454},
        {"area": 110, "rooms": 3, "age": 4, "price": 525},
        {"area": 120, "rooms": 4, "age": 8, "price": 560},
        {"area": 140, "rooms": 4, "age": 3, "price": 680},
        {"area": 150, "rooms": 5, "age": 2, "price": 735},
        {"area": 72, "rooms": 2, "age": 20, "price": 315},
    ]


def train_price_model() -> dict[str, object]:
    """训练一个房价回归模型并返回评估结果。

    这个函数是第 3 课的核心：
    - 训练集用于学习参数；
    - 测试集只用于评估；
    - 测试集必须使用训练集得到的标准化参数，避免数据泄漏。
    """
    train, test = train_test_split(housing_rows(), test_ratio=0.25)
    train_x = [[row["area"], row["rooms"], row["age"]] for row in train]
    train_y = [row["price"] for row in train]
    scaled_x, centers, spreads = standardize_columns(train_x)
    weights, bias = linear_regression_gd(scaled_x, train_y)
    predictions = []
    errors = []
    for row in test:
        # 新样本必须复用训练集的 centers/spreads，不能重新计算自己的均值和标准差。
        x = apply_standardization([row["area"], row["rooms"], row["age"]], centers, spreads)
        pred = sum(w * value for w, value in zip(weights, x)) + bias
        predictions.append(round(pred, 2))
        errors.append(abs(pred - row["price"]))
    return {
        "features": ["area", "rooms", "age"],
        "weights": [round(w, 3) for w in weights],
        "bias": round(bias, 3),
        "test_predictions": predictions,
        "mae": round(mean(errors), 3),
    }


def run() -> dict[str, object]:
    """运行第 3 课演示：输出完整工作流和模型指标。"""
    return {"title": TITLE, "workflow": ["load", "split", "train", "evaluate"], "model": train_price_model()}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()