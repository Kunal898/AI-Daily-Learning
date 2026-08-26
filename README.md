# 🚀 AI-Daily-Learning

> An automated daily educational knowledge base generating real, production-ready educational content across 11 technical domains every single day using Python 3.12, Clean Architecture, and GitHub Actions.

<!-- STATS:START -->
### 📊 Live Learning Statistics

![Total Lessons](https://img.shields.io/badge/Total_Lessons-22-blue?style=for-the-badge&logo=book)
![Progress](https://img.shields.io/badge/Progress-6.03%25-brightgreen?style=for-the-badge&logo=github)
![Total Words](https://img.shields.io/badge/Words_Generated-34721-purple?style=for-the-badge)

**Curriculum Progress:** `[█░░░░░░░░░░░░░░░░░░░] 6.03%` (Target: 365 Days)

| Metric | Value |
| --- | --- |
| 📚 **Total Lessons** | `22` / 365 |
| 📅 **Latest Lesson** | [2026-08-26](output/2026-08-26.md) |
| 📝 **Total Words Written** | `34,721` words |
| 🎯 **Progress Percentage** | `6.03%` |
| 🌐 **Domains Covered** | `11 Core Tech Domains` |

#### 📂 Domain Module Breakdown
| Technical Domain | Lessons Generated | Status |
| --- | --- | --- |
| Python | `22` lessons | 🟢 Active |
| SQL | `22` lessons | 🟢 Active |
| Cybersecurity | `22` lessons | 🟢 Active |
| Data Analysis | `22` lessons | 🟢 Active |
| Linux | `22` lessons | 🟢 Active |
| Git | `22` lessons | 🟢 Active |
| Networking | `22` lessons | 🟢 Active |
| Docker | `22` lessons | 🟢 Active |
| Machine Learning | `22` lessons | 🟢 Active |
| Coding Challenge | `22` lessons | 🟢 Active |
| Interview Questions | `22` lessons | 🟢 Active |
| Quiz | `22` lessons | 🟢 Active |
<!-- STATS:END -->

## 🎯 Repository Overview

This repository automatically generates comprehensive daily markdown lessons covering:
1. 🐍 **Python 3.12** (Advanced typing, Asyncio, Patterns, GIL, Metaclasses)
2. 🗄️ **SQL** (Window functions, Recursive CTEs, Execution Plans, Indexing)
3. 🔒 **Cybersecurity** (OWASP Top 10, JWT Security, Cryptography, Hardening)
4. 📊 **Data Analysis** (Polars, Pandas, Vectorized NumPy, Time-Series)
5. 🐧 **Linux** (Sysadmin commands, awk/sed masterclass, Systemd, Profiling)
6. 🔀 **Git** (Worktrees, Interactive Rebase, Reflog recovery, Submodules)
7. 🌐 **Networking** (TLS 1.3, TCP/IP, DNS, HTTP/3, Socket programming)
8. 🐳 **Docker** (Multi-stage builds, Security, Compose, Image layer optimization)
9. 🤖 **Machine Learning** (Attention mechanism, Transformers, Quantization, PyTorch)
10. ⚡ **Coding Challenges** (Algorithms with test cases & clean solutions)
11. 🧠 **Interview Questions & Quizzes** (STAR method responses & MCQs with answer keys)

## 📁 Repository Structure

- `output/`: Daily generated markdown files (`YYYY-MM-DD.md`).
- `src/ai_daily_learning/`: Python package implementing OOP generators & indexers.
- `generate.py`: Main CLI tool to trigger daily content generation.
- `update_readme.py`: CLI tool to sync statistics and dynamic badges.
- `build_index.py`: CLI tool to compile `INDEX.md` and `search_index.json`.
- `stats.py`: CLI tool to display analytics.
- `quiz_generator.py` & `challenge_generator.py`: Standalone CLI practice tools.

## 🛠️ Local Usage

```bash
# Install dependencies
pip install -e .

# Generate today's daily lesson
python generate.py

# Update README and search index
python update_readme.py
python build_index.py
```

## ⚙️ Automated GitHub Actions Workflow

This repository runs automatically every day at `00:00 UTC` via GitHub Actions (`.github/workflows/daily_generate.yml`). It generates the daily content, updates the master `INDEX.md` and `README.md`, and commits the changes back to the repository.

---
*License: MIT | Maintained by AI-Daily-Learning Team*
