"""第 11 课：Function Calling、Tool Calling 与 Agent。

本章用本地函数模拟工具调用。真实大模型会先决定调用哪个工具和参数，
然后程序执行工具，把结果交回模型继续推理。
"""

from __future__ import annotations

from dataclasses import dataclass

TITLE = "Function calling, tool calling, and agents"


@dataclass
class ToolCall:
    """一次工具调用的结构化表示。

    ``name`` 是工具名，``arguments`` 是工具参数。
    这个数据结构对应大模型 tool calling 返回的结构化 JSON。
    """

    name: str
    arguments: dict[str, float | str]


def calculator(expression: str) -> float:
    """一个极简计算器工具。

    为了避免执行任意代码，只允许数字和基础运算符。
    生产环境里通常会使用更严格的表达式解析器，而不是直接 ``eval``。
    """
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise ValueError("unsafe expression")
    return float(eval(expression, {"__builtins__": {}}, {}))


def fake_weather(city: str) -> str:
    """天气工具示例，用固定结果模拟外部 API。"""
    return f"{city}: sunny, 24C"


def run_agent(goal: str) -> list[str]:
    """根据目标选择工具并记录执行轨迹。

    这不是智能 Agent，而是教学用规则循环：
    看到天气相关词就调用天气工具，看到计算表达式就调用计算器。
    """
    trace = [f"goal: {goal}"]
    if "weather" in goal.lower():
        trace.append(fake_weather("Shanghai"))
    if any(op in goal for op in ["+", "-", "*", "/"]):
        expression = goal.split("calculate", 1)[-1].strip()
        trace.append(f"calculator: {calculator(expression)}")
    trace.append("done")
    return trace


def run() -> dict[str, object]:
    """运行第 11 课演示：展示一次工具调用轨迹。"""
    return {"title": TITLE, "trace": run_agent("calculate 12 * (3 + 1)")}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()