---
id: 1c4ac5d626
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_7800f401.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_8efd4f76.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_4e68416b.png
question: Dbt deploy + Git CI - Unable to configure Continuous Integration (CI) with
  Github
sort_order: 36
---

If you’re trying to configure CI with Github and on the job’s options you can’t see `Run on Pull Requests?` on triggers, follow these steps to reconnect using a native connection instead of cloning by SSH:

1. **Connect Your Github Account**  
   - Go to `Profile Settings > Linked Accounts`.
   - Connect your Github account with the dbt project, allowing the requested permissions.  
   - More information can be found [here](https://docs.getdbt.com/docs/collaborate/git/connect-github).
   
   <{IMAGE:image_1}>
   
2. **Disconnect Current Configuration**  
   - Navigate to `Account Settings > Projects (analytics) > Github connection`.
   - Click the `Disconnect` button at the bottom left.

3. **Reconfigure Github Connection**  
   - After disconnecting, configure again by choosing Github.
   - Select your repository from all allowed repositories to work with dbt. Your setup will now be ready.
   
   <{IMAGE:image_2}>
   
4. **Configure Triggers**  
   - Go to `Deploy > Job Configuration`.
   - Scroll down to `Triggers` where you can see the option `Run on Pull Requests:`
   
   <{IMAGE:image_3}>
