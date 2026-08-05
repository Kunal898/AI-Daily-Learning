"""Builds searchable indexes, table of contents, and JSON catalogs."""

import json
import re
from pathlib import Path
from typing import Dict, List, Any
from ai_daily_learning.config import OUTPUT_DIR, INDEX_FILE, TAGS_FILE, SEARCH_INDEX_FILE
from ai_daily_learning.utils import setup_logger

logger = setup_logger("index_builder")


class IndexBuilder:
    """Parses output directory and builds searchable index files."""

    def __init__(
        self,
        output_dir: Path = OUTPUT_DIR,
        index_file: Path = INDEX_FILE,
        tags_file: Path = TAGS_FILE,
        search_index_file: Path = SEARCH_INDEX_FILE
    ) -> None:
        self.output_dir = output_dir
        self.index_file = index_file
        self.tags_file = tags_file
        self.search_index_file = search_index_file

    def build_all(self) -> Dict[str, Any]:
        """Scans output files and updates INDEX.md, TAGS.md, and search_index.json."""
        logger.info("Scanning output files to build searchable indexes...")
        lesson_files = sorted(self.output_dir.glob("*.md"))

        catalog: List[Dict[str, Any]] = []

        for filepath in lesson_files:
            date_str = filepath.stem
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            day_match = re.search(r"# 📚 AI Daily Learning - Day (\d+)", content)
            day_num = int(day_match.group(1)) if day_match else 0

            # Extract topic titles for each domain
            domain_topics = {}
            for match in re.finditer(r"## 🚀 Domain: (.*?)\n\n### 📌 Topic: (.*?)\n", content):
                domain = match.group(1).strip()
                topic_title = match.group(2).strip()
                domain_topics[domain] = topic_title

            catalog.append({
                "date": date_str,
                "day_num": day_num,
                "file_path": f"output/{filepath.name}",
                "topics": domain_topics
            })

        # Sort catalog by date ascending
        catalog.sort(key=lambda x: x["date"])

        self._write_index_md(catalog)
        self._write_tags_md(catalog)
        self._write_search_json(catalog)

        logger.info(f"Index generation complete across {len(catalog)} lessons.")
        return {"total_indexed": len(catalog)}

    def _write_index_md(self, catalog: List[Dict[str, Any]]) -> None:
        lines = [
            "# 📖 AI-Daily-Learning Master Table of Contents",
            "",
            "This index lists all automatically generated daily lessons in chronological order.",
            "",
            "| Date | Day # | File Link | Key Topics Covered |",
            "| --- | --- | --- | --- |"
        ]

        for item in catalog:
            topics_summary = ", ".join(list(item["topics"].values())[:3])
            if len(item["topics"]) > 3:
                topics_summary += f" (+{len(item['topics']) - 3} more)"

            lines.append(
                f"| `{item['date']}` | **Day {item['day_num']}** | [{item['date']}.md]({item['file_path']}) | {topics_summary} |"
            )

        with open(self.index_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

    def _write_tags_md(self, catalog: List[Dict[str, Any]]) -> None:
        domain_map: Dict[str, List[Dict[str, str]]] = {}

        for item in catalog:
            for domain, topic in item["topics"].items():
                if domain not in domain_map:
                    domain_map[domain] = []
                domain_map[domain].append({
                    "date": item["date"],
                    "day_num": str(item["day_num"]),
                    "file_path": item["file_path"],
                    "topic": topic
                })

        lines = [
            "# 🏷️ Topic & Domain Index",
            "",
            "Browse daily lessons filtered by technical domain.",
            ""
        ]

        for domain, entries in sorted(domain_map.items()):
            lines.append(f"## {domain}")
            for entry in entries:
                lines.append(f"- **Day {entry['day_num']}** (`{entry['date']}`): [{entry['topic']}]({entry['file_path']})")
            lines.append("")

        with open(self.tags_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

    def _write_search_json(self, catalog: List[Dict[str, Any]]) -> None:
        with open(self.search_index_file, "w", encoding="utf-8") as f:
            json.dump(catalog, f, indent=2)
