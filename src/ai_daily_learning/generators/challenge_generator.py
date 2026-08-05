"""Standalone Challenge Generator engine."""

from ai_daily_learning.content_bank.challenge_topics import ChallengeTopicProvider
from ai_daily_learning.models import ChallengeItem
from ai_daily_learning.utils import setup_logger

logger = setup_logger("challenge_generator")


class ChallengeGenerator:
    """Generates standalone coding challenges for practice."""

    def __init__(self) -> None:
        self.provider = ChallengeTopicProvider()

    def generate(self, day_num: int) -> ChallengeItem:
        """Generates a ChallengeItem for the given day number."""
        logger.info(f"Generating Challenge for Day {day_num}...")
        return self.provider.get_challenge(day_num)

    def render_markdown(self, day_num: int) -> str:
        """Renders standalone Challenge Markdown string."""
        challenge = self.generate(day_num)
        lines = [
            f"# ⚡ Coding Challenge - Day {day_num}: {challenge.title}",
            f"**Difficulty:** `{challenge.difficulty}`",
            "",
            "## Description",
            challenge.description,
            "",
            "## Starter Code",
            "```python",
            challenge.starter_code,
            "```",
            "",
            "## Test Cases",
            "```python"
        ]
        for t in challenge.test_cases:
            lines.append(t)
        lines.extend([
            "```",
            "",
            "<details>",
            "<summary><b>View Solution</b></summary>",
            "",
            "```python",
            challenge.solution,
            "```",
            "</details>"
        ])
        return "\n".join(lines)
