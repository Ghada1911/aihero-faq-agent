---
id: 0f8512fc2a
question: Spark - Installation Error Code 1603
sort_order: 10
---

**Issue:** Spark installation on Windows completed but failed to run.

This is a common Windows Installer error code indicating that there was a fatal error during installation. It often occurs due to issues like insufficient permissions, conflicts with other software, or problems with the installer package.

### Step to Solve the Issue:

#### Installing Chocolatey

Chocolatey is a package manager for Windows, which makes it easy to install, update, and manage software.

**Installation Steps**

1. **Open PowerShell as an Administrator**
   - Press `Win + X` and select **Windows PowerShell (Admin)** or search for PowerShell, right-click, and select **Run as administrator**.

2. **Run the following command to install Chocolatey:**
   
   ```bash
   Set-ExecutionPolicy Bypass -Scope Process -Force; \
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \
   iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

3. **Verify the installation**
   - Close and reopen PowerShell as an administrator and run:
   
   ```bash
   choco -v
   ```
   - You should see the Chocolatey version number indicating that it has been installed successfully.

4. **Command for Global Acceptance**
   - To globally accept all licenses for all packages installed using Chocolatey, run the following command:
   
   ```bash
   choco feature enable -n allowGlobalConfirmation
   ```
   - This command configures Chocolatey to automatically accept license agreements for all packages, streamlining the installation process and avoiding prompts for each package.