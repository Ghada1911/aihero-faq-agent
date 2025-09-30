---
id: 0470c11c69
question: AppendableIndex error in minsearch (not resolved by upgrading minsearch
  or importing from minsearch.append)
sort_order: 8
---

Error:

```
ImportError: cannot import name 'AppendableIndex' from 'minsearch'
```

Fix:

- Rename the previously downloaded `minsearch.py` file to avoid conflicts.
- Reinstall `minsearch` using pip so the import works correctly.