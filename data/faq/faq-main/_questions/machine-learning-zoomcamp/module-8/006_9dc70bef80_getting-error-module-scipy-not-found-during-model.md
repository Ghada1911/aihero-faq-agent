---
id: 9dc70bef80
question: Getting error module scipy not found during model training in Saturn Cloud
  tensorflow image
sort_order: 6
---

The error occurs because the `scipy` module is not installed in the Saturn Cloud TensorFlow image.

To resolve this issue:

1. When creating the Jupyter server resource, navigate to the "Extra Packages" section.
2. In the pip textbox, write `scipy`.
3. A command will appear below the textbox: `pip install scipy`.
4. This ensures that when the resource starts, the `scipy` package will be automatically installed.

This method can be used to install additional Python packages as needed.