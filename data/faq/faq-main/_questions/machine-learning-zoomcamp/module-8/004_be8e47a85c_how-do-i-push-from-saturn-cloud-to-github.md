---
id: be8e47a85c
question: How do I push from Saturn Cloud to Github?
sort_order: 4
---

Connecting your GPU on Saturn Cloud to a Github repository is not compulsory, as you can download the notebook and copy it to the Github folder manually. However, if you prefer an automated approach, follow these instructions:

1. **Create SSH Keys**:
   - Refer to the following GitHub documentation to generate an SSH private and public key:
     - [Generating a new SSH key and adding it to the SSH agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
     - [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui)

2. **Authenticating via Terminal**:
   - Access the second video in the Saturn Cloud module to learn how to add SSH keys to secrets and authenticate via a terminal.

3. **Using Saturn Cloud's Default Public Keys**
   - Click on your username and select "Manage".
   - In the "Git SSH keys" section, copy the default public key provided by Saturn Cloud.
   - Paste this key into the SSH keys section of your GitHub repository.
   - Open a terminal on Saturn Cloud and run the following command:

```bash
ssh -T git@github.com
```

You should receive a successful authentication notice.

Follow these steps to efficiently push from Saturn Cloud to GitHub.