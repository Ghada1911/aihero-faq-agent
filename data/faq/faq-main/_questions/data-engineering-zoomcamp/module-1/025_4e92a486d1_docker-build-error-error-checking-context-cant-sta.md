---
id: 4e92a486d1
question: 'Docker: build error: error checking context: ''can''t stat ''/home/user/repos/data-engineering/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data''''.'
sort_order: 25
---

This error appeared when running the command:

```bash
docker build -t taxi_ingest:v001 .
```

The issue often arises because the user ID of the directory `ny_taxi_postgres_data` was changed, causing permission errors when accessing it. To resolve this error, use a directory containing only the necessary files, `Dockerfile` and `ingest_data.py`.

If you need to change permissions, use the following command on Ubuntu:

```bash
sudo chown -R $USER dir_path
```

On Windows, follow the instructions in this guide: [The Geek Page](https://thegeekpage.com/take-ownership-of-a-file-folder-through-command-prompt-in-windows-10/).

For more information, refer to this explanation on Stack Overflow: [Docker build error checking context](https://stackoverflow.com/questions/41286028/docker-build-error-checking-context-cant-stat-c-users-username-appdata).