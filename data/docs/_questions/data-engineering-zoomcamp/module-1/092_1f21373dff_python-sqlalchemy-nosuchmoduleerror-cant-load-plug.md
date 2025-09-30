---
id: 1f21373dff
question: 'Python - SQLAlchemy: NoSuchModuleError: Can''t load plugin: sqlalchemy.dialects:postgresql.psycopg'
sort_order: 92
---

Error raised during the Jupyter notebook’s cell execution:

```python
conn_string = "postgresql+psycopg://root:root@localhost:5432/ny_taxi"

engine = create_engine(conn_string)
```

Solution: 

We had a scenario of a virtual environment (created by PyCharm) being run on top of another virtual environment (on conda). The solution was:

1. Remove the `.venv`.
2. Create a new virtual environment with conda:
   
   ```bash
   conda create -n pyingest python=3.12
   ```

3. Install the required dependencies:
   
   ```bash
   pip install pandas sqlalchemy psycopg2-binary jupyterlab
   ```

4. Re-execute the code.

For `psycopg2`, the connection string should be:

```python
postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}
```

Reference - Kayla Tinker 1/14/25