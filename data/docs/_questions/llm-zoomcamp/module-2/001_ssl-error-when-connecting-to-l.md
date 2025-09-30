---
id: '6494916130'
question: 'SSL Error when connecting to locally running ElasticSearch instance via
  SDK:'
sort_order: 1
---

The issue is likely that you’re trying to use HTTPS instead of HTTP when you call local.

To remove ES authentication constraints, set `xpack.security.enabled=false` in the ES docker settings.