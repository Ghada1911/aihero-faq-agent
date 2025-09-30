---
id: 18001c743b
question: Can BigQuery work with parquet files directly?
sort_order: 35
---

Yes, you can load your Parquet files directly into your GCP (Google Cloud Platform) Bucket first. Then, via BigQuery, you can create an external table of these Parquet files with a query statement like this:

```sql
CREATE OR REPLACE EXTERNAL TABLE `module-3-data-warehouse.taxi_data.external_yellow_tripdata_2024`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://module3-dez/yellow_tripdata_2024-*.parquet']
);
```

Make sure to adjust the SQL statement to your own situation and directories. The `*` symbol can be used as a wildcard to target Parquet files from all the months of 2024.