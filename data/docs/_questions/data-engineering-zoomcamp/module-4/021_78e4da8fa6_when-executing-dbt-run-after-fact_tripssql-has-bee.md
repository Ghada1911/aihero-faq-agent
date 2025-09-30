---
id: 78e4da8fa6
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_a3c7073f.png
question: 'When executing dbt run after fact_trips.sql has been created, the task
  failed with error: "Access Denied: BigQuery BigQuery: Permission denied while globbing
  file pattern."'
sort_order: 21
---

1. Fixed by adding the Storage Object Viewer role to the service account in use in BigQuery.

2. Add the related roles to the service account in use in GCS.

<{IMAGE:image_1}>
