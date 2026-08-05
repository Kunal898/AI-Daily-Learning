"""Tests for quiz_generator module."""

from ai_daily_learning.generators.quiz_generator import QuizGenerator


def test_quiz_generator():
    generator = QuizGenerator()
    quiz = generator.generate(day_num=1)
    assert quiz.correct_option == "B"

    markdown = generator.render_markdown(day_num=1)
    assert "# 🧠 Daily Quiz - Day 1" in markdown
    assert "ParamSpec" in markdown
