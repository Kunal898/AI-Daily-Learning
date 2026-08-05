"""Utility functions for logging, dates, and markdown handling."""

import logging
import re
from datetime import datetime, date
from pathlib import Path
from typing import Optional


def setup_logger(name: str = "ai_daily_learning", level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standard logger instance."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger


def calculate_day_number(target_date: Optional[date] = None) -> int:
    """Computes the 1-365 day index based on the day of the year."""
    if target_date is None:
        target_date = date.today()
    day_of_year = target_date.timetuple().tm_yday
    return ((day_of_year - 1) % 365) + 1


def parse_date_str(date_str: str) -> date:
    """Parses a YYYY-MM-DD string into a datetime.date object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as err:
        raise ValueError(f"Invalid date format '{date_str}'. Expected YYYY-MM-DD.") from err


def count_markdown_words(content: str) -> int:
    """Counts words in a markdown string, stripping code blocks and syntax delimiters."""
    # Remove code blocks
    text = re.sub(r"```[sS]*?```", "", content)
    # Remove headers, links, formatting
    text = re.sub(r"[#*`_~\-\|]", " ", text)
    words = text.split()
    return len(words)
