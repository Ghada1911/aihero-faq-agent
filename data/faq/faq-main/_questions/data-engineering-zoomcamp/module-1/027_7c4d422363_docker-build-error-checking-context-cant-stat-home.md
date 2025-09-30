---
id: 7c4d422363
question: 'Docker: build error checking context: can’t stat ‘/home/fhrzn/Projects/…./ny_taxi_postgres_data’'
sort_order: 27
---

This issue occurs due to insufficient authorization rights to the host folder, which may cause it to appear empty.

**Solution:**

Add permission for everyone to the folder:

```bash
sudo chmod -R 777 <path_to_folder>
```

Example:

```bash
sudo chmod -R 777 ny_taxi_postgres_data/
```