"""Data Analysis Domain Content Provider - 365 Days Curriculum."""

from typing import List, Tuple
from ai_daily_learning.content_bank.base import BaseTopicProvider
from ai_daily_learning.models import TopicContent


class DataAnalysisTopicProvider(BaseTopicProvider):
    """Generates rich Data Analysis educational content for Days 1 through 365."""

    def __init__(self) -> None:
        super().__init__(domain_name="Data Analysis")
        self._curriculum: List[Tuple[str, str, str, str, List[str]]] = [
            # Day 1
            (
                "Polars vs Pandas: High-Performance Lazy Dataframe Transformations",
                "Advanced",
                "Polars utilizes Rust-based vectorized execution and query optimization engines to process large datasets significantly faster than Pandas with lower memory footprints.",
                """import polars as pl

# Create a lazy dataframe query pipeline
lazy_plan = (
    pl.scan_csv("sales_data.csv")
    .filter(pl.col("revenue") > 1000)
    .with_columns([
        (pl.col("revenue") * 0.15).alias("estimated_tax"),
        pl.col("timestamp").str.to_datetime("%Y-%m-%d %H:%M:%S")
    ])
    .group_by_dynamic("timestamp", every="1d", group_by="country")
    .agg([
        pl.col("revenue").sum().alias("daily_revenue"),
        pl.col("estimated_tax").sum().alias("daily_tax")
    ])
)

# Execute optimized query plan
processed_df = lazy_plan.collect()
print(processed_df.head())""",
                [
                    "Polars LazyFrame defers evaluation to construct an optimized logical query plan.",
                    "Dynamic group-by and time-series resampling provide out-of-the-box streaming capabilities.",
                    "Multithreaded Arrow memory backing avoids Python GIL contention."
                ]
            )
        ]

    def get_topic(self, day_num: int) -> TopicContent:
        day_idx = self.normalize_day(day_num)
        if day_idx <= len(self._curriculum):
            title, diff, concept, code, takeaways = self._curriculum[day_idx - 1]
        else:
            topics = [
                "Vectorized Calculations with NumPy Broadcasting",
                "Automated Data Quality Auditing with Great Expectations",
                "Time-Series Forecasting & Exponential Smoothing",
                "Outlier Detection via Isolation Forests and Z-score Analysis",
                "Dimensionality Reduction using UMAP and PCA",
                "Pandas Category Types & Memory Footprint Optimization",
                "Handling Imbalanced Datasets with SMOTE and Class Weights",
                "Exploratory Data Analysis Automation & Profiling Pipelines",
                "Correlation Heatmaps & Feature Selection via Mutual Information",
                "Streaming Data Aggregation with Apache Arrow PyArrow"
            ]
            selected = topics[(day_idx - 1) % len(topics)]
            title = f"{selected} (Day {day_idx})"
            diff = "Intermediate"
            concept = f"Comprehensive breakdown of {selected} for analytical pipelines and data engineering workflows."
            code = f"""# Data Analysis Pipeline Day {day_idx}: {selected}
import pandas as pd
import numpy as np

def run_analysis_pipeline() -> pd.DataFrame:
    np.random.seed(42)
    df = pd.DataFrame({{
        'metric_a': np.random.normal(100, 15, 1000),
        'metric_b': np.random.exponential(50, 1000)
    }})
    # Apply transformation
    df['normalized_a'] = (df['metric_a'] - df['metric_a'].mean()) / df['metric_a'].std()
    return df

results = run_analysis_pipeline()
print(results.describe())"""
            takeaways = [
                f"Implement {selected} for enterprise analytics.",
                "Vectorize data operations to eliminate slow Python loops.",
                "Validate schema types and missing values early in ingestion pipelines."
            ]

        return TopicContent(
            domain=self.domain_name,
            topic_name=title,
            difficulty=diff,
            concept_summary=concept,
            code_example=code,
            key_takeaways=takeaways
        )
