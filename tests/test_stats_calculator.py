"""Tests for stats_calculator module."""

from pathlib import Path
from ai_daily_learning.generators.daily_generator import DailyGenerator
from ai_daily_learning.stats.stats_calculator import StatsCalculator


def test_stats_calculator(temp_output_dir: Path):
    generator = DailyGenerator(output_dir=temp_output_dir)
    generator.generate_lesson(force_day_num=10)

    calculator = StatsCalculator(output_dir=temp_output_dir)
    stats = calculator.calculate()

    assert stats.total_lessons == 1
    assert stats.total_words > 100
    assert stats.progress_percentage == round((1 / 365) * 100, 2)
