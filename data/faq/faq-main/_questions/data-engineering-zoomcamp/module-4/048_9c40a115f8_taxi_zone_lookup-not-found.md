---
id: 9c40a115f8
question: ‘taxi_zone_lookup’ not found
sort_order: 48
---

Check the `.gitignore` file and make sure you don’t have `*.csv` in it.

If you're encountering a dbt error with the following message:

```
Runtime Error in rpc request (from remote system.sql)
404 Not found: Table dtc-de-0315:trips_data_all.green_tripdata_partitioned was not found in location europe-west6
Location: europe-west6
Job ID: 168ee9bd-07cd-4ca4-9ee0-4f6b0f33897c
```

- Verify that all your datasets are configured with the correct region. For example, use `europe-west6` instead of a general region like `EU`.
- To update the region in dbt settings:
  - Go to `dbt -> projects -> optional settings` 
  - Manually set the location to match the required region.