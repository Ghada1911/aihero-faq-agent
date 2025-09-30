---
id: a19360f1ab
question: 'Getting error when connect git on Saturn Cloud: permission denied'
sort_order: 10
---

When following module 8.1b video to set up Git in Saturn Cloud, running the command:

```bash
ssh -T git@github.com
```

results in the error:

```bash
Permission denied (publickey).
```


An alternative method involves setting up Git in your Saturn Cloud environment by generating an SSH key in Saturn Cloud and adding it to your Git account. After completing this setup, you can access and manage your Git repositories through Saturn’s Jupyter server.

For detailed steps, refer to this tutorial: [https://saturncloud.io/docs/using-saturn-cloud/gitrepo/](https://saturncloud.io/docs/using-saturn-cloud/gitrepo/)
