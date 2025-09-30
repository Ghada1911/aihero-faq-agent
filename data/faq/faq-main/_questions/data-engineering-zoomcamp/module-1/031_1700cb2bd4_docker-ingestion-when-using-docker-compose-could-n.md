---
id: 1700cb2bd4
question: 'Docker: ingestion when using docker-compose could not translate host name'
sort_order: 31
---

Typical error:
```python
n.exc.OperationalError: (psycopg2.OperationalError) could not translate host name "pgdatabase" to address: Name or service not known
```

**Solution:**

1. Run `docker-compose up -d` to start your containers.
2. Check which network is created by Docker, as it may differ from your expectations.
3. Use the actual network name in your ingestion script instead of "pg-network".
4. Confirm the correct database service name, replacing "pgdatabase" accordingly.

**Example:**
- "pg-network" might become "2docker_default".