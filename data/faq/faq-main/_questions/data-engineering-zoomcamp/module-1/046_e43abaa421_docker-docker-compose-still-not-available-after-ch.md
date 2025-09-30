---
id: e43abaa421
question: 'Docker: docker-compose still not available after changing .bashrc'
sort_order: 46
---

This issue can occur after installing Docker Compose in a Google Cloud VM, as demonstrated in video 1.4.1. 

If the downloaded Docker Compose file from GitHub is named `docker-compose-linux-x86_64`, you may need to rename it for convenience. Here's how to resolve the issue:

1. Rename `docker-compose-linux-x86_64` to `docker-compose` using the following command:
   
   ```bash
   mv docker-compose-linux-x86_64 docker-compose
   ```

By doing this, you can use the `docker-compose` command directly.