---
id: 16b4ae94ef
question: GCP BQ - Native tables vs External tables in BigQuery?
sort_order: 28
---

Native tables are tables where the data is stored directly in BigQuery. In contrast, external tables store the data outside BigQuery, with BigQuery storing metadata about that external table.

- **External tables:** These tables are not stored directly in BigQuery but are pulled in from a data lake such as Google Cloud Storage or AWS S3.
- **Materialized table:** This is a copy of an external table with data stored in BigQuery, consuming storage space.

Resources:

- [External Tables Documentation](https://cloud.google.com/bigquery/docs/external-tables)
- [BigQuery Tables Introduction](https://cloud.google.com/bigquery/docs/tables-intro)