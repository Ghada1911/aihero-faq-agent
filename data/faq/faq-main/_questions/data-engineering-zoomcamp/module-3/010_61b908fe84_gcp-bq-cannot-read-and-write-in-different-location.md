---
id: 61b908fe84
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_924b3959.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_4d72f30c.png
question: 'GCP BQ - Cannot read and write in different locations: source: EU, destination:
  US - Loading data from GCS into BigQuery (different Region):'
sort_order: 10
---

Be careful when you create your resources on GCP; all of them must share the same region to load data from a GCS Bucket to BigQuery. If you forgot this step, you can create a new dataset in BigQuery using the same region as your GCS Bucket.

<{IMAGE:image_1}>

<{IMAGE:image_2}>

This error indicates that your GCS Bucket and the BigQuery dataset are placed in different regions. You need to create a new dataset in BigQuery in the same region as your GCS Bucket and store the data in this newly created dataset.