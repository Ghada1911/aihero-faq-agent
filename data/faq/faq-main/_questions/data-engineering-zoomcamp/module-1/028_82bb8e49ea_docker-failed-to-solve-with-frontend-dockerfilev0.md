---
id: 82bb8e49ea
question: 'Docker: failed to solve with frontend dockerfile.v0: failed to read dockerfile:
  error from sender: open ny_taxi_postgres_data: permission denied.'
sort_order: 28
---

This issue occurs on Ubuntu/Linux systems when attempting to rebuild the Docker container.

```bash
$ docker build -t taxi_ingest:v001 .
```

A folder is created to host the Docker files. When the build command is executed again, a permission error may occur because there are no permissions on this new folder. To resolve this, grant permissions by running the command:

```bash
$ sudo chmod -R 755 ny_taxi_postgres_data
```

If issues persist, use:

```bash
$ sudo chmod -R 777 ny_taxi_postgres_data
```

Note: 755 grants write access only to the owner.