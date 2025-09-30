---
id: cbaecfefaf
question: Data Type Error when running fact table
sort_order: 51
---

If you encounter a data type error on the `trip_type` column, it may be due to some `nan` values that aren't null in BigQuery.

**Solution:** Try casting it to `FLOAT` datatype instead of `NUMERIC`. 

```sql
SELECT CAST(trip_type AS FLOAT) FROM your_table;
```