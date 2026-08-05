"""Updates README.md dynamically with badges, progress stats, and curriculum tables."""

import re
from pathlib import Path
from typing import Optional
from ai_daily_learning.config import README_FILE, OUTPUT_DIR
from ai_daily_learning.stats.stats_calculator import StatsCalculator
from ai_daily_learning.utils import setup_logger

logger = setup_logger("readme_updater")

STATS_START_MARKER = "<!-- STATS:START -->"
STATS_END_MARKER = "<!-- STATS:END -->"


class ReadmeUpdater:
    """Modifies README.md with live statistical data and progress indicators."""

    def __init__(self, readme_path: Path = README_FILE, output_dir: Path = OUTPUT_DIR) -> None:
        self.readme_path = readme_path
        self.stats_calculator = StatsCalculator(output_dir=output_dir)

    def update(self) -> None:
        """Calculates metrics and injects updated stats into README.md."""
        stats = self.stats_calculator.calculate()

        if not self.readme_path.exists():
            logger.warning(f"README file not found at {self.readme_path}. Creating new README...")
            self._create_base_readme()

        with open(self.readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        stats_block = self._generate_stats_markdown(stats)

        pattern = re.compile(
            rf"{re.escape(STATS_START_MARKER)}[\s\S]*?{re.escape(STATS_END_MARKER)}",
            re.MULTILINE
        )

        new_content = pattern.sub(f"{STATS_START_MARKER}\n{stats_block}\n{STATS_END_MARKER}", content)

        with open(self.readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info("README.md statistics updated successfully.")

    def _generate_stats_markdown(self, stats) -> str:
        filled = int(stats.progress_percentage // 5)
        bar = "█" * filled + "░" * (20 - filled)

        latest_link = f"[{stats.latest_lesson_date}](output/{stats.latest_lesson_date}.md)" if stats.latest_lesson_date != "None" else "None"

        lines = [
            "### 📊 Live Learning Statistics",
            "",
            f"![Total Lessons](https://img.shields.io/badge/Total_Lessons-{stats.total_lessons}-blue?style=for-the-badge&logo=book)",
            f"![Progress](https://img.shields.io/badge/Progress-{stats.progress_percentage}%25-brightgreen?style=for-the-badge&logo=github)",
            f"![Total Words](https://img.shields.io/badge/Words_Generated-{stats.total_words}-purple?style=for-the-badge)",
            "",
            f"**Curriculum Progress:** `[{bar}] {stats.progress_percentage}%` (Target: 365 Days)",
            "",
            "| Metric | Value |",
            "| --- | --- |",
            f"| 📚 **Total Lessons** | `{stats.total_lessons}` / 365 |",
            f"| 📅 **Latest Lesson** | {latest_link} |",
            f"| 📝 **Total Words Written** | `{stats.total_words:,}` words |",
            f"| 🎯 **Progress Percentage** | `{stats.progress_percentage}%` |",
            f"| 🌐 **Domains Covered** | `11 Core Tech Domains` |",
            "",
            "#### 📂 Domain Module Breakdown",
            "| Technical Domain | Lessons Generated | Status |",
            "| --- | --- | --- |"
        ]

        for domain, count in stats.domain_counts.items():
            status = "🟢 Active" if count > 0 else "⚪ Scheduled"
            lines.append(f"| {domain} | `{count}` lessons | {status} |")

        return "\n".join(lines)

    def _create_base_readme(self) -> None:
        base_content = f"""# 🚀 AI-Daily-Learning

> An automated daily educational knowledge base generating real, production-ready educational content across 11 technical domains every single day using Python 3.12, Clean Architecture, and GitHub Actions.

{STATS_START_MARKER}
{STATS_END_MARKER}

## 🎯 Repository Overview

This repository automatically generates comprehensive daily markdown lessons covering:
1. 🐍 **Python 3.12** (Advanced typing, Asyncio, Patterns, GIL, Metaclasses)
2. 🗄️ **SQL** (Window functions, Recursive CTEs, Execution Plans, Indexing)
3. 🔒 **Cybersecurity** (OWASP Top 10, JWT Security, Cryptography, Hardening)
4. 📊 **Data Analysis** (Polars, Pandas, Vectorized NumPy, Time-Series)
5. 🐧 **Linux** (Sysadmin commands, awk/sed masterclass, Systemd, Profiling)
6. 🔀 **Git** (Worktrees, Interactive Rebase, Reflog recovery, Submodules)
7. 🌐 **Networking** (TLS 1.3, TCP/IP, DNS, HTTP/3, Socket programming)
8. 🐳 **Docker** (Multi-stage builds, Security, Compose, Image layer optimization)
9. 🤖 **Machine Learning** (Attention mechanism, Transformers, Quantization, PyTorch)
10. ⚡ **Coding Challenges** (Algorithms with test cases & clean solutions)
11. 🧠 **Interview Questions & Quizzes** (STAR method responses & MCQs with answer keys)

## 📁 Repository Structure

- `output/`: Daily generated markdown files (`YYYY-MM-DD.md`).
- `src/ai_daily_learning/`: Python package implementing OOP generators & indexers.
- `generate.py`: Main CLI tool to trigger daily content generation.
- `update_readme.py`: CLI tool to sync statistics and dynamic badges.
- `build_index.py`: CLI tool to compile `INDEX.md` and `search_index.json`.
- `stats.py`: CLI tool to display analytics.
- `quiz_generator.py` & `challenge_generator.py`: Standalone CLI practice tools.

## 🛠️ Local Usage

```bash
# Install dependencies
pip install -e .

# Generate today's daily lesson
python generate.py

# Update README and search index
python update_readme.py
python build_index.py
```

## ⚙️ Automated GitHub Actions Workflow

This repository runs automatically every day at `00:00 UTC` via GitHub Actions (`.github/workflows/daily_generate.yml`). It generates the daily content, updates the master `INDEX.md` and `README.md`, and commits the changes back to the repository.

---
*License: MIT | Maintained by AI-Daily-Learning Team*
"""
        with open(self.readme_path, "w", encoding="utf-8") as f:
            f.write(base_content)
