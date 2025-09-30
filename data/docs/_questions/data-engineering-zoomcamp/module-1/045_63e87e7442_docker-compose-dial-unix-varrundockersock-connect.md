---
id: 63e87e7442
question: 'Docker-Compose - dial unix /var/run/docker.sock: connect: permission denied'
sort_order: 45
---

This happens if you did not create the docker group and add your user. Follow these steps from the link: [guides/docker-without-sudo.md at main · sindresorhus/guides · GitHub](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md)

1. Press `Ctrl+D` to log out and log back in again.

If you are tired of having to set up your database connection each time you start the containers, create a volume for pgAdmin:

In your `docker-compose.yaml` file, add the following under your pgAdmin service:

```yaml
services:
  pgadmin:
    volumes:
      - type: volume
        source: pgadmin_data
        target: /var/lib/pgadmin
```

Also, add the following to the end of the file:

```yaml
volumes:
  pgadmin_data:
```

This configuration will maintain the state so that pgAdmin remembers your previous connections.