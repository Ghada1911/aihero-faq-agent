---
id: 04f55d5846
question: 'BigQuery adapter: 404 Not found: Dataset was not found in location europe-west6'
sort_order: 32
---

1. Go to **Account settings** > **Project** > **Analytics**.
2. Click on your connection.
3. Scroll down to **Location** and type in the GCP location exactly as displayed in GCP (e.g., `europe-west6`). You might need to reupload your GCP key.

4. Delete your dataset in Google BigQuery (GBQ).
5. Rebuild the project using the command:
   
   ```bash
   dbt build
   ```

6. The newly built dataset should be in the correct location.