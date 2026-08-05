"""Docker Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class DockerTopicProvider(BaseTopicProvider):
    """Generates rich Docker educational content for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Docker")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Production Multi-Stage Dockerfile for Python 3.12 Apps",
                "Intermediate",
                "Multi-stage Docker builds separate build-time dependencies (compilers, headers) from runtime environments, drastically reducing container image size and attack surface.",
                """# Stage 1: Build environment
FROM python:3.12-slim AS builder

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final minimal runtime image
FROM python:3.12-slim AS runtime

# Create non-root system user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . /app

USER appuser
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \\
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "main.py"]""",
                [
                    "Multi-stage builds eliminate heavy build tools (`gcc`, `g++`) from final runtime images.",
                    "Running as non-root (`USER appuser`) prevents container breakout escalation.",
                    "Ordering Dockerfile commands from least to most frequently modified maximizes layer caching."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            topics = [
                "Docker Compose v2 Environment Files & Secret Injection",
                "Container Rootless Execution Mode & User Namespaces",
                "Optimizing Layer Cache using BuildKit Cache Mounts (`--mount=type=cache`)",
                "Container Storage Drivers (Overlay2) & Volume Performance Tuning",
                "Docker Overlay Networks & Macvlan Networking Deep Dive",
                "Securing Containers with Seccomp Profiles and AppArmor",
                "Dockerfile Best Practices: Distroless Base Images",
                "Container Resource Quotas (CPU Shares & Memory OOM Kill Control)",
                "Building Multi-Platform Images with Docker Buildx & QEMU",
                "Docker Init Systems (`tini`) & Zombie Process Harvesting"
            ]
            selected = topics[(day_idx - 1) % len(topics)]
            title = f"{selected} (Day {day_idx})"
            diff = "Intermediate"
            concept = f"Containerization mastery guide for {selected}. Architecting resilient container microservices."
            code = f"""# Dockerfile / Compose Snippet Day {day_idx}: {selected}
version: '3.8'

services:
  app:
    build:
      context: .
      target: runtime
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - APP_ENV=production
    security_opt:
      - no-new-privileges:true"""
            takeaways = [
                f"Master containerization techniques for {selected}.",
                "Always scan container images (`docker scout` or `trivy`) prior to registry push.",
                "Set explicit container CPU and memory resource requests/limits."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )
