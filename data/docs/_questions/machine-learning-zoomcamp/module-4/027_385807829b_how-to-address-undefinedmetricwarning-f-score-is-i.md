---
id: 385807829b
question: 'How to address UndefinedMetricWarning: F-score is ill-defined and being
  set to 0.0 in labels with no predicted samples?'
sort_order: 27
---

This warning occurs when your model doesn't predict any samples for certain labels, causing a zero-division error when calculating the F-score. The warning is triggered when there are no true positives or predicted positives for certain labels, leading to undefined precision or recall.

To address this, you can use the `zero_division` parameter in scikit-learn's `f1_score` function. This parameter defines what should happen in cases of zero division:

- **Set `zero_division=1`**: This will set the precision, recall, and F-score to 1 when no positive samples are predicted.
- **Set `zero_division=0`**: This is the default behavior, setting the metric to 0 when there are no predicted samples for a given label.
- **Set `zero_division='warn'`**: This is the default behavior, acts like 0 but also raises a warning.

Example usage:

```python
from sklearn.metrics import f1_score, precision_score, recall_score

# For precision score
precision = precision_score(y_true, y_pred, average='weighted', zero_division='warn')

# For recall score
recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)

# For f1-score
f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
```

