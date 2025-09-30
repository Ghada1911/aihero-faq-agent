---
id: e532c9677e
question: 'Docker-Compose: cannot execute binary file: Exec format error'
sort_order: 52
---

This error indicates that the docker-compose executable cannot be opened in the current OS. Ensure that the file you download from GitHub matches your system environment.

As of 2025/1/17, docker-compose ([v2.32.4](https://github.com/docker/compose/releases/tag/v2.32.4)) [docker-compose-linux-aarch64](https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-linux-aarch64) does not work. Try v2.32.3 [docker-compose-linux-x86_64](https://github.com/docker/compose/releases/download/v2.32.3/docker-compose-linux-x86_64).