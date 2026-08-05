"""Calculates repository statistics and metrics."""

from pathlib import Path
from typing import Dict
from ai_daily_learning.config import OUTPUT_DIR, TOTAL_CURRICULUM_DAYS, DOMAINS
from ai_daily_learning.models import RepoStats
from ai_daily_learning.utils import count_markdown_words, setup_logger

logger = setup_logger("stats_calculator")


class StatsCalculator:
    """Computes comprehensive metrics over generated lessons."""

    def __init__(self, output_dir: Path = OUTPUT_DIR) -> None:
        self.output_dir = output_dir

    def calculate(self) -> RepoStats:
        """Parses output directory files to construct a RepoStats instance."""
        files = sorted(self.output_dir.glob("*.md"))
        total_lessons = len(files)
        latest_date = files[-1].stem if files else "None"

        total_words = 0
        domain_counts: Dict[str, int] = {domain: total_lessons for domain in DOMAINS}

        for fpath in files:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            total_words += count_markdown_words(content)

        progress_pct = round((total_lessons / TOTAL_CURRICULUM_DAYS) * 100, 2)

        stats = RepoStats(
            total_lessons=total_lessons,
            latest_lesson_date=latest_date,
            total_words=total_words,
            progress_percentage=progress_pct,
            domain_counts=domain_counts
        )

        logger.info(f"Calculated stats: {total_lessons} lessons ({progress_pct}%), {total_words} words.")
        return stats
