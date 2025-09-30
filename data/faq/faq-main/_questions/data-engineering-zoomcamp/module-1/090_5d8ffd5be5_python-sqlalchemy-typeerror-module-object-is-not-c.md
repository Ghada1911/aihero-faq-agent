---
id: 5d8ffd5be5
question: Python - SQLALchemy - TypeError 'module' object is not callable
sort_order: 90
---

When using `create_engine('postgresql://root:root@localhost:5432/ny_taxi')`, you may encounter the error:

```
TypeError: 'module' object is not callable
```
Use the correct connection string syntax:


```python
conn_string = "postgresql+psycopg://root:root@localhost:5432/ny_taxi"
engine = create_engine(conn_string)
```