---
id: 70eceb1a01
question: Are there other ways to compute Precision, Recall and F1 score?
sort_order: 19
---

Scikit-learn offers another way: `precision_recall_fscore_support`.

Example:

```python
from sklearn.metrics import precision_recall_fscore_support

precision, recall, fscore, support = precision_recall_fscore_support(y_val, y_val_pred, zero_division=0)
```

