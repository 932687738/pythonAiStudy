"""第 12 课：Spring Boot + Spring AI 的 Python 侧映射。

原课程面向 Java/Spring。本 Python 项目不强行实现 Spring，
而是提炼其中通用的工程思想：Prompt 模板化、角色消息、业务参数注入。
"""

from __future__ import annotations

from dataclasses import dataclass

TITLE = "Spring Boot and Spring AI mapping"


@dataclass
class PromptTemplate:
    """可复用 Prompt 模板。

    系统消息描述助手身份和规则，用户消息承载具体问题。
    这对应 Spring AI 中常见的 PromptTemplate/Message 组织方式。
    """

    system: str
    user: str

    def render(self, **values: str) -> list[dict[str, str]]:
        """把业务变量填充进模板，生成模型可接收的消息列表。"""
        return [
            {"role": "system", "content": self.system.format(**values)},
            {"role": "user", "content": self.user.format(**values)},
        ]


def run() -> dict[str, object]:
    """运行第 12 课演示：渲染一组结构化消息。"""
    template = PromptTemplate(
        system="You are a support assistant for {product}.",
        user="Answer this question from policy: {question}",
    )
    return {"title": TITLE, "messages": template.render(product="CRM", question="How do refunds work?")}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()