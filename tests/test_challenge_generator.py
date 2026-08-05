"""Tests for challenge_generator module."""

from ai_daily_learning.generators.challenge_generator import ChallengeGenerator


def test_challenge_generator():
    generator = ChallengeGenerator()
    challenge = generator.generate(day_num=1)
    assert challenge.title == "LRU Cache with $O(1)$ Get and Put"

    markdown = generator.render_markdown(day_num=1)
    assert "# ⚡ Coding Challenge - Day 1" in markdown
    assert "LRUCache" in markdown
