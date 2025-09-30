---
id: c8d29f6862
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_1d6e2776.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_0bec8845.png
question: 'GCP BQ - Cannot read and write in different locations: source: <REGION_HERE>,
  destination: <ANOTHER_REGION_HERE>'
sort_order: 11
---

Make sure to create the BigQuery dataset in the same location as your GCS Bucket. For instance, if your GCS Bucket was created in `us-central1`, then the BigQuery dataset must also be created in `us-central1`.

<{IMAGE:image_1}>

<{IMAGE:image_2}>