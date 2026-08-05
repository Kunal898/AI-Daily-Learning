# Contributing to AI-Daily-Learning

Thank you for your interest in contributing to **AI-Daily-Learning**! We welcome contributions from developers, educators, data engineers, security researchers, and learners worldwide.

## How Content Generation Works

Every day, the repository automatically generates content across 11 technical domains:
- Python
- SQL
- Cybersecurity
- Data Analysis
- Linux
- Git
- Networking
- Docker
- Machine Learning
- Daily Coding Challenges
- Interview Questions & Quizzes

All content generation logic resides inside `src/ai_daily_learning/content_bank/`.

## Local Development Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/AI-Daily-Learning.git
   cd AI-Daily-Learning
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

4. **Run Unit Tests**:
   ```bash
   pytest
   ```

5. **Generate Daily Lesson Locally**:
   ```bash
   python generate.py --date 2026-08-05
   ```

6. **Update README & Indexes**:
   ```bash
   python update_readme.py
   python build_index.py
   python stats.py
   ```

## Adding New Topics & Curricula

To add or improve topics in any domain:
1. Navigate to `src/ai_daily_learning/content_bank/`.
2. Locate the appropriate topic module (e.g. `python_topics.py`).
3. Ensure every topic returns structured markdown with real code, clear explanations, and hands-on examples.
4. Add unit test coverage in `tests/test_content_banks.py`.
