"""Template engine for formatting Markdown lessons."""

from typing import Any, Dict
from jinja2 import Environment, BaseLoader
from ai_daily_learning.models import DailyLesson

DEFAULT_LESSON_TEMPLATE = """# 📚 AI Daily Learning - Day {{ lesson.day_num }} ({{ lesson.date_str }})

> **Automated Educational Knowledge Base** | Day {{ lesson.day_num }} of 365

---

## 📅 Overview & Target Curriculum

Today's learning bundle spans **11 Technical Domains** designed for Software Engineers, DevOps Professionals, Data Scientists, and Security Engineers.

---

{% for domain_name, topic in lesson.topics.items() %}
## 🚀 Domain: {{ domain_name }}

### 📌 Topic: {{ topic.topic_name }}
- **Difficulty**: `{{ topic.difficulty }}`

#### 💡 Concept Breakdown
{{ topic.concept_summary }}

#### 💻 Practical Example & Code Snippet
```{% if domain_name == 'Python' %}python{% elif domain_name == 'SQL' %}sql{% elif domain_name == 'Linux' or domain_name == 'Git' or domain_name == 'Docker' %}bash{% else %}python{% endif %}
{{ topic.code_example }}
```

#### 🔑 Key Takeaways
{% for point in topic.key_takeaways %}
- {{ point }}
{% endfor %}

---
{% endfor %}

## 🧠 Daily Multiple-Choice Quiz

**Question:** {{ lesson.quiz.question }}

{% for opt in lesson.quiz.options %}
- {{ opt }}
{% endfor %}

<details>
<summary><b>🔍 Reveal Answer & Explanation</b></summary>

**Correct Answer:** `{{ lesson.quiz.correct_option }}`

**Explanation:**
{{ lesson.quiz.explanation }}
</details>

---

## ⚡ Daily Coding Challenge

### 🎯 Problem Statement: {{ lesson.challenge.title }}
**Difficulty:** `{{ lesson.challenge.difficulty }}`

{{ lesson.challenge.description }}

#### ✏️ Starter Code
```python
{{ lesson.challenge.starter_code }}
```

#### 🧪 Test Cases
```python
{% for test in lesson.challenge.test_cases %}
{{ test }}
{% endfor %}
```

<details>
<summary><b>💡 View Complete Solution</b></summary>

```python
{{ lesson.challenge.solution }}
```
</details>

---

*Generated automatically by AI-Daily-Learning Pipeline on {{ lesson.date_str }}.*
"""


class TemplateEngine:
    """Renders DailyLesson data models into clean, structured Markdown."""

    def __init__(self) -> None:
        self.env = Environment(loader=BaseLoader(), autoescape=False)
        self.template = self.env.from_string(DEFAULT_LESSON_TEMPLATE)

    def render_daily_lesson(self, lesson: DailyLesson) -> str:
        """Compiles a DailyLesson instance into a complete Markdown document."""
        return self.template.render(lesson=lesson)
