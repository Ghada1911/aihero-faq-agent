---
id: 7f7aa5f5e6
question: 'PGCLI - After installing PGCLI and checking with `pgcli --help` we get
  the error: `ImportError: no pq wrapper available`'
sort_order: 71
---

The error persists because the psycopg library cannot find the required libpq library. Ensure the required PostgreSQL client library is installed:

```bash
sudo apt install libpq-dev
```

Rebuild psycopg:

1. Uninstall the existing packages:
   
   ```bash
   pip uninstall psycopg psycopg_binary psycopg_c -y
   ```

2. Reinstall psycopg:
   
   ```bash
   pip install psycopg --no-binary psycopg
   ```

The issue should be resolved by now. However, if you still encounter the error:

`ModuleNotFoundError: No module named 'psycopg2'`

Then run the following:

```bash
pip install psycopg2-binary
```