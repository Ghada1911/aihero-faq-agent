---
id: 5b7577406d
question: 'BigQuery returns an error when I try to run ‘dbt run’:'
sort_order: 62
---

My taxi data was loaded into GCS with `etl_web_to_gcs.py`, which converts CSV data into Parquet. Then I placed raw data trips into external tables, and when I executed `dbt run`, I got an error message:

```plaintext
Parquet column 'passenger_count' has type INT64 which does not match the target cpp_type DOUBLE.
```

This is because several columns in the files have different data formats.

To resolve this error, I added the transformation:

```python
df[col] = df[col].astype('Int64')
```

Apply this transformation to the following columns:

- `passenger_count`
- `payment_type`
- `RatecodeID`
- `VendorID`
- `trip_type`

After making these changes, the process completed successfully.