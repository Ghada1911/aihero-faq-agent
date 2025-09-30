---
id: e596dc3cbe
question: 'DBT: When executing dbt run after installing dbt-utils latest version i.e.,
  1.0.0 warning has generated'
sort_order: 20
---

**Error**: `dbt_utils.surrogate_key` has been replaced by `dbt_utils.generate_surrogate_key`

**Fix**:

- Replace `dbt_utils.surrogate_key` with `dbt_utils.generate_surrogate_key` in `stg_green_tripdata.sql`.