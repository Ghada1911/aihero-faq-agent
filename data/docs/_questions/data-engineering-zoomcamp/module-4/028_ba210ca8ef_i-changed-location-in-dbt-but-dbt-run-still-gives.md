---
id: ba210ca8ef
question: I changed location in dbt, but dbt run still gives me an error
sort_order: 28
---

- Remove the dataset from BigQuery that was created by dbt.
- Run `dbt run` again so that it will recreate the dataset in BigQuery with the correct location.