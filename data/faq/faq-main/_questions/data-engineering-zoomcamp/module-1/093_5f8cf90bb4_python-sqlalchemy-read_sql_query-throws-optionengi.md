---
id: 5f8cf90bb4
question: Python - SQLAlchemy - read_sql_query() throws "'OptionEngine' object has
  no attribute 'execute'"
sort_order: 93
---

First, check the versions of SQLAlchemy and Pandas to ensure they are both up-to-date. You can upgrade them using `pip` or `conda` if needed.

Then, try to wrap the query using `text`:

```python
from sqlalchemy import text

query = text("SELECT * FROM tbl")
df = pd.read_sql_query(query, conn)
```