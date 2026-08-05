"""Tests for index_builder module."""

from pathlib import Path
from ai_daily_learning.generators.daily_generator import DailyGenerator
from ai_daily_learning.indexers.index_builder import IndexBuilder


def test_index_builder(temp_output_dir: Path, tmp_path: Path):
    # Generate sample daily file
    generator = DailyGenerator(output_dir=temp_output_dir)
    generator.generate_lesson(force_day_num=1)

    index_file = tmp_path / "INDEX.md"
    tags_file = tmp_path / "TAGS.md"
    search_json = tmp_path / "search_index.json"

    builder = IndexBuilder(
        output_dir=temp_output_dir,
        index_file=index_file,
        tags_file=tags_file,
        search_index_file=search_json
    )

    result = builder.build_all()
    assert result["total_indexed"] == 1
    assert index_file.exists()
    assert tags_file.exists()
    assert search_json.exists()
