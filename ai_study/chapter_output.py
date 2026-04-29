"""Shared output formatting for standalone chapter scripts."""

from __future__ import annotations

import json
from typing import Any


def print_result(value: Any) -> None:
    """Print a chapter result as readable JSON.

    Chapter files call this helper only for display formatting. Each chapter still
    owns its own standalone script entry under ``if __name__ == "__main__"``.
    """
    print(json.dumps(value, ensure_ascii=False, indent=2))
