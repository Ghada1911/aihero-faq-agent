---
id: b209edb213
question: 'DBT: Error: “404 Not found: Dataset <dataset_name>:<dbt_schema_name> was
  not found in location EU” after building from stg_green_tripdata.sql'
sort_order: 70
---

In the step in [this video](https://www.youtube.com/watch?v=ueVy2N54lyc&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=44) (DE Zoomcamp 4.3.1 - Build the First dbt Models), after creating `stg_green_tripdata.sql` and clicking `build`, I encountered an error saying the dataset was not found in location EU. The default location for dbt Bigquery is the US, so when generating the new Bigquery schema for dbt, unless specified, the schema locates in the US.

Solution:

- Ensure the location is set to `EU` when adding connection details:
  - Navigate to **Develop** -> **Configure Cloud CLI** -> **Projects** -> **taxi_rides_ny** -> (connection) **Bigquery** -> **Edit**
  - Under **Location (Optional)**, type `EU`
  - Save the changes.