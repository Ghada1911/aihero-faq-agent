---
id: 2e2f27a6c0
question: 'Replace: {{ dbt_utils.surrogate_key([ field_a, field_b, field_c, …, field_z
  ]) }}'
sort_order: 27
---

For this use:

```sql
{{ dbt_utils.generate_surrogate_key([ field_a, field_b, field_c, …, field_z ]) }}
```

Additionally, add a global variable in `dbt_project.yml`. (...)