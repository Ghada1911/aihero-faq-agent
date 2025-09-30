---
id: 26ff32cb35
question: 'Python - SQLAlchemy - ImportError: cannot import name ''TypeAliasType''
  from ''typing_extensions''.'
sort_order: 89
---


The following error occurs during the execution of a Jupyter notebook cell:

```python
from sqlalchemy import create_engine
```

Solution:

The issue can be resolved by ensuring the version of the Python module `typing_extensions` is 4.6.0 or later. You can update it using either Conda or pip:

- **Using Conda:**
  ```bash
  conda update typing_extensions
  ```

- **Using pip:**
  ```bash
  pip install --upgrade typing_extensions
  ```

For more details, you can refer to the [changelog for typing_extensions 4.6.0](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md#release-460-may-22-2023).