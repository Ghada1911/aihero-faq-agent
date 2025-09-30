---
id: c1eeebf4ce
question: 'Docker: Error response from daemon: error while creating buildmount source'
sort_order: 24
---

You may get this error:

```
error while creating buildmount source path '/run/desktop/mnt/host/c/<your path>': mkdir /run/desktop/mnt/host/c: file exists
```

When you encounter the error above while rerunning your Docker command, it indicates that you should not mount on the second run. Here’s the initial problematic command:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v <your path>:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

To resolve the issue, use the revised command without the volume mount:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -p 5432:5432 \
  postgres:13
```