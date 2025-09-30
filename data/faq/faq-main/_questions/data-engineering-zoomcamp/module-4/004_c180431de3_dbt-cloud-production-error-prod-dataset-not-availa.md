---
id: c180431de3
question: 'DBT Cloud production error: prod dataset not available in location EU'
sort_order: 4
---

**Problem:**

I am trying to deploy my DBT models to production using DBT Cloud. The data should reside in BigQuery with the dataset location as EU. However, when running the model in production, a prod dataset is incorrectly created in BigQuery with a location of US. This leads to the build failing with the error:

```
ERROR 404: project.dataset:prod not available in location EU
```

I have attempted various fixes, but I'm unsure if there is a simpler solution than creating my projects or buckets in the US location.

Note: Everything functions properly in development mode; the issue arises only during job scheduling and execution in production.

**Solution:**

1. Manually create the `prod` dataset in BigQuery with the EU location specified.
2. Rerun the production job.