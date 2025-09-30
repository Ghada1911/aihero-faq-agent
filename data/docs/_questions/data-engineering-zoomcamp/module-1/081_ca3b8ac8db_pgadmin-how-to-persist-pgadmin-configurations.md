---
id: ca3b8ac8db
question: 'pgAdmin: How to Persist pgAdmin Configurations'
sort_order: 81
---

To keep pgAdmin settings after restarting the container, follow these steps:

1. Create the directory for pgAdmin data:
   
   ```bash
   mkdir -p /path/to/pgadmin-data
   ```

2. Assign ownership to pgAdmin's user (ID 5050):
   
   ```bash
   sudo chown -R 5050:5050 /path/to/pgadmin-data
   ```

3. Set the appropriate permissions:
   
   ```bash
   sudo chmod -R 755 /path/to/pgadmin-data
   ```