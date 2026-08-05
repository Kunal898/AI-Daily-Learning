"""Quiz Domain Content Provider - 365 Days Curriculum."""

from typing import List
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import QuizItem, TopicContent


class QuizTopicProvider(BaseTopicProvider):
    """Generates daily quizzes for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Quiz")

    def get_topic(self, day_num: int) -> TopicContent:
        quiz = self.get_quiz(day_num)
        options_text = "\n".join(quiz.options)
        return TopicContent(
            domain=self.domain_name,
            topic_name=f"Daily Quiz - Day {day_num}",
            difficulty="Intermediate",
            concept_summary=quiz.question,
            code_example=f"Options:\n{options_text}\n\n# Correct Answer: {quiz.correct_option}",
            key_takeaways=[quiz.explanation]
        )

    def get_quiz(self, day_num: int) -> QuizItem:
        day_idx = self.normalize_day(day_num)
        
        quizzes = [
            # Day 1
            QuizItem(
                question="In Python 3.12, what is the primary benefit of using `ParamSpec` in type hints?",
                options=[
                    "A) It speeds up the CPython bytecode execution engine by 20%.",
                    "B) It captures and passes positional and keyword parameter signatures of callables across decorators for static type checkers.",
                    "C) It replaces `asyncio.Future` objects with native C threads.",
                    "D) It automatically converts Python dictionaries into C-structs."
                ],
                correct_option="B",
                explanation="`ParamSpec` (introduced in PEP 612) allows static type checkers like mypy and Pyright to forward parameter types of decorated functions accurately without losing argument signatures."
            ),
            # Day 2
            QuizItem(
                question="Which SQL Window function assigns unique sequential integer ranks to rows, guaranteeing NO gaps in ranking numbers when duplicates occur?",
                options=[
                    "A) RANK()",
                    "B) ROW_NUMBER()",
                    "C) DENSE_RANK()"
                ],
                correct_option="C",
                explanation="`DENSE_RANK()` assigns consecutive integers without leaving gaps when duplicate values share the same rank, unlike `RANK()` which skips numbers after ties."
            )
        ]

        if day_idx <= len(quizzes):
            return quizzes[day_idx - 1]

        questions_pool = [
            ("What command in Linux displays open ports along with holding process names?", ["A) netstat -an", "B) lsof -iTCP -sTCP:LISTEN", "C) ps -ef", "D) top -b"], "B", "lsof -iTCP -sTCP:LISTEN lists all listening TCP sockets and identifies the associated process PIDs."),
            ("In Docker, what is the primary purpose of multi-stage builds?", ["A) To run multiple containers inside a single image.", "B) To separate build-time tooling from the final minimal runtime container.", "C) To automatically push images to Docker Hub.", "D) To bypass image layer caching."], "B", "Multi-stage builds allow developers to keep build tools out of the final production image, reducing image size and attack surface."),
            ("What key benefit does the TLS 1.3 protocol provide over TLS 1.2?", ["A) Uses MD5 hashing for speed.", "B) Reduces connection handshake latency from 2-RTT to 1-RTT.", "C) Allows unencrypted HTTP traffic over port 443.", "D) Removes Diffie-Hellman key exchange."], "B", "TLS 1.3 completes the cryptographic handshake in 1-RTT (or 0-RTT for session resumption), improving performance and security."),
            ("In Git, which command allows you to search for the specific commit that introduced a bug using binary search?", ["A) git reflog", "B) git bisect", "C) git log --grep", "D) git rebase -i"], "B", "git bisect uses binary search through commit history to quickly pinpoint the exact commit that broke tests."),
            ("What does the softmax activation function compute in Machine Learning?", ["A) Normalizes raw output logits into a valid probability distribution summing to 1.", "B) Clips negative values to zero.", "C) Computes the derivative of loss matrix.", "D) Scales data using Z-score standardization."], "A", "Softmax exponentiates and divides logits by their sum to transform raw predictions into a probability distribution."),
        ]
        q_text, opts, correct, expl = questions_pool[(day_idx - 1) % len(questions_pool)]

        return QuizItem(
            question=f"Day {day_idx} Quiz: {q_text}",
            options=opts,
            correct_option=correct,
            explanation=expl
        )
