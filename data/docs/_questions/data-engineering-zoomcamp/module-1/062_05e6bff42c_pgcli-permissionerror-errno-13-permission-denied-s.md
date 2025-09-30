---
id: 05e6bff42c
question: 'PGCLI - PermissionError: [Errno 13] Permission denied: ''/some/path/.config/pgcli'''
sort_order: 62
---

I encountered this error:

```bash
pgcli -h localhost -p 5432 -U root -d ny_taxi

Traceback (most recent call last):
  File "/opt/anaconda3/bin/pgcli", line 8, in <module>
    sys.exit(cli())
  File "/opt/anaconda3/lib/python3.9/site-packages/click/core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "/opt/anaconda3/lib/python3.9/site-packages/click/core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "/opt/anaconda3/lib/python3.9/site-packages/click/core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/opt/anaconda3/lib/python3.9/site-packages/click/core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "/opt/anaconda3/lib/python3.9/site-packages/pgcli/main.py", line 880, in cli
    os.makedirs(config_dir)
  File "/opt/anaconda3/lib/python3.9/os.py", line 225, in makedirspython
    mkdir(name, mode)
PermissionError: [Errno 13] Permission denied: '/Users/vray/.config/pgcli'
```

### Solution 1:

This error indicates that your user doesn’t have the necessary permissions to access or modify the directory or file (`/some/path/.config/pgcli`). This can occur in Docker environments when privileges are assigned to root instead of the current user.

To resolve this:

1. Check the file permissions:

   ```bash
   ls -l /some/path/.config/pgcli
   ```

2. Change the ownership/permissions so that your user has the necessary permissions:

   ```bash
   sudo chown -R user_name /Users/user_name/.config
   ```

   - `sudo` stands for Super User DO.
   - `chown` means change owner.
   - `-R` applies recursively.
   - `user_name` is your PC username (e.g., vray).

### Solution 2:

Make sure you install pgcli without using `sudo`. The recommended approach is to use conda/anaconda to avoid affecting your system Python.

If `conda install` gets stuck at "Solving environment," try these alternatives:

[https://stackoverflow.com/questions/63734508/stuck-at-solving-environment-on-anaconda](https://stackoverflow.com/questions/63734508/stuck-at-solving-environment-on-anaconda)