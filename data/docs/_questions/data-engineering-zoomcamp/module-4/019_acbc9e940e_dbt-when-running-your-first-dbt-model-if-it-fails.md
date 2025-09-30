---
id: acbc9e940e
question: 'DBT: When running your first dbt model, if it fails with an error:'
sort_order: 19
---

```
404 Not found: Dataset was not found in location US

404 Not found: Dataset eighth-zenith-372015:trip_data_all was not found in location us-west1
```

To resolve this issue, follow these steps:

1. **Verify Locations in BigQuery:**
   - Go to BigQuery and check the location of both:
     - The source dataset (e.g., `trips_data_all`).
     - The schema you’re writing to. The name should be in the format `dbt_<first initial><last name>` if you didn’t change the default settings.

2. **Check Region Consistency:**
   - Ensure both datasets are in the same region. Typically, your source data is in your region, while the write location could be multi-regional (e.g., US).
   - If there's a mismatch, delete the datasets and recreate them in the specified region with the correct naming format.

3. **Specify Single-Region Location:**
   - Instead of using a multi-regional location like `US`, specify the exact region (e.g., `US-east1`). Refer to [this Github comment](https://github.com/dbt-labs/dbt-bigquery/issues/19#issuecomment-635545315) for more details.
   - Additional guidance is available in [this post](https://learningdataengineering540969211.wordpress.com/dbt-cloud-and-bigquery-an-effort-to-try-and-resolve-location-issues/).

4. **Update Location in DBT Cloud:**
   - Go to your profile page (top right drop-down --> profile).
   - Under Credentials --> Analytics (or your customized name), click on BigQuery >.
   - Hit Edit and update your location. You may need to re-upload your service account JSON to refresh your private key. Ensure the region matches exactly as specified in BigQuery.

Following these steps should help resolve location-related errors when running your dbt models.