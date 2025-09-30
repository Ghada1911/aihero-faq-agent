---
id: 3d24f7796d
question: 'GitHub Codespaces: Running pgadmin in Docker'
sort_order: 9
---

With the default instructions, running pgadmin in Docker may result in a blank screen after logging into the pgadmin console. To resolve this, add the following two environment variables to your pgadmin configuration to allow it to work with Codespaces’ reverse proxy:

```plaintext
PGADMIN_CONFIG_PROXY_X_HOST_COUNT: 1
PGADMIN_CONFIG_PROXY_X_PREFIX_COUNT: 1
```