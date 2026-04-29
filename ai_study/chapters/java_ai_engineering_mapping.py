"""第 14 课：Java AI 工程化的 Python 侧映射。

AI 工程化关注稳定性、权限、日志、成本和评估。
本模块用 token 记录、配额判断和成本估算模拟服务端常见治理逻辑。
"""

from __future__ import annotations

from dataclasses import dataclass

TITLE = "Java AI engineering mapping"


@dataclass
class UsageRecord:
    """一次模型调用的用量记录。

    服务端通常会记录用户、模型、输入 token、输出 token，用于审计、限流和计费。
    """

    user_id: str
    prompt_tokens: int
    completion_tokens: int
    model: str

    @property
    def total_tokens(self) -> int:
        """总 token 数，常用于配额和成本计算。"""
        return self.prompt_tokens + self.completion_tokens


def allow_request(record: UsageRecord, daily_quota: int) -> bool:
    """判断这次请求是否还在用户配额内。"""
    return record.total_tokens <= daily_quota


def estimate_cost(record: UsageRecord, price_per_1k: float) -> float:
    """按每千 token 单价估算调用成本。"""
    return round(record.total_tokens / 1000.0 * price_per_1k, 6)


def run() -> dict[str, object]:
    """运行第 14 课演示：输出配额判断和成本估算。"""
    record = UsageRecord("u-001", 800, 200, "low-cost-model")
    return {"title": TITLE, "allowed": allow_request(record, 1500), "cost": estimate_cost(record, 0.002)}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()