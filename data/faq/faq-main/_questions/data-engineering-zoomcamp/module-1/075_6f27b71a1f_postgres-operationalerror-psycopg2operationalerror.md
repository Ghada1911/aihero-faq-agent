---
id: 6f27b71a1f
question: 'Postgres - OperationalError: (psycopg2.OperationalError) connection to
  server at "localhost" (::1), port 5432 failed: FATAL:  database "ny_taxi" does not
  exist'
sort_order: 75
---

```
OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "ny_taxi" does not exist
```

Make sure PostgreSQL is running. You can check that by running:

```bash
docker ps
```

**Solution:**

- If you have PostgreSQL software installed on your computer previously, consider building your instance on a different port, such as 8080, instead of 5432.