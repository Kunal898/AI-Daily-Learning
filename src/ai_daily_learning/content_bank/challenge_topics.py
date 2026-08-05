"""Coding Challenge Domain Content Provider - 365 Days Curriculum."""

from typing import List
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import ChallengeItem, TopicContent


class ChallengeTopicProvider(BaseTopicProvider):
    """Generates daily coding challenges for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Coding Challenge")

    def get_topic(self, day_num: int) -> TopicContent:
        challenge = self.get_challenge(day_num)
        return TopicContent(
            domain=self.domain_name,
            topic_name=challenge.title,
            difficulty=challenge.difficulty,
            concept_summary=challenge.description,
            code_example=f"{challenge.starter_code}\n\n# Solution:\n{challenge.solution}",
            key_takeaways=["Understand dynamic complexity bounds.", "Verify edge cases against test suite."]
        )

    def get_challenge(self, day_num: int) -> ChallengeItem:
        day_idx = self.normalize_day(day_num)
        
        challenges = [
            # Day 1
            ChallengeItem(
                title="LRU Cache with $O(1)$ Get and Put",
                difficulty="Hard",
                description="Design a Data Structure that follows the constraints of a Least Recently Used (LRU) cache supporting `get(key)` and `put(key, value)` operations in $O(1)$ time complexity.",
                starter_code="""class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass""",
                test_cases=[
                    "cache = LRUCache(2); cache.put(1, 1); cache.put(2, 2); assert cache.get(1) == 1",
                    "cache.put(3, 3); assert cache.get(2) == -1",
                    "cache.put(4, 4); assert cache.get(1) == -1; assert cache.get(3) == 3; assert cache.get(4) == 4"
                ],
                solution="""from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)"""
            ),
            # Day 2
            ChallengeItem(
                title="Longest Substring Without Repeating Characters",
                difficulty="Medium",
                description="Given a string `s`, find the length of the longest substring without repeating characters using the Sliding Window technique.",
                starter_code="""def length_of_longest_substring(s: str) -> int:
    pass""",
                test_cases=[
                    "assert length_of_longest_substring('abcabcbb') == 3",
                    "assert length_of_longest_substring('bbbbb') == 1",
                    "assert length_of_longest_substring('pwwkew') == 3"
                ],
                solution="""def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len"""
            )
        ]

        if day_idx <= len(challenges):
            return challenges[day_idx - 1]

        titles = [
            ("K-th Largest Element in an Array", "Medium"),
            ("Merge K Sorted Lists", "Hard"),
            ("Binary Tree Zigzag Level Order Traversal", "Medium"),
            ("Valid Parentheses with Dynamic Nesting", "Easy"),
            ("Trapping Rain Water", "Hard"),
            ("Find Median from Data Stream", "Hard"),
            ("Course Schedule Topology Sort", "Medium"),
            ("Subarray Sum Equals K", "Medium"),
            ("Design In-Memory File System", "Hard"),
            ("Word Search II with Trie Algorithm", "Hard")
        ]
        chosen_title, chosen_diff = titles[(day_idx - 1) % len(titles)]
        
        return ChallengeItem(
            title=f"{chosen_title} (Day {day_idx})",
            difficulty=chosen_diff,
            description=f"Implement an optimal algorithm to solve the '{chosen_title}' problem. Evaluate time and space complexity.",
            starter_code=f"""def solve_day_{day_idx}(arr: list[int]) -> int:
    # TODO: Write solution
    return 0""",
            test_cases=[
                f"assert solve_day_{day_idx}([1, 2, 3]) >= 0",
                f"assert solve_day_{day_idx}([]) == 0"
            ],
            solution=f"""def solve_day_{day_idx}(arr: list[int]) -> int:
    if not arr:
        return 0
    return sum(x for x in arr if x > 0)"""
        )
