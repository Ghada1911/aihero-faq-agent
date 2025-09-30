---
id: ec6d89a462
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_ee3efac5.png
question: 'Access Denied: Table yellow_tripdata: User does not have permission to
  query table yellow_tripdata, or perhaps it does not exist in location US.'
sort_order: 58
---

<{IMAGE:image_1}>

### Error Details

```
Database Error in model stg_yellow_tripdata (models/staging/stg_yellow_tripdata.sql)

Access Denied: Table taxi-rides-ny-339813-412521:trips_data_all.yellow_tripdata: User does not have permission to query table taxi-rides-ny-339813-412521:trips_data_all.yellow_tripdata, or perhaps it does not exist in location US.

compiled Code at target/run/taxi_rides_ny/models/staging/stg_yellow_tripdata.sql
```

### Solution

1. **Branch Verification**:
   - Ensure you are working on the correct branch. If not, switch to the appropriate branch.
   
2. **Schema Configuration**:
   - Edit the `04-analytics-engineering/taxi_rides_ny/models/staging/schema.yml` file.
   - Ensure the configuration is correct:
     
     ```yaml
     sources:
     - name: staging
       database: your_database_name
     ```

3. **Custom Branch Setup in dbt Cloud**:
   - If the error persists, consider running the dbt job on a custom branch:
     
     - Navigate to the environment settings in dbt Cloud.
     - In General settings, select "Only run on a custom branch".
     - Enter the name of your custom branch (e.g., HW).
     - Click Save.
