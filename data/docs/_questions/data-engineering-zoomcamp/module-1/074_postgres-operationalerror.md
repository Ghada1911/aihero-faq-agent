---
id: '3459487271'
question: 'Postgres - OperationalError: (psycopg2.OperationalError) connection to
  server at "localhost" (::1), port 5432 failed: FATAL:  role "root" does not exist'
sort_order: 74
---

This error can occur in the following scenarios:

- **Using `pgcli`**:
  ```bash
  pgcli -h localhost -p 5432 -U root -d ny_taxi
  ```
- **Uploading data via a connection in a Jupyter notebook**:
  ```python
  engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
  ```

### Solutions:

1. **Port Change**:
   - Change the port from 5432 to another port (e.g., 5431).
   - Example: Change `5432:5432` to `5431:5432`.

2. **User Change**:
   - Change `POSTGRES_USER=root` to `PGUSER=postgres`.

3. **Docker Solution**:
   - Run `docker compose down`.
   - Remove the folder containing the Postgres volume.
   - Run `docker compose up` again.

### Additional Resources:
For more details, refer to [this Stack Overflow discussion](https://stackoverflow.com/questions/60193781/postgres-with-docker-compose-gives-fatal-role-root-does-not-exist-error).