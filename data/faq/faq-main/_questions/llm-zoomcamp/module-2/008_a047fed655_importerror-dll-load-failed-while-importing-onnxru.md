---
id: a047fed655
question: 'ImportError: DLL load failed while importing onnxruntime_pybind11_state:
  A dynamic link library (DLL) initialization routine failed.'
sort_order: 8
---

If you encounter this error while using Anaconda or Miniconda, try re-installing `onnxruntime` with the following command:

```bash
conda install -c conda-forge onnxruntime
```

To create an environment for using `qdrant-client[fastembed]>=1.14.2`, which may trigger this error, follow these steps:

1. **Create a Conda Environment**
   
   ```bash
   conda create --name llm-zoomcamp-env python=3.10
   ```

2. **Activate the Environment**
   
   ```bash
   conda activate llm-zoomcamp-env
   ```

3. **Install the Dependency**
   
   ```bash
   pip install "qdrant-client[fastembed]>=1.14.2"
   ```

4. **Use the Environment**
   
   - **Jupyter Notebook**: Activate the environment before launching Jupyter.
   - **VSCode/Cursor**: Use `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac), then select "Python Interpreter" and choose "llm-zoomcamp-env".