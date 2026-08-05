"""Tests for CLI entrypoint scripts."""

import subprocess
import sys


def test_cli_stats():
    result = subprocess.run([sys.executable, "stats.py", "--json"], capture_output=True, text=True)
    assert result.returncode == 0
    assert '"total_lessons"' in result.stdout


def test_cli_quiz_generator():
    result = subprocess.run([sys.executable, "quiz_generator.py", "--day-num", "1"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Daily Quiz" in result.stdout


def test_cli_challenge_generator():
    result = subprocess.run([sys.executable, "challenge_generator.py", "--day-num", "1"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Coding Challenge" in result.stdout
