---
id: 49b5277d77
question: 'GCP BQ: DATE() Error in BigQuery'
sort_order: 26
---

**Error Message:**

```
PARTITION BY expression must be DATE(<timestamp_column>), DATE(<datetime_column>), DATETIME_TRUNC(<datetime_column>, DAY/HOUR/MONTH/YEAR), a DATE column, TIMESTAMP_TRUNC(<timestamp_column>, DAY/HOUR/MONTH/YEAR), DATE_TRUNC(<date_column>, MONTH/YEAR), or RANGE_BUCKET(<int64_column>, GENERATE_ARRAY(<int64_value>, <int64_value>[, <int64_value>]))
```

**Solution:**

Convert the column to datetime first:

```python
# Convert pickup_datetime to datetime
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

# Convert dropOff_datetime to datetime
df["dropOff_datetime"] = pd.to_datetime(df["dropOff_datetime"])
```