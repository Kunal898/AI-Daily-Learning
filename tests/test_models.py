"""Tests for Pydantic & Dataclass models."""

from ai_daily_learning.models import TopicContent, QuizItem, ChallengeItem, DailyLesson, RepoStats


def test_topic_content_instantiation(sample_topic_content):
    assert sample_topic_content.domain == "Python"
    assert len(sample_topic_content.key_takeaways) == 2


def test_quiz_item_instantiation(sample_quiz_item):
    assert sample_quiz_item.correct_option == "B"
    assert len(sample_quiz_item.options) == 4


def test_challenge_item_instantiation(sample_challenge_item):
    assert sample_challenge_item.title == "Sum of Elements"
    assert sample_challenge_item.difficulty == "Easy"


def test_daily_lesson_serialization(sample_daily_lesson):
    data = sample_daily_lesson.model_dump()
    assert data["date_str"] == "2026-08-05"
    assert data["day_num"] == 217
    assert "Python" in data["topics"]


def test_repo_stats_defaults():
    stats = RepoStats()
    assert stats.total_lessons == 0
    assert stats.progress_percentage == 0.0
