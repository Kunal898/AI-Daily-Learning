"""Standalone Quiz Generator engine."""

from ai_daily_learning.content_bank.quiz_topics import QuizTopicProvider
from ai_daily_learning.models import QuizItem
from ai_daily_learning.utils import setup_logger

logger = setup_logger("quiz_generator")


class QuizGenerator:
    """Generates standalone quizzes for daily practice."""

    def __init__(self) -> None:
        self.provider = QuizTopicProvider()

    def generate(self, day_num: int) -> QuizItem:
        """Generates a QuizItem for the given day number."""
        logger.info(f"Generating Quiz for Day {day_num}...")
        return self.provider.get_quiz(day_num)

    def render_markdown(self, day_num: int) -> str:
        """Renders standalone Quiz Markdown string."""
        quiz = self.generate(day_num)
        lines = [
            f"# 🧠 Daily Quiz - Day {day_num}",
            "",
            f"**Question:** {quiz.question}",
            ""
        ]
        for opt in quiz.options:
            lines.append(f"- {opt}")

        lines.extend([
            "",
            "<details>",
            "<summary><b>Reveal Answer</b></summary>",
            "",
            f"**Correct Option:** `{quiz.correct_option}`",
            "",
            f"**Explanation:** {quiz.explanation}",
            "</details>"
        ])
        return "\n".join(lines)
