---
id: f4dcbdd4ee
question: Is it mandatory to use a reference dataset when generating a report with
  Evidently?
sort_order: 29
---

No. While Evidently is designed to compare a reference dataset with a current one, it can also be used without a reference dataset.

In such cases, you can pass `reference_data=None` when creating the report. This is useful for generating descriptive statistics or univariate analyses on a single dataset (e.g., using `ColumnSummaryMetric`, `DatasetMissingValuesMetric`, etc.).