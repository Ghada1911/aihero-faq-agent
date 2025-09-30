---
id: 094dc060a4
question: AppendableIndex error in minsearch
sort_order: 6
---

### Error

```
ImportError: cannot import name 'AppendableIndex' from 'minsearch'
```

### Fix

1. Run the following command to upgrade:
   
   ```bash
   pip install --upgrade minsearch
   ```

2. Ensure you are using minsearch version 0.0.4.

3. Restart the Jupyter kernel after the upgrade.