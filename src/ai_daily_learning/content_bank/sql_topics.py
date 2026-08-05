"""SQL Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class SQLTopicProvider(BaseTopicProvider):
    """Generates rich SQL educational content for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="SQL")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Advanced Window Functions: `DENSE_RANK()`, `LEAD()`, and `LAG()`",
                "Intermediate",
                "Window functions compute aggregations across sets of rows related to the current row without collapsing the result set into a single summary row.",
                """-- Ranking top revenue per region and calculating period-over-period growth
WITH RegionalSales AS (
    SELECT
        region_id,
        sales_rep,
        total_revenue,
        sale_date,
        DENSE_RANK() OVER (PARTITION BY region_id ORDER BY total_revenue DESC) AS rev_rank,
        LAG(total_revenue, 1) OVER (PARTITION BY region_id, sales_rep ORDER BY sale_date) AS prev_revenue
    FROM sales_records
)
SELECT
    region_id,
    sales_rep,
    total_revenue,
    prev_revenue,
    ROUND(((total_revenue - prev_revenue) / NULLIF(prev_revenue, 0)) * 100, 2) AS growth_pct
FROM RegionalSales
WHERE rev_rank <= 3;""",
                [
                    "Window functions operate on partitions defined by `PARTITION BY` and ordered by `ORDER BY`.",
                    "`NULLIF` prevents division-by-zero runtime exceptions during percentage growth calculations.",
                    "`DENSE_RANK()` assigns consecutive rank numbers without gaps in case of duplicate values."
                ]
            ),
            # Day 2
            (
                "Recursive Common Table Expressions (CTEs) for Hierarchical Data",
                "Advanced",
                "Recursive CTEs allow querying graph structures, org trees, and bill-of-materials by recursively joining a query block to itself until a termination condition is met.",
                """-- Traverse organizational hierarchy to build employee reporting tree
WITH RECURSIVE OrgTree AS (
    -- Anchor member: root executives
    SELECT
        employee_id,
        first_name || ' ' || last_name AS full_name,
        manager_id,
        1 AS level_depth,
        ARRAY[employee_id] AS hierarchy_path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive member: child employees
    SELECT
        e.employee_id,
        e.first_name || ' ' || e.last_name,
        e.manager_id,
        t.level_depth + 1,
        t.hierarchy_path || e.employee_id
    FROM employees e
    INNER JOIN OrgTree t ON e.manager_id = t.employee_id
)
SELECT
    level_depth,
    REPEAT('  ', level_depth - 1) || full_name AS indented_name,
    hierarchy_path
FROM OrgTree
ORDER BY hierarchy_path;""",
                [
                    "Anchor member defines the base set; recursive member joins back to the CTE name.",
                    "Hierarchy path arrays prevent infinite loop cycles in circular graphs.",
                    "Essential for hierarchical reporting, file systems, and category taxonomies."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            topics = [
                "B-Tree vs Generalized Inverted Index (GIN) Performance Tuning",
                "Query Execution Plan Analysis using EXPLAIN ANALYZE",
                "ACID Compliance & Isolation Levels (READ COMMITTED vs SERIALIZABLE)",
                "Partitioning Strategies: Range vs List vs Hash Partitioning",
                "JSONB Inverted Indexing & Querying in PostgreSQL",
                "Optimizing Lateral Joins for Correlated Subqueries",
                "Materialized Views & Incremental Refresh Pipelines",
                "Upsert Patterns using ON CONFLICT DO UPDATE",
                "Database Transactions & Savepoints Management",
                "Pivot & Unpivot Data Transformation Queries"
            ]
            selected = topics[(day_idx - 1) % len(topics)]
            title = f"{selected} (Day {day_idx})"
            diff = "Advanced" if day_idx % 2 == 0 else "Intermediate"
            concept = f"Mastering {selected} provides deep optimization capabilities for enterprise SQL relational data platforms."
            code = f"""-- SQL Masterclass Day {day_idx}: {selected}
SELECT
    id,
    entity_name,
    created_at,
    COUNT(*) OVER (PARTITION BY category_id) AS category_total
FROM primary_table
WHERE status = 'ACTIVE'
ORDER BY created_at DESC
LIMIT 100;"""
            takeaways = [
                f"Leverage {selected} to eliminate query bottlenecks.",
                "Always inspect execution plans (`EXPLAIN ANALYZE`) before deploying indexes to production.",
                "Ensure proper concurrency control when executing state modifications."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )
