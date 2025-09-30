---
id: fb9fab513f
question: 'Docker: Error response from daemon: invalid mode: \Program Files\Git\var\lib\postgresql\data.'
sort_order: 23
---

Change the mounting path. Replace it with one of the following:

```bash
-v /e/zoomcamp/...:/var/lib/postgresql/data
```
Or

```bash
-v /c:/.../ny_taxi_postgres_data:/var/lib/postgresql/data
```

(Note: Include a leading slash in front of `c:`)