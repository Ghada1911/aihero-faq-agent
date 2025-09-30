---
id: 0cfd7f7ed6
question: pgAdmin - Blank/white screen after login (browser)
sort_order: 79
---

Using GitHub Codespaces in the browser resulted in a blank screen after logging into pgAdmin (running in a Docker container). The terminal of the pgAdmin container was showing the following error message:

```
CSRFError: 400 Bad Request: The referrer does not match the host.
```

### Solution #1:

As recommended in the following issue: [GitHub Issue #5432](https://github.com/pgadmin-org/pgadmin4/issues/5432), setting the following environment variable solved it:

```bash
docker run --rm -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -e PGADMIN_CONFIG_WTF_CSRF_ENABLED="False" \
  -p "8080:80" \
  --name pgadmin \
  --network=pg-network \
  dpage/pgadmin4:8.2
```

### Solution #2:

Using the locally installed VSCode to display GitHub Codespaces. When using GitHub Codespaces in the locally installed VSCode (opening a Codespace or creating/starting one), this issue did not occur.