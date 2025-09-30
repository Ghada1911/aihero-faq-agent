---
id: c1acd7331a
question: 'Dbt+git: It appears that I can''t edit the files because I''m in read-only
  mode. Does anyone know how I can change that?'
sort_order: 34
---

1. **Create a New Branch:**
   - You need to create a new branch for development to make changes.
   
   ```bash
   git checkout -b your-feature-branch
   ```
   
2. **Switch to the New Branch:**
   - This allows you to make edits.

   ```bash
   git checkout your-feature-branch
   ```

3. **Commit and Push Changes:**
   - Once you've made your changes, commit and push them to the main branch.

   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin your-feature-branch
   ```

4. **Merge Changes to Main:**
   - Finally, merge your changes from your feature branch to the main branch.