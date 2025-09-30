---
id: 3e83372387
question: 'Docker: invalid reference format: repository name must be lowercase (Mounting
  volumes with Docker on Windows)'
sort_order: 22
---

Mapping volumes on Windows can be tricky. If the approach shown in the course video doesn't work for you, consider the following suggestions:

- Move your data to a directory without spaces. For example, move from `C:/Users/Alexey Grigorev/git/...` to `C:/git/...`.

- Replace the `-v` part with one of these options:

  ```bash
  -v /c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data
  -v //c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data
  -v /c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data
  -v //c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data
  --volume //driveletter/path/ny_taxi_postgres_data/:/var/lib/postgresql/data
  ```

- Add `winpty` before the whole command:

  ```bash
  winpty docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:1
  ```

- Try adding quotes:

  ```bash
  -v "/c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"
  -v "//c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"
  -v “/c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"
  -v "//c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"
  -v "c:\some\path\ny_taxi_postgres_data":/var/lib/postgresql/data
  ```

- Note: If Windows automatically creates a folder called `ny_taxi_postgres_data;C`, it suggests a problem with volume mapping. Try deleting both folders and replacing the `-v` part with other options. Using `//c/` instead of `/c/` might work, as it creates the correct folder `ny_taxi_postgres_data`.

- A possible solution is using `"$(pwd)"/ny_taxi_postgres_data:/var/lib/postgresql/data` and pay attention to the placement of quotes.

- If none of these work, use a volume name instead of the path:

  ```bash
  -v ny_taxi_postgres_data:/var/lib/postgresql/data
  ```

- For Mac, you can wrap `$(pwd)` with quotes:

  ```bash
  docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v "$(pwd)"/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
  ```

Source: [StackOverflow](https://stackoverflow.com/questions/48522615/docker-error-invalid-reference-format-repository-name-must-be-lowercase)