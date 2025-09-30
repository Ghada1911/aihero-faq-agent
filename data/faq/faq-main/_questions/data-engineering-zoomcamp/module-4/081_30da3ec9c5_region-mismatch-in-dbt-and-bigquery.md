---
id: 30da3ec9c5
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_6e795821.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_522c20d6.png
question: Region Mismatch in DBT and BigQuery
sort_order: 81
---

If you are using the datasets copied into BigQuery from BigQuery public datasets, the region will be set as `US` by default. It is much easier to set your dbt profile location as `US` while transforming the tables and views. You can change the location as follows:

<{IMAGE:image_1}>

<{IMAGE:image_2}>