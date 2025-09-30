---
id: 5f056e236c
question: Docker-Compose - Error undefined volume in Windows/WSL
sort_order: 51
---

If you wrote the `docker-compose.yaml` file exactly like the video, you might run into an error:

```
service "pgdatabase" refers to undefined volume dtc_postgres_volume_local: invalid compose project
```

To resolve this, include the volume definition in your `docker-compose.yaml` file by adding:

```yaml
dt_postgres_volume_local:
```

This should be added under the `volumes` section. Make sure your file looks similar to this:

```yaml
volumes:
  dtc_postgres_volume_local:
```