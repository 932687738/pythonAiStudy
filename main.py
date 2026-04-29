"""Project index.

Chapters are intended to run independently. This file no longer dispatches to a
shared chapter runner; it only prints the available standalone commands.
"""

from __future__ import annotations

from ai_study.chapter_output import print_result
from ai_study.chapters import CHAPTERS, list_chapters


if __name__ == "__main__":
    print_result(
        [
            {
                "chapter": chapter,
                "title": title,
                "command": f"python -m ai_study.chapters.{CHAPTERS[chapter]}",
            }
            for chapter, title in list_chapters()
        ]
    )
