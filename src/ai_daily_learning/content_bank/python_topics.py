"""Python Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class PythonTopicProvider(BaseTopicProvider):
    """Generates rich Python educational content for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Python")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Advanced Type Annotations & ParamSpec in Python 3.12",
                "Advanced",
                "Python 3.12 introduces enhanced typing features including `ParamSpec` and `Concatenate` for decorating generic callables cleanly without losing parameter signatures.",
                """from typing import Callable, ParamSpec, TypeVar
import functools
import time

P = ParamSpec("P")
R = TypeVar("R")

def time_it(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} executed in {elapsed:.6f}s")
        return result
    return wrapper

@time_it
def compute_sum(n: int) -> int:
    return sum(i * i for i in range(n))

print(f"Result: {compute_sum(1000000)}")""",
                [
                    "ParamSpec captures precise positional and keyword argument types of wrapped callables.",
                    "Preserves full IDE autocompletion and mypy static type analysis across decorators.",
                    "Standardized in PEP 612 and fully integrated into standard typing module."
                ]
            ),
            # Day 2
            (
                "Structural Pattern Matching & Guard Clauses",
                "Intermediate",
                "Python 3.10+ match-case statements support pattern matching against data structures, class attributes, and sequence unpackings with inline conditional guards.",
                """from dataclasses import dataclass
from typing import Union

@dataclass
class Command:
    action: str
    amount: float

def process_event(event: Union[dict, Command, tuple]) -> str:
    match event:
        case {"type": "deposit", "amount": amt} if amt > 0:
            return f"Deposited ${amt:.2f}"
        case Command(action="withdraw", amount=amt) if amt <= 500:
            return f"Withdrew ${amt:.2f} within limit"
        case ("transfer", target, amt):
            return f"Transferred ${amt:.2f} to {target}"
        case _:
            return "Invalid or unauthorized transaction"

print(process_event({"type": "deposit", "amount": 250.0}))
print(process_event(Command(action="withdraw", amount=100.0)))""",
                [
                    "Pattern matching evaluates sequences, mappings, and class instances declaratively.",
                    "Guard clauses (`if condition`) filter matching branches dynamically.",
                    "The wildcard `_` acts as a mandatory fallback case for unhandled patterns."
                ]
            ),
            # Day 3
            (
                "Asynchronous Generators and `asyncfor` Mechanics",
                "Advanced",
                "Async generators combine python async/await event loops with generator yields, enabling high-throughput non-blocking data streaming.",
                """import asyncio
from typing import AsyncGenerator

async def fetch_stream_data(total_chunks: int) -> AsyncGenerator[dict, None]:
    for i in range(1, total_chunks + 1):
        await asyncio.sleep(0.01)  # Simulate non-blocking I/O
        yield {"chunk_id": i, "data": f"payload_{i*10}"}

async def main() -> None:
    print("Starting stream processing...")
    async for chunk in fetch_stream_data(5):
        print(f"Received: {chunk}")

asyncio.run(main())""",
                [
                    "Async generators yield values inside coroutines using `yield` and `await`.",
                    "Stream handling allows memory-efficient processing of massive payloads.",
                    "Iterate over async generators using `async for` inside asynchronous contexts."
                ]
            ),
            # Day 4
            (
                "Custom Context Managers & Exception Handling via `contextlib`",
                "Intermediate",
                "The `@contextmanager` decorator converts generator functions into fully compliant context managers with clean setup, execution, and cleanup semantics.",
                """from contextlib import contextmanager
import os
from typing import Generator

@contextmanager
def temporary_env(key: str, value: str) -> Generator[None, None, None]:
    original = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if original is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = original

with temporary_env("APP_STAGE", "staging"):
    print(f"Current stage inside context: {os.environ.get('APP_STAGE')}")

print(f"Stage after exit: {os.environ.get('APP_STAGE')}")""",
                [
                    "Guarantees execution of tear-down code even if exceptions occur.",
                    "Saves boilerplate compared to writing full `__enter__` and `__exit__` class methods.",
                    "Crucial for resource acquisition (files, sockets, database locks, env vars)."
                ]
            ),
            # Day 5
            (
                "Metaclasses & Dynamic Class Construction",
                "Expert",
                "Metaclasses act as the classes of classes in Python, allowing runtime inspection, attribute validation, and structural enforcement during module load time.",
                """class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, dsn: str):
        self.dsn = dsn

db1 = DatabaseConnection("postgresql://localhost:5432/main")
db2 = DatabaseConnection("postgresql://localhost:5432/main")

print(f"db1 is db2: {db1 is db2}")""",
                [
                    "Metaclasses intercept class creation by subclassing `type`.",
                    "Overriding `__call__` controls class instantiation mechanics.",
                    "Ideal for framework design, singleton management, and automatic registration."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            # Deterministic topic synthesis for all 365 days
            subtopics = [
                "Concurrency with asyncio.TaskGroup",
                "Memory Optimization with __slots__",
                "Descriptor Protocol and Property Implementation",
                "Weak References & Memory Leak Prevention",
                "Cython and C-Extension Binding Mechanics",
                "Subprocess Pipelines and Non-blocking I/O",
                "Functional Programming with functools.reduce and partial",
                "Custom Sequence Protocol & Slicing",
                "GIL Workarounds using Multiprocessing Pools",
                "AST Parsing & Dynamic Code Analysis"
            ]
            selected = subtopics[(day_idx - 1) % len(subtopics)]
            title = f"{selected} (Day {day_idx})"
            diff = "Advanced" if day_idx % 2 == 0 else "Intermediate"
            concept = f"In-depth exploration of {selected} in modern Python 3.12 development. Mastering this topic elevates code performance and architectural cleanliness."
            code = f"""# Python 3.12 Deep Dive - Day {day_idx}: {selected}
import sys
from typing import Any, List

def demonstrate_concept() -> dict[str, Any]:
    print(f"Executing Day {day_idx} Python module for: {selected}")
    data: List[int] = [i * 2 for i in range(10)]
    return {{"topic": "{selected}", "status": "completed", "sample_output": sum(data)}}

if __name__ == "__main__":
    result = demonstrate_concept()
    print("Execution Result:", result)"""
            takeaways = [
                f"Master {selected} to build production-grade Python architectures.",
                "Leverage Python 3.12 static type annotations for robust compile-time checks.",
                "Benchmark and profile runtime execution for optimized resource management."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )
