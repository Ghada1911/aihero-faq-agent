---
id: 0812df9bf6
question: 'Docker: PostgreSQL Database directory appears to contain a database. Database
  system is shut down'
sort_order: 35
---

When you see this in logs, your container with PostgreSQL is not accepting any requests. Attempting to connect may result in the error:

```
connection failed: server closed the connection unexpectedly

This probably means the server terminated abnormally before or while processing the request.
```

To resolve this issue:

1. **Delete Data Directory**: Delete the directory with data (the one you map to the container using the `-v` flag) and restart the container.

2. **Preserve Critical Data**: If your data is critical, you may be able to reset the write-ahead log from within the Docker container. For more details, see [here](https://github.com/alexg9010/2025_data_engineering_zoomcamp/blob/master/01_docker/README.md#fix-broken-postgress-docker-container).

   ```bash
   docker run -it \
   -e POSTGRES_USER="root" \
   -e POSTGRES_PASSWORD="root" \
   -e POSTGRES_DB="ny_taxi" \
   -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
   -p 5432:5432 \
   --network pg-network \
   postgres:13 \
   /bin/bash -c 'gosu postgres pg_resetwal /var/lib/postgresql/data'
   ```