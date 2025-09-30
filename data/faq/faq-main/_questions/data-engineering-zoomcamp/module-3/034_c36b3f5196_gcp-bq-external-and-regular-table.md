---
id: c36b3f5196
question: GCP BQ - External and regular table
sort_order: 34
---


**External Table**

- Data remains stored in a Google Cloud Storage (GCS) bucket.

**Regular Table**

- Data is copied into BigQuery storage.

**Example of creating an external table:**

```sql
CREATE OR REPLACE EXTERNAL TABLE `your_project.your_dataset.tablenamel`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://your-bucket-name/yellow_tripdata_2024-*.parquet']
);
```

**Example of creating a regular table from an external table:**

```sql
CREATE OR REPLACE TABLE `your_project.your_dataset.tablename`
AS
SELECT * FROM `your_project.your_dataset.yellow_taxi_external`;
```

**Directly loading data from GCS into a regular BigQuery table without creating an external table:**

```sql
CREATE OR REPLACE TABLE `your_project.your_dataset.yellow_taxi_table`
OPTIONS (
  format = 'PARQUET'
) AS
SELECT * FROM `your_project.your_dataset.external_table_placeholder`
FROM EXTERNAL_QUERY(
  'your_project.region-us.gcs_external',
  'SELECT * FROM `gs://your-bucket-name/yellow_tripdata_2024-*.parquet`'
);
```