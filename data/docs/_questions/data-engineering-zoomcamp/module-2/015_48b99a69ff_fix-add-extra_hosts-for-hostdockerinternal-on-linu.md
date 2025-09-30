---
id: 48b99a69ff
question: 'Fix: Add extra_hosts for host.docker.internal on Linux'
sort_order: 15
---

This update corrects the Docker Compose configuration to resolve the error when using the alias `host.docker.internal` on Linux systems. Since this alias does not resolve natively on Linux, the following entry was added to the affected container:

```
yaml
kestra:
  image: kestra/kestra:latest
  pull_policy: always
  user: "root"
  command: server standalone
  volumes:
    # Add volume configurations here
  environment:
    # Add environment variables here
  ports:
    # Add ports here
  depends_on:
    # Add dependencies here
  extra_hosts:
    - "host.docker.internal:host-gateway"
```

With this change, containers that need to access host services via `host.docker.internal` will be able to do so correctly. For inter-container communication within the same network, it is recommended to use the service name directly.