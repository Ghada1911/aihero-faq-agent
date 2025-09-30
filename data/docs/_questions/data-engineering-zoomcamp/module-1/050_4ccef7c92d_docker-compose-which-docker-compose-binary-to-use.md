---
id: 4ccef7c92d
question: 'Docker-Compose: Which docker-compose binary to use for WSL?'
sort_order: 50
---

To determine which `docker-compose` binary to download from [Docker Compose releases](https://github.com/docker/compose/releases), you can check your system with the following commands:

- To check the system type:

  ```bash
  uname -s  # This will most likely return 'Linux'
  ```

- To check the system architecture:

  ```bash
  uname -m  # This will return your system's 'flavor'
  ```

Alternatively, you can use the following command to download `docker-compose` directly:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```