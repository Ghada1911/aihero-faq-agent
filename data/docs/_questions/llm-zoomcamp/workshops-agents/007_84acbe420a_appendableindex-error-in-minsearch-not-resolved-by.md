---
id: 84acbe420a
question: AppendableIndex error in minsearch (not resolved by upgrading minsearch)
sort_order: 7
---

**Error:**

```python
ImportError: cannot import name 'AppendableIndex' from 'minsearch'
```

**Fix:**

```python
from minsearch.append import AppendableIndex
```