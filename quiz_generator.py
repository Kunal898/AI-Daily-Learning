"""CLI Entry Point: Standalone Daily Quiz Generator.

Usage:
    python quiz_generator.py
    python quiz_generator.py --day-num 10
"""

import argparse
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows stdout
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ai_daily_learning.generators.quiz_generator import QuizGenerator
from ai_daily_learning.utils import calculate_day_number


def main() -> None:
    parser = argparse.ArgumentParser(description="Standalone Quiz Generator")
    parser.add_argument("--day-num", type=int, help="Curriculum day index (1-365)")
    args = parser.parse_args()

    day_num = args.day_num if args.day_num is not None else calculate_day_number()
    generator = QuizGenerator()
    md_output = generator.render_markdown(day_num)
    print(md_output)


if __name__ == "__main__":
    main()
