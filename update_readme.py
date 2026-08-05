"""CLI Entry Point: Update README Statistics & Dynamic Badges.

Usage:
    python update_readme.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ai_daily_learning.stats.readme_updater import ReadmeUpdater
from ai_daily_learning.utils import setup_logger

logger = setup_logger("cli_update_readme")


def main() -> None:
    logger.info("Updating README.md statistics and dynamic badges...")
    updater = ReadmeUpdater()
    updater.update()
    logger.info("README.md updated successfully.")


if __name__ == "__main__":
    main()
