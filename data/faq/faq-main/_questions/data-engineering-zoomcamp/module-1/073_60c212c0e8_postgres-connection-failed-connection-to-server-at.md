---
id: 60c212c0e8
question: 'Postgres: connection failed: connection to server at "127.0.0.1", port
  5432 failed: FATAL: password authentication failed for user "root"'
sort_order: 73
---

To resolve the issue of a failed connection to PostgreSQL due to password authentication, consider the following steps:

- **Check Port Usage**: Ensure that port 5432 is properly forwarded. If it is being used by another process, follow these steps to kill it:
  
  ```bash
  sudo lsof -i :5432
  sudo kill -9 PID
  ```

- **For Windows Users**: If PostgreSQL is running locally and pgAdmin4 is using the 5432 port, follow these instructions:
  
  1. Press **Win + R** to open the Run dialog.
  2. Type `services.msc` and press Enter.
  3. In the Services window, scroll down to find a service named like `PostgreSQL`, `postgresql-x64-13`, or similar, depending on your PostgreSQL version.
  4. Right-click the PostgreSQL service and select **Stop**.