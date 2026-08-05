"""Content bank package containing modular topic generators for all 11 domains."""

from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.content_bank.python_topics import PythonTopicProvider
from ai_daily_learning.content_bank.sql_topics import SQLTopicProvider
from ai_daily_learning.content_bank.cybersecurity_topics import CybersecurityTopicProvider
from ai_daily_learning.content_bank.data_analysis_topics import DataAnalysisTopicProvider
from ai_daily_learning.content_bank.linux_topics import LinuxTopicProvider
from ai_daily_learning.content_bank.git_topics import GitTopicProvider
from ai_daily_learning.content_bank.networking_topics import NetworkingTopicProvider
from ai_daily_learning.content_bank.docker_topics import DockerTopicProvider
from ai_daily_learning.content_bank.ml_topics import MLTopicProvider
from ai_daily_learning.content_bank.challenge_topics import ChallengeTopicProvider
from ai_daily_learning.content_bank.interview_topics import InterviewTopicProvider
from ai_daily_learning.content_bank.quiz_topics import QuizTopicProvider

__all__ = [
    "BaseTopicProvider",
    "PythonTopicProvider",
    "SQLTopicProvider",
    "CybersecurityTopicProvider",
    "DataAnalysisTopicProvider",
    "LinuxTopicProvider",
    "GitTopicProvider",
    "NetworkingTopicProvider",
    "DockerTopicProvider",
    "MLTopicProvider",
    "ChallengeTopicProvider",
    "InterviewTopicProvider",
    "QuizTopicProvider",
]
