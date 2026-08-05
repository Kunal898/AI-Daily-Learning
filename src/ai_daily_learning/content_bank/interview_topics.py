"""Interview Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class InterviewTopicProvider(BaseTopicProvider):
    """Generates rich Tech Interview Questions & Answers for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Interview Questions")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "How do you design a high-availability Distributed Rate Limiter?",
                "Advanced",
                "**Question:** System Design Interview: Explain how to design a distributed rate limiter (e.g. Token Bucket / Sliding Window Log) capable of handling millions of requests per second with low latency.",
                """# Python Redis Sliding Window Counter Implementation Concept
import time
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def is_rate_limited(user_id: str, limit: int = 100, window_seconds: int = 60) -> bool:
    current_time = time.time()
    pipeline = r.pipeline()
    key = f"rate_limit:{user_id}"
    
    # Remove older entries outside window
    pipeline.zremrangebyscore(key, 0, current_time - window_seconds)
    # Add current timestamp
    pipeline.zadd(key, {str(current_time): current_time})
    # Count requests in window
    pipeline.zcard(key)
    # Set TTL on key
    pipeline.expire(key, window_seconds)
    
    results = pipeline.execute()
    request_count = results[2]
    
    return request_count > limit""",
                [
                    "**Situation & Task:** Scale API infrastructure to prevent DDoS and API quota abuse.",
                    "**Action:** Implement Redis Sorted Sets (ZSET) for precise sliding window rate limiting across distributed web nodes.",
                    "**Result:** Sub-millisecond latency checks with zero race conditions when using Redis Lua scripts."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            questions = [
                "What is the difference between Process and Thread context switching overhead?",
                "Explain database connection pooling and how to prevent connection exhaustion.",
                "How does Garbage Collection operate in Python vs Java vs Go?",
                "Design a URL Shortener Service (e.g., TinyURL) with Base62 Encoding.",
                "Explain the CAP Theorem and PACELC extension with real-world database examples.",
                "What happens step-by-step when you type `https://google.com` into your browser address bar?",
                "How do you handle Deadlocks in distributed database systems?",
                "Explain Microservices Saga Pattern (Choreography vs Orchestration) for distributed transactions.",
                "What is the difference between Hard Links and Soft (Symbolic) Links in Linux file systems?",
                "How do you debug a memory leak in a production Python asynchronous service?"
            ]
            selected = questions[(day_idx - 1) % len(questions)]
            title = f"{selected} (Day {day_idx})"
            diff = "Advanced" if day_idx % 2 == 0 else "Intermediate"
            concept = f"**System Architecture & Coding Interview Focus:** {selected}\n\nKey evaluation criteria: Clear problem decomposition, edge case awareness, and performance trade-off analysis."
            code = f"""# Interview Code Demonstration Day {day_idx}: {selected}

def demonstrate_solution() -> str:
    return "Structured response following STAR method: Situation, Task, Action, Result."

print(demonstrate_solution())"""
            takeaways = [
                f"Structure your response logically for: {selected}.",
                "State architectural trade-offs explicitly (e.g. Latency vs Consistency).",
                "Provide code or pseudocode with accurate big-O time/space complexity analysis."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )
