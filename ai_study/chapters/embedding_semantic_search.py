"""第 9 课：Embedding、语义搜索与向量数据库。

真实项目会用模型生成 embedding，并存入向量数据库。
这里用词袋向量模拟 embedding，让检索流程在无模型依赖时仍然可运行。
"""

from __future__ import annotations

from collections import Counter

from ai_study.common import cosine

TITLE = "Embedding, semantic search, and vector database"


def tokenize(text: str) -> list[str]:
    """把文本切成规范化 token。

    真实系统要处理分词、大小写、停用词、同义词等问题；这里保留最小实现。
    """
    return [token.strip(".,:;!?()").lower() for token in text.split() if token.strip(".,:;!?()")]


def vocabulary(texts: list[str]) -> list[str]:
    """从语料构造词表，词表决定词袋向量的每个维度含义。"""
    return sorted({token for text in texts for token in tokenize(text)})


def embed(text: str, vocab: list[str]) -> list[float]:
    """把文本转成词袋向量。

    向量第 i 维表示词表中第 i 个词出现了多少次。
    虽然它不是真正的语义 embedding，但足够演示“文本 -> 向量 -> 相似度检索”的流程。
    """
    counts = Counter(tokenize(text))
    return [float(counts[word]) for word in vocab]


def semantic_search(query: str, documents: list[str], top_k: int = 2) -> list[tuple[float, str]]:
    """对文档做相似度检索，返回最相关的 top_k 条。

    真实向量库会提前存储文档向量，并使用索引加速近邻搜索。
    这里每次临时计算，是为了让流程更透明。
    """
    vocab = vocabulary(documents + [query])
    q = embed(query, vocab)
    scored = [(cosine(q, embed(doc, vocab)), doc) for doc in documents]
    return sorted(scored, reverse=True)[:top_k]


def run() -> dict[str, object]:
    """运行第 9 课演示：用一个查询检索最相关文档。"""
    docs = [
        "Vector databases store embeddings for semantic search.",
        "Linear regression predicts numeric prices.",
        "RAG retrieves documents before answering questions.",
    ]
    return {"title": TITLE, "results": [(round(score, 4), doc) for score, doc in semantic_search("document question retrieval", docs)]}
