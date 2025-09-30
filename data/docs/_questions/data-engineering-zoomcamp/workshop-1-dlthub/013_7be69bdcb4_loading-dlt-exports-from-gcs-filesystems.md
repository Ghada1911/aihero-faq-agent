---
id: 7be69bdcb4
question: Loading Dlt Exports from GCS Filesystems
sort_order: 13
---

When using the filesystem destination, you may have issues reading the files exported because DLT will by default compress the files. If you are using `loader_file_format="parquet"` then BigQuery should cope with this compression OK. If you want to use JSONL or CSV format, however, you may need to disable file compression to avoid issues with reading the files directly in BigQuery. To do this, set the following config:

```bash
[normalize.data_writer]
disable_compression = true
```

There is further information at [DLTHub Docs](https://dlthub.com/docs/dlt-ecosystem/destinations/filesystem#file-compression).

**Warning:**
```yaml
Test 'test.taxi_rides_ny.relationships_stg_yellow_tripdata_dropoff_locationid__locationid__ref_taxi_zone_lookup_csv_.085c4830e7' (models/staging/schema.yml) depends on a node named 'taxi_zone_lookup.csv' in package '' which was not found
```

**Solution:** This warning indicates that dbt is trying to reference a model or source named `taxi_zone_lookup.csv`, but it cannot find it. We might have a typo in our `ref()` function.

**Tests:**

- **Name:** relationships_stg_yellow_tripdata_dropoff_locationid
  
  **Description:** Ensure `dropoff_location_id` exists in `taxi_zone_lookup.csv`

  **Relationships:**
  - **To:** `ref('taxi_zone_lookup.csv')`  # ❌ Wrong reference

  - **Field:** `locationid`

  - **To:** `ref('taxi_zone_lookup')`  # ✅ Correct reference

**Pandas and Spark Version Mismatch:**

When running `df_spark = spark.createDataFrame(df_pandas)`, an error indicating a version mismatch between Pandas and Spark was encountered. To resolve this, either:

1. Downgrade Pandas to a version below 2.
2. Upgrade Spark to version 3.5.5.

I chose to upgrade Spark to 3.5.5, and it worked.

**Avoiding Backpressure in Flink:**

**What’s Backpressure?**

- It occurs when Flink processes data slower than Kafka produces it.
- This leads to increased memory usage and can slow down or crash the job.

**How to Fix It?**

- Adjust Kafka’s consumer parallelism to match the producer rate.
- Increase partitions in Kafka to allow more parallel processing.
- Monitor Flink metrics to detect backpressure.

```python
env.set_parallelism(4)  # Adjust parallelism to avoid bottlenecks
```