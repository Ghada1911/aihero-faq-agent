---
id: a17cb536b1
question: 'When executing dbt run after using fhv_tripdata as an external table: you
  get "Access Denied: BigQuery BigQuery: Permission denied"'
sort_order: 45
---

1. Go to your dbt cloud service account.

2. Add the `Storage Object Admin` and `Storage Admin` roles in addition to `BigQuery Admin`.