"""CLI Entry Point: Build Searchable Indexes.

Usage:
    python build_index.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ai_daily_learning.indexers.index_builder import IndexBuilder
from ai_daily_learning.utils import setup_logger

logger = setup_logger("cli_build_index")


def main() -> None:
    logger.info("Building searchable indexes (INDEX.md, TAGS.md, search_index.json)...")
    builder = IndexBuilder()
    results = builder.build_all()
    logger.info(f"Indexing completed: {results['total_indexed']} total lessons indexed.")


if __name__ == "__main__":
    main()
