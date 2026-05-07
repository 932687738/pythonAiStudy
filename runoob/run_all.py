"""Run all Runoob tutorial tasks in order.

Usage:
    python run_all.py
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TASKS_FILE = ROOT / "TASKS.md"
REPORT_FILE = ROOT / "RUN_ALL_REPORT.md"


@dataclass
class TaskResult:
    """Store one task execution result."""

    index: str
    file_name: str
    return_code: int
    stdout: str
    stderr: str

    @property
    def passed(self) -> bool:
        """Return whether the task completed successfully."""
        return self.return_code == 0


def read_task_files() -> list[tuple[str, str]]:
    """Read ordered task file names from TASKS.md."""
    tasks: list[tuple[str, str]] = []
    for line in TASKS_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 4:
            continue
        index, _title, file_name, _status = parts
        if index.isdigit() and file_name.endswith(".py"):
            tasks.append((index, file_name))
    return tasks


def run_task(index: str, file_name: str) -> TaskResult:
    """Run a single task file with the current Python interpreter."""
    file_path = ROOT / file_name
    process = subprocess.run(
        [sys.executable, str(file_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return TaskResult(
        index=index,
        file_name=file_name,
        return_code=process.returncode,
        stdout=process.stdout,
        stderr=process.stderr,
    )


def write_report(results: list[TaskResult]) -> None:
    """Write a Markdown execution report."""
    lines = [
        "# Runoob 批量运行报告",
        "",
        f"- Python: `{sys.executable}`",
        f"- 总任务数: {len(results)}",
        f"- 成功: {sum(result.passed for result in results)}",
        f"- 失败: {sum(not result.passed for result in results)}",
        "",
        "| 序号 | 文件名 | 状态 | 返回码 |",
        "|---|---|---|---|",
    ]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        lines.append(f"| {result.index} | {result.file_name} | {status} | {result.return_code} |")

    failed_results = [result for result in results if not result.passed]
    if failed_results:
        lines.extend(["", "## 失败详情", ""])
        for result in failed_results:
            lines.extend(
                [
                    f"### {result.index} {result.file_name}",
                    "",
                    "标准输出:",
                    "",
                    "```text",
                    result.stdout.strip(),
                    "```",
                    "",
                    "标准错误:",
                    "",
                    "```text",
                    result.stderr.strip(),
                    "```",
                    "",
                ]
            )

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Run all tutorial tasks and generate a report."""
    tasks = read_task_files()
    if not tasks:
        raise RuntimeError(f"No tasks found in {TASKS_FILE}")

    results: list[TaskResult] = []
    for index, file_name in tasks:
        print(f"[{index}] running {file_name} ...", flush=True)
        result = run_task(index, file_name)
        results.append(result)
        status = "PASS" if result.passed else "FAIL"
        print(f"[{index}] {status}", flush=True)

    write_report(results)
    failed_count = sum(not result.passed for result in results)
    print(f"Report written to: {REPORT_FILE}")
    if failed_count:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
