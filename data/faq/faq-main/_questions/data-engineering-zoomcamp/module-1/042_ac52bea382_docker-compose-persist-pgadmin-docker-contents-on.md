---
id: ac52bea382
question: 'Docker-Compose: Persist PGAdmin docker contents on GCP'
sort_order: 42
---

One common issue when running Docker Compose on GCP is that PostgreSQL might not persist its data to the specified path. For example:

```yaml
services:
  ...
  pgadmin:
    ...
    volumes:
      - "./pgadmin:/var/lib/pgadmin:wr"
```

This setup might not work. To resolve this, use Docker Volume to make the data persist:

```yaml
services:
  ...
  pgadmin:
    ...
    volumes:
      - pgadmin:/var/lib/pgadmin

volumes:
  pgadmin:
```

This configuration change ensures the persistence of the PGAdmin data on GCP.