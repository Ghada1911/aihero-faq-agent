---
id: df4171cea7
question: 'Fix: Add extra_hosts for taskRunner in the dbt-build'
sort_order: 16
---

To resolve the issue with `host.docker.internal` not being recognized on Linux, add the `extraHosts` configuration to the `taskRunner` in the `dbt-build` task:

```yaml
taskRunner:
  type: io.kestra.plugin.scripts.runner.docker.Docker
  extraHosts:
    - "host.docker.internal:host-gateway"
```