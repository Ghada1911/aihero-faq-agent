---
id: a9081d1a79
question: Anaconda to PIP
sort_order: 133
---

To get a pip-friendly `requirements.txt` file from Anaconda, use the following steps:

1. Install pip in your Anaconda environment:
   ```bash
   conda install pip
   ```
2. Generate the `requirements.txt` file:
   ```bash
   pip list --format=freeze > requirements.txt
   ```

Note:
- `conda list -d > requirements.txt` will not work.
- `pip freeze > requirements.txt` may give odd pathing.