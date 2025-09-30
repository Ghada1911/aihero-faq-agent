---
id: 0fbc18e0f2
question: 'DBT: Error on building fact_trips.sql - Parquet column ''ehail_fee'' has
  type DOUBLE which does not match the target cpp_type INT64.'
sort_order: 56
---

To resolve the error regarding the 'ehail_fee' column type mismatch, you can use the following line in `stg_green_trips.sql` to replace the original `ehail_fee` line:

```sql
{{ dbt.safe_cast('ehail_fee', api.Column.translate_type("numeric")) }} as ehail_fee,
```

This ensures that the column type is correctly converted to match the expected type.