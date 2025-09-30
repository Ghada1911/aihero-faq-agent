---
id: c76ca2f769
question: How to upload Kaggle data to Saturn Cloud?
sort_order: 7
---

Uploading data directly from Kaggle to Saturn Cloud can save time, especially for large datasets. You can download it to your local machine and then upload it to Saturn Cloud, but there is a more efficient method.


1. **Install Kaggle Package**
   
   Run the following command in your notebook:
   
   ```bash
   !pip install -q kaggle
   ```

2. **Generate Kaggle API Token**
   
   - Go to the Kaggle website and log into your account.
   - Click on your profile image and select "Account."
   - Scroll down to the "API" section.
   - Click on "Create New API Token." A JSON file named `kaggle.json` will download to your local computer.

3. **Upload the Kaggle API Token to Saturn Cloud**
   
   - In your notebook, click on the folder icon in the upper left corner to navigate to the root folder.
   - Click on the `.kaggle` folder.
   - Upload the `kaggle.json` file into the `.kaggle` folder.

4. **Set File Permissions**
   
   Run this command to secure your Kaggle API token:
   
   ```bash
   !chmod 600 /home/jovyan/.kaggle/kaggle.json
   ```

5. **Download the Dataset**
   
   Use the following command to download your desired dataset (e.g., the "dino-or-dragon" dataset):
   
   ```bash
   !kaggle datasets download -d agrigorev/dino-or-dragon
   ```

6. **Unzip the Dataset**
   
   - Create a folder to unzip your files:
     
     ```bash
     !mkdir data
     ```
   
   - Unzip your files inside that folder:
     
     ```bash
     !unzip dino-or-dragon.zip -d data
     ```

By following these steps, you set up Saturn Cloud with access to all Kaggle datasets efficiently.