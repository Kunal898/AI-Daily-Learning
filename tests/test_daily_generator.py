"""Tests for daily_generator module."""

from datetime import date
from pathlib import Path
from ai_daily_learning.generators.daily_generator import DailyGenerator


def test_daily_generator_creates_file(temp_output_dir: Path):
    generator = DailyGenerator(output_dir=temp_output_dir)
    target_date = date(2026, 8, 5)

    created_path = generator.generate_lesson(target_date=target_date, force_day_num=245)

    assert created_path.exists()
    assert created_path.name == "2026-08-05.md"

    with open(created_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "# 📚 AI Daily Learning - Day 245 (2026-08-05)" in content
    assert "## 🚀 Domain: Python" in content
    assert "## 🚀 Domain: SQL" in content
    assert "## 🧠 Daily Multiple-Choice Quiz" in content
    assert "## ⚡ Daily Coding Challenge" in content
