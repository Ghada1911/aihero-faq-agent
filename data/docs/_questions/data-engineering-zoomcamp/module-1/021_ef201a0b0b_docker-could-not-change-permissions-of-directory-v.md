---
id: ef201a0b0b
question: 'Docker - Could not change permissions of directory "/var/lib/postgresql/data":
  Operation not permitted'
sort_order: 21
---

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="admin" \
  -e POSTGRES_DB="ny_taxi" \
  -v "/mnt/path/to/ny_taxi_postgres_data":"/var/lib/postgresql/data" \
  -p 5432:5432 \
  postgres:13
```

**Error Message:**

```plaintext
The files belonging to this database system will be owned by user "postgres". 
The database cluster will be initialized with locale "en_US.utf8". 
The default database encoding has accordingly been set to "UTF8". 
Data page checksums are disabled.
fixing permissions on existing directory /var/lib/postgresql/data ...
initdb: error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted
```

**Solution:**

1. Create a local Docker volume and map it to the Postgres data directory `/var/lib/postgresql/data`.
   
   - The volume name `dtc_postgres_volume_local` must match in both commands below:

    ```bash
    docker volume create --name dtc_postgres_volume_local -d local
    ```

2. Run the Docker container using the created volume:

    ```bash
    docker run -it \
      -e POSTGRES_USER="root" \
      -e POSTGRES_PASSWORD="root" \
      -e POSTGRES_DB="ny_taxi" \
      -v dtc_postgres_volume_local:/var/lib/postgresql/data \
      -p 5432:5432 \
      postgres:13
    ```

3. Verify the command works in Docker Desktop under Volumes. The `dtc_postgres_volume_local` should be listed, but the folder `ny_taxi_postgres_data` will be empty as an alternative configuration is used.

**Alternate Error:**

```plaintext
initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
```

To resolve this, either remove or empty the directory "/var/lib/postgresql/data", or run `initdb`. 