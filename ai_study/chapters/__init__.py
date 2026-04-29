"""章节注册表和统一运行入口。

每个课程章节都实现成一个独立模块，并在 ``CHAPTERS`` 中登记章节号和模块名。
这样 ``main.py`` 不需要知道每章文件叫什么，只需要调用 ``run_chapter("03")``。

如果以后新增第 27 课，只需要：
1. 在 ``ai_study/chapters`` 下新增模块；
2. 在 ``CHAPTERS`` 中增加 ``"27": "module_name"``；
3. 确保新模块提供 ``TITLE`` 和 ``run()``。
"""

from __future__ import annotations

from importlib import import_module

CHAPTERS: dict[str, str] = {
    "00": "ai_overview",
    "01": "python_ai_environment",
    "02": "ai_math_foundation",
    "03": "machine_learning_workflow",
    "04": "supervised_learning",
    "05": "unsupervised_feature_engineering",
    "06": "deep_learning_basics",
    "07": "cnn_rnn_transformer_intro",
    "08": "llm_token_prompt_engineering",
    "09": "embedding_semantic_search",
    "10": "rag_knowledge_base_qa",
    "11": "tool_calling_agent",
    "12": "spring_ai_mapping",
    "13": "langchain4j_mapping",
    "14": "java_ai_engineering_mapping",
    "15": "advanced_linalg_spectral",
    "16": "advanced_low_rank_peft",
    "17": "advanced_variational_flows",
    "18": "advanced_optimization",
    "19": "advanced_transformer_mechanisms",
    "20": "advanced_moe",
    "21": "advanced_ssm_rwkv",
    "22": "advanced_diffusion_flow_matching",
    "23": "advanced_alignment",
    "24": "advanced_inference_systems",
    "25": "advanced_representation_learning",
    "26": "advanced_interpretability",
}


def load(chapter: str):
    """按章节号动态导入模块。

    ``zfill(2)`` 允许用户输入 ``3`` 或 ``03``，都能定位到第 3 课。
    动态导入让章节模块保持懒加载：只有真正运行某一章时才加载对应代码。
    """
    key = chapter.zfill(2)
    if key not in CHAPTERS:
        raise KeyError(f"unknown chapter: {chapter}")
    return import_module(f"{__name__}.{CHAPTERS[key]}")


def list_chapters() -> list[tuple[str, str]]:
    """返回所有已登记章节的编号和标题。"""
    rows = []
    for key in sorted(CHAPTERS):
        module = load(key)
        rows.append((key, getattr(module, "TITLE", CHAPTERS[key])))
    return rows


def run_chapter(chapter: str):
    """运行指定章节的 ``run()`` 演示函数。"""
    module = load(chapter)
    return module.run()
