---
id: 409296db3e
question: 'Postgres - OperationalError: (psycopg2.OperationalError) connection to
  server at "localhost" (::1), port 5432 failed: FATAL: password authentication failed
  for user "root"'
sort_order: 72
---

This error occurs when uploading data via a connection in Jupyter Notebook:

```python
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
```

### Possible Solutions:

1. **Port Conflict:**
   - Port 5432 might be occupied by another Postgres installation on your local machine. This can lead to your connection not reaching Docker.
   - Try using a different port, such as 5431, or verify the port mapping.
   - Alternatively, remove any old or unnecessary Postgres installations if they're not in use.

2. **Windows Service Check:**
   - Check for any running services on Windows that might be using Postgres.
   - Stopping such services might resolve the issue. 
