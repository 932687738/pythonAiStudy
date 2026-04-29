"""Chapter registry.

Each course chapter is implemented as an independent module. The registry is
kept only for indexing, documentation, and tests; chapter examples should be
run directly, for example:

``python -m ai_study.chapters.machine_learning_workflow``

To add a new chapter:
1. Add a module under ``ai_study/chapters``.
2. Register the module name in ``CHAPTERS``.
3. Provide ``TITLE`` and ``run()`` in the new module.
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
    """Load a chapter module by number."""
    key = chapter.zfill(2)
    if key not in CHAPTERS:
        raise KeyError(f"unknown chapter: {chapter}")
    return import_module(f"{__name__}.{CHAPTERS[key]}")


def list_chapters() -> list[tuple[str, str]]:
    """Return registered chapter numbers and titles."""
    rows = []
    for key in sorted(CHAPTERS):
        module = load(key)
        rows.append((key, getattr(module, "TITLE", CHAPTERS[key])))
    return rows


def run_chapter(chapter: str):
    """Run a chapter for tests or programmatic use.

    Command-line usage should prefer each chapter's own module entry.
    """
    module = load(chapter)
    return module.run()
