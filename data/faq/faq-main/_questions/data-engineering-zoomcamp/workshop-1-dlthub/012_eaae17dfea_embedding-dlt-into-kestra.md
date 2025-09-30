---
id: eaae17dfea
question: Embedding dlt into Kestra
sort_order: 12
---

```yaml
id: dlt_ingestion

namespace: my.dlt

description: "Run dlt pipeline with Kestra"

tasks:

- id: run_dlt

  type: io.kestra.plugin.scripts.python.Commands

  commands:

  - |

    import dlt

    from my_dlt_pipeline import load_data  # Import your dlt function

    pipeline = dlt.pipeline(

      pipeline_name="kestra_pipeline",

      destination="duckdb",

      dataset_name="kestra_dataset"

    )

    info = pipeline.run(load_data())

    print(info)
```