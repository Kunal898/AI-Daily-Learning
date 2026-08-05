"""Daily content generation orchestrator."""

from datetime import date
from pathlib import Path
from typing import Optional
from ai_daily_learning.config import OUTPUT_DIR
from ai_daily_learning.content_bank import (
    PythonTopicProvider,
    SQLTopicProvider,
    CybersecurityTopicProvider,
    DataAnalysisTopicProvider,
    LinuxTopicProvider,
    GitTopicProvider,
    NetworkingTopicProvider,
    DockerTopicProvider,
    MLTopicProvider,
    ChallengeTopicProvider,
    InterviewTopicProvider,
    QuizTopicProvider,
)
from ai_daily_learning.generators.template_engine import TemplateEngine
from ai_daily_learning.models import DailyLesson
from ai_daily_learning.utils import calculate_day_number, parse_date_str, setup_logger

logger = setup_logger("daily_generator")


class DailyGenerator:
    """Orchestrates daily educational lesson compilation across all 11 domains."""

    def __init__(self, output_dir: Path = OUTPUT_DIR) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.template_engine = TemplateEngine()

        # Initialize domain content providers
        self.providers = {
            "Python": PythonTopicProvider(),
            "SQL": SQLTopicProvider(),
            "Cybersecurity": CybersecurityTopicProvider(),
            "Data Analysis": DataAnalysisTopicProvider(),
            "Linux": LinuxTopicProvider(),
            "Git": GitTopicProvider(),
            "Networking": NetworkingTopicProvider(),
            "Docker": DockerTopicProvider(),
            "Machine Learning": MLTopicProvider(),
            "Interview Questions": InterviewTopicProvider(),
        }
        self.challenge_provider = ChallengeTopicProvider()
        self.quiz_provider = QuizTopicProvider()

    def generate_lesson(self, target_date: Optional[date] = None, force_day_num: Optional[int] = None) -> Path:
        """Generates a complete daily lesson Markdown file for the specified date or day index."""
        if target_date is None:
            target_date = date.today()

        date_str = target_date.strftime("%Y-%m-%d")
        day_num = force_day_num if force_day_num is not None else calculate_day_number(target_date)

        logger.info(f"Generating daily lesson for {date_str} (Day {day_num}/365)...")

        # Collect topic content from all providers
        topics = {}
        for domain, provider in self.providers.items():
            topics[domain] = provider.get_topic(day_num)

        quiz = self.quiz_provider.get_quiz(day_num)
        challenge = self.challenge_provider.get_challenge(day_num)

        lesson = DailyLesson(
            date_str=date_str,
            day_num=day_num,
            topics=topics,
            quiz=quiz,
            challenge=challenge
        )

        markdown_content = self.template_engine.render_daily_lesson(lesson)
        file_path = self.output_dir / f"{date_str}.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        logger.info(f"Successfully created daily lesson at {file_path}")
        return file_path
