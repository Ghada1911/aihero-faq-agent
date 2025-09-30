---
id: 9ef838bb46
question: 'Docker: Compose up -d error getting credentials - err: exec: "docker-credential-desktop":
  executable file not found in %PATH%, out: ``'
sort_order: 49
---

To resolve this error, follow these steps:

1. Locate the `config.json` file for Docker, typically found in your home directory at `Users/username/.docker`.
2. Modify the `credsStore` setting to `credStore`.
3. Save the file and re-run your Docker Compose command.
