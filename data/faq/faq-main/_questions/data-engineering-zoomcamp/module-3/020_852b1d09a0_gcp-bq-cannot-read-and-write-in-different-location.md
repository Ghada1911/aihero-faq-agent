---
id: 852b1d09a0
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_199a39eb.jpg
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_e2a4f6bc.jpg
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_9f3cd4ef.jpg
question: 'GCP BQ - Cannot read and write in different locations: source: asia-south2,
  destination: US'
sort_order: 20
---

Solution: This problem arises if your GCS and BigQuery storage are in different regions.

One potential way to solve it:

- Go to your Google Cloud bucket and check the region in the field named "Location."

  <{IMAGE:image_1}>

- In BigQuery, click on the three-dot icon near your project name and select "Create dataset."

  <{IMAGE:image_2}>

- In the region field, choose the same region as your Google Cloud bucket.

  <{IMAGE:image_3}>
