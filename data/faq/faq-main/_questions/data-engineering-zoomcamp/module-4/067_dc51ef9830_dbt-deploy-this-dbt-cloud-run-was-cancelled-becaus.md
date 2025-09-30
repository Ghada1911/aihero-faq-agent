---
id: dc51ef9830
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_c27ecb8e.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_8b6478c1.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_80992235.png
- description: 'image #4'
  id: image_4
  path: images/data-engineering-zoomcamp/image_cd924928.png
question: 'DBT Deploy: This dbt Cloud run was cancelled because a valid dbt project
  was not found.'
sort_order: 67
---

This issue occurs when the dbt project is moved to another directory in the repository or if you're on a different branch than expected.

**Solution:**

1. Navigate to the projects window on dbt Cloud.
2. Go to Settings -> Edit.
3. Add the directory path where the dbt project is located. Ensure that this path matches your file explorer path. For example:
   
   ```
   /week5/taxi_rides_ny
   ```

4. Check that there are no files waiting to be committed to GitHub if you’re running the job to deploy to PROD.

<{IMAGE:image_1}>

<{IMAGE:image_2}>

5. Ensure the PROD environment is set up to check the main branch, or the specified branch.

In the image below, the branch "ella2024" is set to be checked as "production-ready" by the "freshness" check mark in PROD environment settings. Each time a branch is merged into "ella2024" and a PR is triggered, the CI check job initiates. Note that merging and closing the PR must be done manually.

<{IMAGE:image_3}>

6. Set up the PROD custom branch (if not the default main) in the Environment setup screen.

<{IMAGE:image_4}>
