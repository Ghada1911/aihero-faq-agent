---
id: 87e92edf02
question: 'Docker: ny_taxi_postgres_data is empty'
sort_order: 19
---

Even after properly running the Docker script, the folder may appear empty in VS Code. For Windows, try the following steps:

**Solution 1:**

Run the Docker command with the absolute path quoted in the `-v` parameter:

```bash
winpty docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v "C:\Users\abhin\dataengg\DE_Project_git_connected\DE_OLD\week1_set_up\docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data" \
  -p 5432:5432 \
  postgres:13
```

This should resolve the visibility issue in the VS Code `ny_taxi` folder.

**Note:** Ensure the correct direction for the slashes: `/` versus `\`.

**Solution 2:**

Another possible solution for Windows is to finish the folder path with a forward slash `/`:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /"$(pwd)"/ny_taxi_postgres_data/:/var/lib/postgresql/data/ \
  -p 5432:5432 \
  postgres:13
```

These steps should help resolve the issue of the `ny_taxi_postgres_data` folder appearing empty in your Docker setup.