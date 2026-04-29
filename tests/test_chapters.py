"""Smoke tests for all chapter examples."""

from __future__ import annotations

import unittest

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


if __name__ == "__main__":
    unittest.main()
