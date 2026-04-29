"""第 13 课：LangChain4j 应用开发的 Python 侧映射。

原课程关注 Java 生态下的模型、工具、记忆和 RAG 组合。
这里用一个小型记忆类和链式函数说明“应用入口如何组织上下文”。
"""

from __future__ import annotations

TITLE = "LangChain4j application development mapping"


class ConversationMemory:
    """固定长度会话记忆。

    真实应用不能无限保存上下文，否则成本和延迟都会上涨。
    ``max_items`` 用来保留最近若干条消息，体现“最小必要记忆”的原则。
    """

    def __init__(self, max_items: int = 4) -> None:
        """创建一个最多保留 ``max_items`` 条消息的记忆容器。"""
        self.max_items = max_items
        self.items: list[str] = []

    def add(self, message: str) -> None:
        """添加一条消息，并裁剪到最大长度。"""
        self.items.append(message)
        self.items = self.items[-self.max_items :]

    def context(self) -> str:
        """把记忆拼成可放入 Prompt 的上下文文本。"""
        return "\n".join(self.items)


def chain(question: str, memory: ConversationMemory) -> str:
    """一个极简应用链。

    先把用户问题写入记忆，再生成回答，最后把回答也写回记忆。
    真实 LangChain4j 应用会在这里组合模型、工具、检索器和业务服务。
    """
    memory.add(f"user: {question}")
    answer = f"Use retrieved context and tools before answering: {question}"
    memory.add(f"assistant: {answer}")
    return answer


def run() -> dict[str, object]:
    """运行第 13 课演示：执行一次带记忆的应用链。"""
    memory = ConversationMemory()
    return {"title": TITLE, "answer": chain("Find project policy", memory), "memory": memory.items}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()