---
id: 9f2048fc73
question: 'Bad int64 value: 0.0 error'
sort_order: 53
---

Some ehail fees are null, causing a `Bad int64 value: 0.0` error when casting them to integer.

Solution:

- Use `safe_cast`, which returns NULL instead of throwing an error. Implement `safe_cast` from the `dbt_utils` function in Jinja code for casting into integer as follows:

  ```jinja
  {{ dbt_utils.safe_cast('ehail_fee', api.Column.translate_type("integer")) }} as ehail_fee,
  ```

- Alternatively, use `safe_cast(ehail_fee as integer)` without relying on `dbt_utils`.