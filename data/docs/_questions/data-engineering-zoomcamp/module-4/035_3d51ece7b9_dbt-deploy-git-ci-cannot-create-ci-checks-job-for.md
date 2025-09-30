---
id: 3d51ece7b9
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_c35c101c.png
question: 'Dbt deploy + Git CI: cannot create CI checks job for deployment to Production'
sort_order: 35
---

**Error:**

```
Triggered by pull requests

This feature is only available for dbt repositories connected through dbt Cloud's native integration with Github, Gitlab, or Azure DevOps
```

**Solution:**

Contrary to the [guide on DTC repo](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md), don’t use the Git Clone option. Use the Github one instead. A step-by-step guide to unlink Git Clone and relink with Github is available in the next entry.

<{IMAGE:image_1}>
