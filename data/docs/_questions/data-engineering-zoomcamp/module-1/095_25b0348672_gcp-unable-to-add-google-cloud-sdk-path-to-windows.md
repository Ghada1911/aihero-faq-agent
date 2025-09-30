---
id: 25b0348672
question: 'GCP: Unable to add Google Cloud SDK PATH to Windows'
sort_order: 95
---

### Issue

Windows error:

```
The installer is unable to automatically update your system PATH. Please add C:\tools\google-cloud-sdk\bin
```

### Solution

If you encounter this error frequently, consider the following steps:

1. **Add Gitbash to Windows Path:**
   
   - **Using Conda:**
     - Download the Anaconda Navigator.
     - During installation, check the box to add Conda to the path (even though it's not recommended).

2. **Install Git Bash:**

   - If not installed, install Git Bash.
   - If installed, consider reinstalling it.
   - During installation, ensure you check:
     - Add GitBash to Windows Terminal
     - Use Git and optional Unix tools from the command prompt

3. **Setup Git Bash:**

   - Open Git Bash and type the following command:
     
     ```bash
     conda init bash
     ```
   
   - This will modify your bash profile.

4. **Set Gitbash as Default Terminal:**

   - Open the Windows Terminal.
   - Go to settings.
   - Change the default profile from Windows PowerShell to Git Bash.

By following these steps, you should be able to add the Google Cloud SDK path to your system on Windows without issues.