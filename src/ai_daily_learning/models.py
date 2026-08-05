"""Data models for AI Daily Learning using Pydantic and Dataclasses."""

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class TopicContent(BaseModel):
    """Represents educational content for a single topic within a domain."""

    domain: str
    topic_name: str
    difficulty: str = "Intermediate"
    concept_summary: str
    code_example: str
    key_takeaways: List[str] = Field(default_factory=list)


class QuizItem(BaseModel):
    """Represents a multiple-choice quiz item."""

    question: str
    options: List[str]
    correct_option: str
    explanation: str


class ChallengeItem(BaseModel):
    """Represents a coding challenge with solution and tests."""

    title: str
    difficulty: str = "Medium"
    description: str
    starter_code: str
    test_cases: List[str]
    solution: str


class DailyLesson(BaseModel):
    """Complete daily lesson structure aggregating all 11 domains."""

    date_str: str
    day_num: int
    topics: Dict[str, TopicContent]
    quiz: QuizItem
    challenge: ChallengeItem


@dataclass
class RepoStats:
    """Statistics container for the repository progress."""

    total_lessons: int = 0
    latest_lesson_date: str = "None"
    total_words: int = 0
    progress_percentage: float = 0.0
    domain_counts: Dict[str, int] = field(default_factory=dict)
