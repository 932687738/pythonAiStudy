"""第 0 课：AI 全局认知与学习定位。

这一章不实现具体模型，而是把 AI 应用拆成几个层次：
数据、表示、模型、评估、应用接口和监控。后面每一章基本都能放回这张地图里。
"""

TITLE = "AI overview and learning map"


def ai_application_layers() -> list[str]:
    """返回一个典型 AI 应用从底到顶的组成层次。"""
    return [
        "data",
        "features-or-embeddings",
        "model",
        "evaluation",
        "application-api",
        "monitoring",
    ]


def classify_ai_task(description: str) -> str:
    """根据任务描述粗略判断它属于哪类 AI 应用。

    这不是生产级分类器，而是教学用的规则示例：让学习者先形成“问题类型”的意识。
    """
    text = description.lower()
    if any(word in text for word in ["predict", "price", "score", "regression"]):
        return "supervised learning"
    if any(word in text for word in ["cluster", "segment", "similar"]):
        return "unsupervised learning"
    if any(word in text for word in ["question", "document", "knowledge"]):
        return "rag application"
    if any(word in text for word in ["tool", "action", "agent"]):
        return "agentic application"
    return "general ai application"


def run() -> dict[str, object]:
    """运行第 0 课演示：输出应用层次和一个任务分类示例。"""
    return {
        "title": TITLE,
        "layers": ai_application_layers(),
        "example_task": classify_ai_task("answer questions from project documents"),
    }
