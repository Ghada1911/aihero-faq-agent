---
id: 432d3f7e09
question: 'Docker-Compose: Hostname does not resolve'
sort_order: 40
---

When encountering the error:

```
Error response from daemon: network 66ae65944d643fdebbc89bd0329f1409dec2c9e12248052f5f4c4be7d1bdc6a3 not found
```

Try the following steps:

1. Run `docker ps -a` to see all stopped and running containers.
2. Remove all containers to clean up the environment.
3. Execute `docker-compose up -d` again.

If facing issues connecting to the server at `localhost:8080` with the error:

```
Unable to connect to server: could not translate host name 'pg-database' to address: Name does not resolve
```

Consider these solutions:

- Use a new hostname without dashes, e.g., `pgdatabase`.
- Make sure to specify the Docker network and use the same network in both containers in your `docker-compose.yml` file.

Example `docker-compose.yml`:

```yaml
services:

  pgdatabase:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxi
    volumes:
      - "./ny_taxi_postgres_data:/var/lib/postgresql/data:rw"
    ports:
      - "5431:5432"
    networks:
      - pg-network

  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"
    networks:
      - pg-network

networks:
  pg-network:
    name: pg-network
```
