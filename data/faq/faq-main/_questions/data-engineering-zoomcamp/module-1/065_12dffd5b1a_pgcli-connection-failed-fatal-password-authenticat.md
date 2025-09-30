---
id: 12dffd5b1a
images:
question: 'PGCLI -connection failed: FATAL: password authentication failed for user
  "root"'
sort_order: 65
---

The error above was faced continually despite inputting the correct password.


1. **Stop the PostgreSQL service on Windows**

2. **Using WSL:** Completely uninstall PostgreSQL 12 from Windows and install `postgresql-client` on WSL:  

```bash
sudo apt install postgresql-client-common postgresql-client libpq-dev
```

3. **Change the port of the Docker container**

4. **Keep the Database Connection:**
   
If you encounter the error:
   
```
PGCLI -connection failed: FATAL: password authentication failed for user "root"
```
   
It might be because the connection to the `Postgres:13` image was closed. Ensure you keep the database connected in order to continue with the tutorial steps, using the following command:

```bash
docker run -it \
   -e POSTGRES_USER=root \
   -e POSTGRES_PASSWORD=root \
   -e POSTGRES_DB=ny_taxi \
   -v d:/git/data-engineering-zoomcamp/week_1/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
   -p 5432:5432 \
   postgres:13
```

You should see this 

```
2024-01-26 20:14:43.124 UTC [1] LOG:  database system is ready to accept connections
```

5. **Change the Port for Docker PostgreSQL:**

   After running the command `pgcli -h localhost -p 5432 -u root -d ny_taxi`, if prompted for a password, the error may persist due to local Postgres installation. To resolve this port conflict between host and container:

   - Configure your Docker PostgreSQL container to use a different port. Map it to a different port on your host machine:
   
```bash
docker run -it \
   -e POSTGRES_USER="root" \
   -e POSTGRES_PASSWORD="root" \
   -e POSTGRES_DB="ny_taxi" \
   -v c:/workspace/de-zoomcamp/1_intro_to_data_engineering/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
   -p 5433:5432 \
   postgres:13
```

- `5433` refers to the port on the host machine.
- `5432` refers to the port inside the Docker Postgres container.