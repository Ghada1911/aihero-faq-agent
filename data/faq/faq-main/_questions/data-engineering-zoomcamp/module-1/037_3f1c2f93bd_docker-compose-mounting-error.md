---
id: 3f1c2f93bd
question: 'Docker-Compose: mounting error'
sort_order: 37
---


```
error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted
```

If you have used the previous answer and created a local Docker volume, then you need to inform the compose file about the named volume:

```yaml
dtc_postgres_volume_local:  # Define the named volume here
```

- Services mentioned in the compose file automatically become part of the same network.

### Steps:

1. Use the command:
   ```bash
   docker volume inspect dtc_postgres_volume_local
   ```
   to see the location by checking the value of `Mountpoint`.

2. In some cases, after running `docker compose up`, the mounting directory created is named `docker_sql_dtc_postgres_volume_local` instead of the existing `dtc_postgres_volume_local`.

3. Rename the existing `dtc_postgres_volume_local` to `docker_sql_dtc_postgres_volume_local`:
   - Be careful when performing this operation.

4. Remove the newly created one.

5. Run `docker compose up` again and check if the table is there.