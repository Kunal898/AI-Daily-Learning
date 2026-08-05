"""Pytest fixtures for AI Daily Learning tests."""

import pytest
from pathlib import Path
from datetime import date
from ai_daily_learning.models import TopicContent, QuizItem, ChallengeItem, DailyLesson


@pytest.fixture
def temp_output_dir(tmp_path: Path) -> Path:
    """Fixture providing a temporary output directory."""
    out = tmp_path / "output"
    out.mkdir(parents=True, exist_ok=True)
    return out


@pytest.fixture
def sample_topic_content() -> TopicContent:
    """Fixture providing a sample TopicContent instance."""
    return TopicContent(
        domain="Python",
        topic_name="Type Hints in Python 3.12",
        difficulty="Intermediate",
        concept_summary="Overview of type hints.",
        code_example="x: int = 10",
        key_takeaways=["Use static typing for safety.", "Integrate with mypy."]
    )


@pytest.fixture
def sample_quiz_item() -> QuizItem:
    """Fixture providing a sample QuizItem instance."""
    return QuizItem(
        question="What is 2 + 2?",
        options=["A) 3", "B) 4", "C) 5", "D) 22"],
        correct_option="B",
        explanation="2 + 2 equals 4 arithmetic sum."
    )


@pytest.fixture
def sample_challenge_item() -> ChallengeItem:
    """Fixture providing a sample ChallengeItem instance."""
    return ChallengeItem(
        title="Sum of Elements",
        difficulty="Easy",
        description="Return sum of integer list.",
        starter_code="def sum_list(nums: list[int]) -> int:\n    pass",
        test_cases=["assert sum_list([1, 2]) == 3"],
        solution="def sum_list(nums: list[int]) -> int:\n    return sum(nums)"
    )


@pytest.fixture
def sample_daily_lesson(sample_topic_content, sample_quiz_item, sample_challenge_item) -> DailyLesson:
    """Fixture providing a complete DailyLesson instance."""
    return DailyLesson(
        date_str="2026-08-05",
        day_num=217,
        topics={"Python": sample_topic_content},
        quiz=sample_quiz_item,
        challenge=sample_challenge_item
    )
