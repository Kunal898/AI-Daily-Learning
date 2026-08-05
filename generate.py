"""CLI Entry Point: Generate Daily Educational Content.

Usage:
    python generate.py
    python generate.py --date 2026-08-05
    python generate.py --day-num 245
"""

import argparse
import sys
from datetime import date
from pathlib import Path

# Add src to python path for standalone execution
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ai_daily_learning.generators.daily_generator import DailyGenerator
from ai_daily_learning.utils import parse_date_str, setup_logger

logger = setup_logger("cli_generate")


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Daily Learning Content Generator")
    parser.add_argument("--date", type=str, help="Target date in YYYY-MM-DD format (default: today)")
    parser.add_argument("--day-num", type=int, help="Override curriculum day number (1-365)")

    args = parser.parse_args()

    target_date: date = parse_date_str(args.date) if args.date else date.today()
    
    generator = DailyGenerator()
    generated_path = generator.generate_lesson(target_date=target_date, force_day_num=args.day_num)
    
    logger.info(f"Successfully generated lesson: {generated_path}")


if __name__ == "__main__":
    main()
