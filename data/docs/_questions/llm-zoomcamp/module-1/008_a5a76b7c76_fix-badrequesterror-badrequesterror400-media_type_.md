---
id: a5a76b7c76
question: 'Fix BadRequestError: BadRequestError(400, ''media_type_header_exception'',
  ''Invalid media-type value on headers [Content-Type, Accept]'', Accept version must
  be either version 8 or 7, but found 9. Accept=application/vnd.elasticsearch+json;
  compatible-with=9)'
sort_order: 8
---

When trying to connect to the Elasticsearch server/node version 8.17.6 running within a Docker container with the Python client Elasticsearch version 9.x or more, you may encounter the following `BadRequestError`:

```plaintext
BadRequestError(400, 'media_type_header_exception', 'Invalid media-type value on headers [Content-Type, Accept]', Accept version must be either version 8 or 7, but found 9. Accept=application/vnd.elasticsearch+json; compatible-with=9)
```

This issue arises because `pip install elasticsearch` installs Elasticsearch 9.x Python client, which is incompatible with Elasticsearch 8.17.6. To resolve this issue, use the following command to install a compatible Elasticsearch client version:

```bash
pip install "elasticsearch>=8,<9"
```