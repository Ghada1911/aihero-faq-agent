---
id: e087742204
question: 'Why am I getting `docker: invalid reference format` when trying to run
  Qdrant with a volume in Windows?'
sort_order: 7
---

If you're running the `docker run` command on **Windows (especially Command Prompt or PowerShell)** and you use `$(pwd)` to mount a volume, you'll likely get the following error:

```
docker: invalid reference format.
```

The expression `$(pwd)` is a Unix-style command used to get the current working directory. It **won’t work in Windows**, which causes Docker to misinterpret the image name or the `-v` argument, hence the “invalid reference format” error.

**Solution:**

1. Use the full absolute path instead of `$(pwd)`, for example:

   ```bash
   docker run -p 6333:6333 -p 6334:6334 \
   -v C:/Users/youruser/path/to/qdrant_storage:/qdrant/storage:z \
   qdrant/qdrant
   ```

2. Alternatively, use a named volume:

   ```bash
   docker volume create qdrant_storage
   
   docker run -p 6333:6333 -p 6334:6334 \
   -v qdrant_storage:/qdrant/storage \
   qdrant/qdrant
   ```