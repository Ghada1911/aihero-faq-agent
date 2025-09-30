---
id: 1ae137c022
question: 'Docker: can’t delete local folder that mounted to docker volume'
sort_order: 14
---

When a PostgreSQL Docker container is created, it may create a folder on the local machine to mount to a volume inside the container. This folder is often owned by user 999 and has read and write protection, preventing deletion by conventional means such as dragging it to the trash.

If you encounter an access error or need to delete the folder, you can use the following command:

```bash
sudo rm -r -f docker_test/
```

- `rm` : Command to remove files or directories.
- `-r` : Recursively remove directories and their contents.
- `-f` : Forcefully remove files/directories without prompting.
- `docker_test/` : The folder to be deleted.