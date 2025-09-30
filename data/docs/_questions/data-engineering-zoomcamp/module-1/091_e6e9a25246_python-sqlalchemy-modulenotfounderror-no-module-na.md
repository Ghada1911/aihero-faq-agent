---
id: e6e9a25246
question: 'Python: SQLAlchemy - ModuleNotFoundError: No module named ''psycopg2''.'
sort_order: 91
---


Error raised during the Jupyter Notebook cell execution:

```python
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
```

Solution:

Install the Python module `psycopg2`. It can be installed using Conda or pip:

- Using Conda:
  ```bash
  conda install psycopg2
  ```
- Using pip:
  ```bash
  pip install psycopg2
  ```