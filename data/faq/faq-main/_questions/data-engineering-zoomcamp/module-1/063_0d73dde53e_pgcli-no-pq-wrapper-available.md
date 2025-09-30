---
id: 0d73dde53e
question: PGCLI - no pq wrapper available.
sort_order: 63
---

**Error:**

```
ImportError: no pq wrapper available.
```

### Problem Details:

- Could not import `\dt`
- `opg 'c' implementation: No module named 'psycopg_c'`
- `couldn't import psycopg 'binary' implementation: No module named 'psycopg_binary'`
- `couldn't import psycopg 'python' implementation: libpq library not found`

### Solution:

1. **Check Python Version:**
   
   Ensure your Python version is at least 3.9. The `'psycopg2-binary'` might fail to install on older versions like 3.7.3.
   
   ```bash
   $ python -V
   ```

2. **Environment Setup:**

   - If your Python version is not 3.9, create a new environment:
     
     ```bash
     $ conda create --name de-zoomcamp python=3.9
     $ conda activate de-zoomcamp
     ```

3. **Install Required Libraries:**

   - Install Postgres libraries:
     
     ```bash
     $ pip install psycopg2-binary
     $ pip install psycopg_binary
     ```

4. **Upgrade pgcli:**

   - If the above steps do not work, try upgrading `pgcli`:
     
     ```bash
     $ pip install --upgrade pgcli
     ```

5. **Install pgcli via Conda:**

   - Make sure to also install `pgcli` using conda:
     
     ```bash
     $ conda install -c conda-forge pgcli
     ```

If you follow these steps, you should be able to resolve the issue.