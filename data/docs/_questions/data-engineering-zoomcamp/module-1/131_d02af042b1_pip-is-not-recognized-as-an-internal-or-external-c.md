---
id: d02af042b1
question: '''pip'' is not recognized as an internal or external command, operable
  program or batch file.'
sort_order: 131
---

If you use Anaconda (recommended for the course), it comes with `pip`, so the issue is probably that Anaconda’s Python is not on the PATH.


**For Linux and MacOS:**

1. Open a terminal.
2. Find the path to your Anaconda installation. This is typically `~/anaconda3` or `~/opt/anaconda3`.
3. Add Anaconda to your PATH with the command:
   
   ```bash
   export PATH="/path/to/anaconda3/bin:$PATH"
   ```

4. To make this change permanent, add the command to your `.bashrc` (Linux) or `.bash_profile` (MacOS) file.

**On Windows, using Git Bash:**

1. Locate your Anaconda installation. The default path is usually `C:\Users\[YourUsername]\Anaconda3`.
2. Convert the Windows path to a Unix-style path for Git Bash, e.g., `C:\Users\[YourUsername]\Anaconda3` becomes `/c/Users/[YourUsername]/Anaconda3`.
3. Add Anaconda to your PATH with the command:

   ```bash
   export PATH="/c/Users/[YourUsername]/Anaconda3/:/c/Users/[YourUsername]/Anaconda3/Scripts/$PATH"
   ```

4. To make this change permanent, add the command to your `.bashrc` file in your home directory.
5. Refresh your environment with the command:

   ```bash
   source ~/.bashrc
   ```

**For Windows (without Git Bash):**

1. Right-click on 'This PC' or 'My Computer' and select 'Properties'.
2. Click on 'Advanced system settings'.
3. In the System Properties window, click on 'Environment Variables'.
4. In the Environment Variables window, select the 'Path' variable in the 'System variables' section and click 'Edit'.
5. In the Edit Environment Variable window, click 'New' and add the path to your Anaconda installation (typically `C:\Users\[YourUsername]\Anaconda3` and `C:\Users\[YourUsername]\Anaconda3\Scripts`).
6. Click 'OK' in all windows to apply the changes.

After adding Anaconda to the PATH, you should be able to use `pip` from the command line. Remember to restart your terminal (or command prompt in Windows) to apply these changes.