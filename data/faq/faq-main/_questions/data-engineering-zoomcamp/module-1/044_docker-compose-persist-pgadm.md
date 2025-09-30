---
id: '4146155608'
question: 'Docker-Compose: Persist PGAdmin configuration'
sort_order: 44
---

To persist pgAdmin configuration, such as the server name, modify your `docker-compose.yml` by adding a "volumes" section:

```yaml
services:

  pgdatabase:
    [...]

  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    volumes:
      - "./pgAdmin_data:/var/lib/pgadmin/sessions:rw"
    ports:
      - "8080:80"
```

In the example above, "pgAdmin_data" is a folder on the host machine, and "/var/lib/pgadmin/sessions" is the session settings folder in the pgAdmin container.

Before running `docker-compose up` on the YAML file, provide the pgAdmin container with access permissions to the "pgAdmin_data" folder. The container runs with a username "5050" and user group "5050". Use the following command to set permissions:

```bash
sudo chown -R 5050:5050 pgAdmin_data
```