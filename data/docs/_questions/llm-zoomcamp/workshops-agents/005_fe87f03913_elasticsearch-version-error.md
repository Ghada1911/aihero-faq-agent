---
id: fe87f03913
question: Elasticsearch version error
sort_order: 5
---


### Elasticsearch version error

**Error:**
```plaintext
elasticsearch.BadRequestError: BadRequestError(400, 'media_type_header_exception', 'Invalid media-type value on headers [Content-Type, Accept]', Accept version must be either version 8 or 7, but found 9. Accept=application/vnd.elasticsearch+json; compatible-with=9)
```

**Fix:**
1. Uninstall the current Elasticsearch package:
   ```bash
   pip uninstall elasticsearch
   ```
2. Install the correct version (8.10.0) of the Elasticsearch package:
   ```bash
   pip install elasticsearch==8.10.0
   ```