---
id: 2d17397995
question: 'Compilation Error: Model ''<model_name>'' (<model_path>) depends on a node
  named ''<seed_name>'' which was not found (Production Environment)'
sort_order: 44
---

Make sure that you create a pull request from your Development branch to the Production branch (main by default). After that, check in your `seeds` folder to ensure the seed file is inside it. Another thing to check is your `.gitignore` file. Make sure that the `.csv` extension is not included.