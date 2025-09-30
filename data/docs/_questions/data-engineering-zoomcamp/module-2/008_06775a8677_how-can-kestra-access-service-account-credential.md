---
id: 06775a8677
question: How can Kestra access service account credential?
sort_order: 8
---

Do not directly add the content of service account credential JSON in Kestra script, especially if you are pushing to GitHub. Follow the instruction to add the service account as a secret [Configure Google Service Account](https://kestra.io/docs/how-to-guides/google-credentials#add-service-account-as-a-secret).

When you need to use it in Kestra, you can pull it through `{{ secret('GCP_SERVICE_ACCOUNT') }}` in the `pluginDefaults`.