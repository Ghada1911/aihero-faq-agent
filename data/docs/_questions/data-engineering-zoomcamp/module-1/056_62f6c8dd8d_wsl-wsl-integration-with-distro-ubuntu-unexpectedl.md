---
id: 62f6c8dd8d
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_bc654841.png
question: 'WSL: WSL integration with distro Ubuntu unexpectedly stopped with exit
  code 1.'
sort_order: 56
---

<{IMAGE:image_1}>

Upon restarting, the same issue appears and occurs unexpectedly on Windows.

**Solutions:**

1. **Fixing DNS Issue**
   
   This solution is credited to [reddit](https://www.reddit.com/r/docker/comments/p98xq6/docker_failed_to_start_exit_code_1/) and has worked for some users.

   ```bash
   reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "4" /f
   ```

   Restart your computer and then re-enable it with the following command:

   ```bash
   reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "2" /f
   ```

   Restart your OS again. It should work.

2. **Switch to Linux Containers**

   - Right-click on the running Docker icon (next to the clock).
   - Choose "Switch to Linux containers."

```bash
bash: conda: command not found
```

```bash
Database is uninitialized and superuser password is not specified.
```

```bash
Database is uninitialized and superuser password is not specified.
```
