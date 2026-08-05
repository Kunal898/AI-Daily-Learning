"""Tests for topic providers and content banks."""

import pytest
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


@pytest.mark.parametrize("day_num", [1, 2, 50, 100, 245, 365])
def test_all_providers_return_valid_content(day_num: int):
    providers = [
        PythonTopicProvider(),
        SQLTopicProvider(),
        CybersecurityTopicProvider(),
        DataAnalysisTopicProvider(),
        LinuxTopicProvider(),
        GitTopicProvider(),
        NetworkingTopicProvider(),
        DockerTopicProvider(),
        MLTopicProvider(),
        InterviewTopicProvider(),
    ]

    for provider in providers:
        topic = provider.get_topic(day_num)
        assert topic.domain == provider.domain_name
        assert len(topic.topic_name) > 0
        assert len(topic.concept_summary) > 0
        assert len(topic.code_example) > 0
        assert len(topic.key_takeaways) > 0


@pytest.mark.parametrize("day_num", [1, 10, 200, 365])
def test_challenge_and_quiz_providers(day_num: int):
    c_provider = ChallengeTopicProvider()
    q_provider = QuizTopicProvider()

    challenge = c_provider.get_challenge(day_num)
    assert len(challenge.title) > 0
    assert len(challenge.starter_code) > 0
    assert len(challenge.solution) > 0

    quiz = q_provider.get_quiz(day_num)
    assert len(quiz.question) > 0
    assert len(quiz.options) == 4
    assert quiz.correct_option in ["A", "B", "C", "D"]
