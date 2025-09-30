---
id: 35d7874a8d
question: 'Jupyter: Install, open Jupyter and convert Jupyter notebook to Python script'
sort_order: 134
---

### Install and Open Jupyter Notebook

To install Jupyter Notebook, run:

```bash
pip install jupyter
```

To open Jupyter Notebook, use:

```bash
python3 -m notebook
```

### Convert Jupyter Notebook to Python Script

First, ensure `nbconvert` is installed and upgraded:

```bash
pip install nbconvert --upgrade
```

Then, convert a Jupyter Notebook to a Python script with the following command:

```bash
python3 -m jupyter nbconvert --to=script upload-data.ipynb
```
