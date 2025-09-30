---
id: 6783a9bddb
question: 'Homework: Ingesting FHV_20?? data'
sort_order: 71
---

### Issue

If you’re having problems loading the FHV_20?? data from the GitHub repo into GCS and then into BigQuery (input file not of type parquet), follow these steps:

1. **Append URL Template**
   
   Add `?raw=true` to the `URL_TEMPLATE` link:
   
   ```python
   URL_TEMPLATE = URL_PREFIX + "/fhv_tripdata_{{ execution_date.strftime('%Y-%m') }}.parquet?raw=true"
   ```
   
2. **Update URL Prefix**
   
   Ensure `URL_PREFIX` is set to the following value:
   
   ```
   URL_PREFIX = "https://github.com/alexeygrigorev/datasets/blob/master/nyc-tlc/fhv"
   ```
   
   It is critical to use this link with the keyword `blob`. If the link contains `tree`, replace it with `blob`. Everything else, including the `curl -sSLf` command, can remain unchanged.