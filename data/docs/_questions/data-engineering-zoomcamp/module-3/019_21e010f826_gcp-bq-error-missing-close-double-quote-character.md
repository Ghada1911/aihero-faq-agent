---
id: 21e010f826
question: 'GCP BQ - Error: Missing close double quote (") character'
sort_order: 19
---

To avoid this error, you can upload data from Google Cloud Storage to BigQuery through BigQuery Cloud Shell using the command:

```bash
bq load --autodetect --allow_quoted_newlines --source_format=CSV dataset_name.table_name "gs://dtc-data-lake-bucketname/fhv/fhv_tripdata_2019-*.csv.gz"
```