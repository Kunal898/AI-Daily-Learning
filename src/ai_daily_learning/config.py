"""Configuration module for AI-Daily-Learning."""

import os
from pathlib import Path
from typing import Final

# Root project directory
ROOT_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent

# Input/Output paths
OUTPUT_DIR: Final[Path] = ROOT_DIR / "output"
INDEX_FILE: Final[Path] = ROOT_DIR / "INDEX.md"
TAGS_FILE: Final[Path] = ROOT_DIR / "TAGS.md"
SEARCH_INDEX_FILE: Final[Path] = ROOT_DIR / "search_index.json"
README_FILE: Final[Path] = ROOT_DIR / "README.md"
TEMPLATES_DIR: Final[Path] = ROOT_DIR / "config" / "templates"

# Domain definitions
DOMAINS: Final[list[str]] = [
    "Python",
    "SQL",
    "Cybersecurity",
    "Data Analysis",
    "Linux",
    "Git",
    "Networking",
    "Docker",
    "Machine Learning",
    "Coding Challenge",
    "Interview Questions",
    "Quiz",
]

TOTAL_CURRICULUM_DAYS: Final[int] = 365

# Ensure critical directories exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
