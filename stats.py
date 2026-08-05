"""CLI Entry Point: Repository Statistics & Metrics Counter.

Usage:
    python stats.py
    python stats.py --json
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows stdout
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ai_daily_learning.stats.stats_calculator import StatsCalculator


def main() -> None:
    parser = argparse.ArgumentParser(description="Repository Analytics & Lesson Counter")
    parser.add_argument("--json", action="store_true", help="Output stats in raw JSON format")
    args = parser.parse_args()

    calculator = StatsCalculator()
    stats = calculator.calculate()

    if args.json:
        data = {
            "total_lessons": stats.total_lessons,
            "latest_lesson_date": stats.latest_lesson_date,
            "total_words": stats.total_words,
            "progress_percentage": stats.progress_percentage,
            "domain_counts": stats.domain_counts
        }
        print(json.dumps(data, indent=2))
    else:
        print("\n==========================================")
        print("   AI-DAILY-LEARNING REPO STATISTICS   ")
        print("==========================================")
        print(f" Total Lessons Generated: {stats.total_lessons} / 365")
        print(f" Latest Lesson Date:     {stats.latest_lesson_date}")
        print(f" Total Words Written:    {stats.total_words:,} words")
        print(f" Progress Percentage:    {stats.progress_percentage}%")
        print("------------------------------------------")
        print(" Domain Module Breakdown:")
        for domain, count in stats.domain_counts.items():
            print(f"  - {domain:<20}: {count} lessons")
        print("==========================================\n")


if __name__ == "__main__":
    main()
