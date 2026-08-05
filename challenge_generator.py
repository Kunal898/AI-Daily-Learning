"""CLI Entry Point: Standalone Daily Challenge Generator.

Usage:
    python challenge_generator.py
    python challenge_generator.py --day-num 15
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

from ai_daily_learning.generators.challenge_generator import ChallengeGenerator
from ai_daily_learning.utils import calculate_day_number


def main() -> None:
    parser = argparse.ArgumentParser(description="Standalone Challenge Generator")
    parser.add_argument("--day-num", type=int, help="Curriculum day index (1-365)")
    args = parser.parse_args()

    day_num = args.day_num if args.day_num is not None else calculate_day_number()
    generator = ChallengeGenerator()
    md_output = generator.render_markdown(day_num)
    print(md_output)


if __name__ == "__main__":
    main()
