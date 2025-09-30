---
id: e644e2b7b6
question: 'PGCLI - FATAL: password authentication failed for user "root" (You already
  have Postgres)'
sort_order: 61
---

For a more visual and detailed explanation, feel free to check the video [1.4.2 - Port Mapping and Networks in Docker](https://www.youtube.com/watch?v=tOr4hTsHOzU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=16&ab_channel=DataTalksClub%E2%AC%9B).

If you want to debug the issue on MacOS, you can try the following steps:

- **Check if something is blocking your port:**
  
  Use the `lsof` command to find out which application is using a specific port on your local machine:
  
  ```bash
  lsof -i :5432
  ```

- **List running PostgreSQL services:**

  Use `launchctl` to list running postgres services on your local machine.

- **Unload the running service:**

  Unload the launch agent for the PostgreSQL service, which will stop the service and free up the port:
  
  ```bash
  launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
  ```

- **Restart the service:**

  ```bash
  launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
  ```

- **Change the port:**

  Changing the port from `5432:5432` to `5431:5432` can help avoid this error.