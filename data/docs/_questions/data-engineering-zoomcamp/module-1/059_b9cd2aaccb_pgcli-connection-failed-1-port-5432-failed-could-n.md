---
id: b9cd2aaccb
question: 'PGCLI - connection failed: :1), port 5432 failed: could not receive data
  from server: Connection refused could not send SSL negotiation packet: Connection
  refused'
sort_order: 59
---

To resolve the connection failure with PGCLI, use the following command to connect via socket:

```bash
pgcli -h 127.0.0.1 -p 5432 -u root -d ny_taxi
```

Ensure the database server is running and properly configured to accept connections.