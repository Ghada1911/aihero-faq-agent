---
id: 3124f13c7c
question: 'pgAdmin - Unable to connect to server: [Errno -3] Try again'
sort_order: 82
---

This error occurs when connecting pgAdmin with Docker Postgres. In the tutorial, the pgAdmin server creation under **Connection > Host name/address** uses `pg-database` and results in the above-mentioned error when saved.

### Solution 1:

- Verify that both containers are connected to `pg-network`:
  
  ```bash
  docker network inspect pg-network
  ```

- If the Docker Postgres container is not connected, connect it to `pg-network`:

  ```bash
  docker network connect pg-network postgresContainer_name
  ```
  
- Retry the connection. If the error persists, instead of using `pg-database` under **Connection > Host name/address**, try using the IP Address:

  - Use the IP address of the `postgresContainer_name` container (e.g., `172.19.0.3`) in the pgAdmin configuration instead of the container name or `pg-database`.