"""第 10 课：RAG 知识库问答系统。

RAG 的核心不是“直接让模型回答”，而是先从知识库检索证据，再基于证据生成答案。
本模块用简化版检索替代真实大模型，展示 RAG 的数据流。
"""

from __future__ import annotations

from ai_study.chapters.embedding_semantic_search import semantic_search

TITLE = "RAG knowledge base QA"


def chunk_document(document: str, size: int = 18) -> list[str]:
    """把长文档切成较短片段。

    分块是 RAG 的关键步骤之一。块太大容易浪费上下文，块太小又可能丢失语义。
    这里按词数切分，只用于演示。
    """
    words = document.split()
    return [" ".join(words[i : i + size]) for i in range(0, len(words), size)]


def answer_with_retrieval(question: str, documents: list[str]) -> dict[str, object]:
    """执行一个最小 RAG 流程。

    步骤：
    1. 文档切块；
    2. 根据问题检索相关块；
    3. 把检索到的块作为证据组织成答案。

    真实项目中第 3 步通常会交给大模型，并要求模型引用证据。
    """
    chunks = [chunk for doc in documents for chunk in chunk_document(doc)]
    hits = semantic_search(question, chunks, top_k=2)
    evidence = [chunk for _, chunk in hits]
    return {
        "question": question,
        "evidence": evidence,
        "answer": " ".join(evidence),
    }


def run() -> dict[str, object]:
    """运行第 10 课演示：基于知识库片段回答问题。"""
    docs = [
        "Access policy: project documents can only be searched by project members.",
        "Cost policy: cache repeated questions and limit very long inputs.",
    ]
    return {"title": TITLE, "qa": answer_with_retrieval("Who can search project documents?", docs)}

def main() -> None:
    """Run this chapter as an independent script."""
    from ai_study.chapter_output import print_result

    print_result(run())


if __name__ == "__main__":
    main()