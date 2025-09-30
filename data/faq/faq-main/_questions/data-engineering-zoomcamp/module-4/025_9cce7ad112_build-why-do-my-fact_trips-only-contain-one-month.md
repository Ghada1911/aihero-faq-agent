---
id: 9cce7ad112
question: 'Build: Why do my fact_trips only contain one month of data?'
sort_order: 25
---

Check if you specified the `if_exists` argument correctly when writing data from GCS to BigQuery. 

When I wrote my automated flow for each month of the years 2019 and 2020 for green and yellow data, I had specified `if_exists="replace"` while experimenting with the flow setup. Once you want to run the flow for all months in 2019 and 2020, make sure to set `if_exists="append"`.

- `if_exists="replace"` will replace the whole table with only the month data that you are writing into BigQuery in that one iteration -> you end up with only one month in BigQuery (the last one you inserted).

- `if_exists="append"` will append the new monthly data -> you end up with data from all months.