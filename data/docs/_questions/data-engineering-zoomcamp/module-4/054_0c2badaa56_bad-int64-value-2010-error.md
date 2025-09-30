---
id: 0c2badaa56
question: 'Bad int64 value: 2.0/1.0 error'
sort_order: 54
---

You might encounter this when building the `fact_trips.sql` model. The issue may be with the `payment_type_description` field.

Using `safe_cast` as above would cause the entire field to become null. A better approach is to drop the offending decimal place, then cast to integer:

```sql
cast(replace({{ payment_type }},'.0','') as integer)
```