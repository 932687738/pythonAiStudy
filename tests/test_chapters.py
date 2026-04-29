"""Smoke tests for all chapter examples."""

from __future__ import annotations

import unittest
from pathlib import Path

from ai_study.chapters import list_chapters, run_chapter


class ChapterSmokeTest(unittest.TestCase):
    """确保章节注册表中的每个章节都能返回结构化结果。"""

    def test_all_chapters_run(self) -> None:
        """逐章调用 ``run()``，检查返回值至少包含标题。"""
        chapters = list_chapters()
        self.assertEqual(27, len(chapters))
        for chapter, _ in chapters:
            with self.subTest(chapter=chapter):
                result = run_chapter(chapter)
                self.assertIsInstance(result, dict)
                self.assertIn("title", result)

    def test_each_chapter_has_standalone_main(self) -> None:
        """每个章节文件都应该有自己的独立 ``main()`` 入口。"""
        chapter_dir = Path(__file__).resolve().parents[1] / "ai_study" / "chapters"
        for path in chapter_dir.glob("*.py"):
            if path.name == "__init__.py":
                continue
            with self.subTest(file=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertIn("def main() -> None:", text)
                self.assertIn('if __name__ == "__main__":', text)


if __name__ == "__main__":
    unittest.main()
