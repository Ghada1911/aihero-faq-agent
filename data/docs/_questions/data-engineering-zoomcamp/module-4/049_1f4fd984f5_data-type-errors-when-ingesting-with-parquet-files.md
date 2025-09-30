---
id: 1f4fd984f5
question: Data type errors when ingesting with parquet files
sort_order: 49
---

The easiest way to avoid these errors is by ingesting the relevant data in a `.csv.gz` file type. Then, do:

```sql
CREATE OR REPLACE EXTERNAL TABLE `dtc-de.trips_data_all.fhv_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://dtc_data_lake_dtc-de-updated/data/fhv_all/fhv_tripdata_2019-*.csv.gz']
);
```

This example should help you avoid data type issues for week 4.