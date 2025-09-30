---
id: e4bce3ff6b
question: Error when running Kestra flow connecting to postgres
sort_order: 5
---

### Error Message
```plaintext
org.postgresql.util.psqlexception the connection attempt failed due to this config on kestra flow -> jdbc:postgresql://host.docker.internal:5432/postgres-zoomcamp
```

### Solution
- Replace `host.docker.internal` with the name of the service for Postgres in your Docker Compose file.

---

### Additional Error Message
```plaintext
org.postgresql.util.PSQLException: The connection attempt failed. 2025-01-29 22:52:22.281 green_create_table The connection attempt failed. host.docker.internal
```

### Analysis and Solution
- If using Linux, the PostgreSQL database URL differs from the tutorial. Instead of `host.docker.internal`, Linux users should use the service or container name for Postgres. For example, use:
  
  ```plaintext
  jdbc:postgresql://postgres:5432/kestra
  ```
- Double-check the database name in your Docker Compose file. It might be different from the tutorial; for example, `kestra` instead of `postgres-zoomcamp`.

### Reminder
- Ensure that the PostgreSQL database name in the Docker Compose matches what you configure in your flow.