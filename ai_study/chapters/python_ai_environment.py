"""第 1 课：Python 与 AI 开发环境。

这一章把课程中的 Python 基础操作落实成函数：列表统计、字典组织数据、Path 管理目录。
这些能力是后面读数据、保存模型、输出报告时反复要用到的基本功。
"""

from __future__ import annotations

from pathlib import Path
from statistics import mean

TITLE = "Python and AI development environment"


def score_summary(scores: list[int]) -> dict[str, float | int]:
    """统计一组成绩。

    这里演示列表推导式、条件筛选、均值、最大值等基础语法。
    返回字典是因为 AI 项目里常用结构化结果承载多个指标。
    """
    passed = [score for score in scores if score >= 60]
    return {
        "count": len(scores),
        "passed": len(passed),
        "average": round(mean(scores), 2),
        "best": max(scores),
    }


def project_paths(root: Path) -> dict[str, Path]:
    """基于项目根目录构造常见子目录。

    使用 ``pathlib.Path`` 比手写字符串路径更稳，能减少 Windows/Linux 路径分隔符差异带来的问题。
    """
    return {
        "root": root,
        "data": root / "data",
        "models": root / "models",
        "reports": root / "reports",
    }


def run() -> dict[str, object]:
    """运行第 1 课演示：展示基础数据结构和项目路径组织。"""
    scores = [88, 92, 79, 95]
    return {
        "title": TITLE,
        "student": {"name": "Alice", "role": "AI learner"},
        "scores": score_summary(scores),
        "paths": {key: str(value) for key, value in project_paths(Path.cwd()).items()},
    }

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()