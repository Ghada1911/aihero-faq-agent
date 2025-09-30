---
id: b26658a658
question: How to automatically infer the column data type (pandas missing value issues)?
sort_order: 46
---

Problem: When injecting data to BigQuery, you may face a type error. This is because pandas by default will parse integer columns with missing values as float type.

Solution:

One way to solve this problem is to specify or cast the data type as `Int64` during the data transformation stage.

If specifying all the integer columns is inconvenient, you can use `convert_dtypes` to infer the data type automatically.

- Make pandas infer the correct data type (as pandas parse int with missing as float):

```python
# Fill missing values with a placeholder
 df.fillna(-999999, inplace=True)

# Infer data types
 df = df.convert_dtypes()

# Replace placeholder with None
 df = df.replace(-999999, None)
```