---
id: 66ae44829d
question: 'ElasticSearch: ERROR: BadRequestError: BadRequestError(400, ''media_type_header_exception'',
  ''Invalid media-type value on headers [Content-Type, Accept]'', Accept version must
  be either version 8 or 7, but found 9.'
sort_order: 7
---

**Reason:** ElasticSearch client and server are on different versions.

**Solution:**

- Upgrade ElasticSearch on Docker to version 9:

  ```bash
  docker run -it \
  --rm \
  --name elasticsearch \
  -p 9200:9200 \
  -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  elasticsearch:9.0.1
  ```

- If upgrading to version 9 doesn’t work, check the client version (Python module) using:
  
  ```bash
  pip show elasticsearch
  ```
  
- Then install that specific version of ElasticSearch on Docker. Check if it worked using:
  
  ```bash
  curl http://localhost:9200/
  ```
  
**Example output of `pip show elasticsearch`:**

```
Name: elasticsearch
Version: 9.0.2
Summary: Python client for Elasticsearch
Home-page: [GitHub](https://github.com/elastic/elasticsearch-py)
Author:
Author-email: Elastic Client Library Maintainers <client-libs@elastic.co>
License-Expression: Apache-2.0
Location: /home/codespace/.python/current/lib/python3.12/site-packages
Requires: elastic-transport, python-dateutil, typing-extensions
Required-by:
```