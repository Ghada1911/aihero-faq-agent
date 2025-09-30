---
id: 38fe6ace53
question: I'm getting the error “cannot import name 'VectorSearch' from 'minsearch'”
  even though I installed the latest version of minsearch. How can I fix it?
sort_order: 2
---

If you're working with Jupyter notebooks, make sure the kernel you're using has the correct version of `minsearch`. You can check the version in your kernel with:

```python
minsearch.__version__
```

You can also try installing the latest version directly from a notebook cell using:

```python
%pip install -U minsearch
```

`%pip` is a Jupyter magic command that ensures the package gets installed in the same environment your notebook kernel is using. This can prevent issues that arise with `!pip`, which might install it in a different environment.