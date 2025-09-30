---
id: 6c9785b291
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_981381c8.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_ebc771b3.png
question: Orchestrating dbt cloud with Mage
sort_order: 11
---

You can trigger your dbt job in a Mage pipeline. Follow these steps:

1. Retrieve your dbt cloud API key from **Settings > API Tokens > Personal Tokens**. Add this key safely to your `.env` file. For example:

   ```bash
   dbt_api_trigger=dbt_**
   ```

2. Navigate to the job page in dbt cloud and find the API trigger link.

3. Create a custom Mage Python block with a simple HTTP request, as shown in [this example](https://github.com/Nogromi/ukraine-vaccinations/blob/master/2_mage/vaccination/custom/trigger_dbt_cloud.py).

   <{IMAGE:image_1}>

   <{IMAGE:image_2}>

4. Use the following script to trigger the dbt job:

   ```python
   from dotenv import load_dotenv
   from pathlib import Path

   dotenv_path = Path('/home/src/.env')
   load_dotenv(dotenv_path=dotenv_path)

   dbt_api_trigger = os.getenv('dbt_api_trigger')
   
   url = f"https://cloud.getdbt.com/api/v2/accounts/{dbt_account_id}/jobs/<job_id>/run/"

   headers = {
       "Authorization": f"Token {dbt_api_trigger}",
       "Content-Type": "application/json"
   }

   body = {
       "cause": "Triggered via API"
   }

   response = requests.post(url, headers=headers, json=body)
   ```

   Voilà! You've triggered a dbt job from your Mage pipeline.