---
id: 00e8093b90
question: Running out of storage when using kestra with postgres on GCP VM
sort_order: 7
---

Running out of storage while trying to backfill. I realized my GCP VM only has 30GB of storage and I was using it up quickly. Here are a couple of suggestions for managing storage:

- **Clean up your GCP VM drive:** Use the command below to identify what is taking up the most space:

  ```bash
  sudo du -sh *
  ```

  - **(~1GB)** For me, the Anaconda installer was consuming a lot of space. If you no longer need it, you can delete it:
  
    ```bash
    rm -rf <anacondainstaller_fpath>
    ```

  - **(~3GB)** Anaconda itself takes up a lot of space. You can’t delete it entirely if you need Python, but you can clean it up significantly:
    
    ```bash
    conda clean --all -y
    ```

- **Clean up your Kestra files:** Use a purge flow. You can find a generic example here:
  
  [https://kestra.io/docs/administrator-guide/purge](https://kestra.io/docs/administrator-guide/purge)
  
  I wanted to perform the cleanup immediately, rather than waiting until the end of the month, so I adjusted the `endDate` to `"{{ now() }}"` and removed the trigger block. You can also choose whether to remove FAILED state executions.

- **Clean up your PostgreSQL database:** You can manually delete tables in pgAdmin, or set up a workflow in Kestra for it. I found it easy to do manually.