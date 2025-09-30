---
id: 5dd0cdae58
question: 'DBT Deploy + CI: Location Problems on BigQuery'
sort_order: 68
---

When creating a pull request and running the CI, dbt creates a new schema on BigQuery. By default, this new schema is created with the 'US' location. If your datasets, schemas, and tables are in the 'EU', this will cause an error and the pull request will not be accepted. 

To change the location to 'EU' in the connection to BigQuery from dbt, follow these steps:

- Navigate to **Dbt -> Project -> Settings -> Connection BigQuery**
- Open **Optional Settings**
- Set **Location** to `EU`