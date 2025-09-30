---
id: 9abc27b002
question: 'Kestra: Don’t forget to set GCP_CREDS variable'
sort_order: 17
---

If you plan on using Kestra with Google Cloud Platform, make sure you set up the `GCP_CREDS` that will be used in flows with "gcp" in their name.

To set it:

1. Go to **Namespaces** and select "zoomcamp" if you are using the examples from the lessons.
2. In the **KV Store** tab, create a new key as `GCP_CREDS`.
3. Set the type to JSON and paste the content of the `.json` file with credentials for the service account created.