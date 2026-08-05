"""Tests for readme_updater module."""

from pathlib import Path
from ai_daily_learning.stats.readme_updater import ReadmeUpdater


def test_readme_updater_creation(tmp_path: Path):
    readme_path = tmp_path / "README.md"
    updater = ReadmeUpdater(readme_path=readme_path)
    updater.update()

    assert readme_path.exists()
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "# 🚀 AI-Daily-Learning" in content
    assert "Live Learning Statistics" in content
