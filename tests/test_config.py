"""Tests for configuration settings."""

from ai_daily_learning.config import DOMAINS, TOTAL_CURRICULUM_DAYS, OUTPUT_DIR


def test_config_domains():
    assert len(DOMAINS) == 12
    assert "Python" in DOMAINS
    assert "SQL" in DOMAINS
    assert "Machine Learning" in DOMAINS


def test_total_curriculum_days():
    assert TOTAL_CURRICULUM_DAYS == 365
