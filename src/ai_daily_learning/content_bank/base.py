"""Abstract Base Class for Domain Content Providers."""

from abc import ABC, abstractmethod
from typing import Dict, Any
from ai_daily_learning.models import TopicContent


class BaseTopicProvider(ABC):
    """Abstract interface for all educational domain providers."""

    def __init__(self, domain_name: str):
        self.domain_name = domain_name

    @abstractmethod
    def get_topic(self, day_num: int) -> TopicContent:
        """Returns the topic content for a specific day index (1-365)."""
        pass

    def normalize_day(self, day_num: int) -> int:
        """Ensures day index is bounded between 1 and 365."""
        return ((day_num - 1) % 365) + 1
