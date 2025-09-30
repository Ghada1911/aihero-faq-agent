---
id: 646e2067e8
question: 'Python - ModuleNotFoundError: No module named ''pysqlite2'''
sort_order: 83
---

```
ImportError: DLL load failed while importing _sqlite3: The specified module could not be found. 
ModuleNotFoundError: No module named 'pysqlite2'
```

The issue may arise due to the absence of `sqlite3.dll` in the path `".\Anaconda\Dlls\"`.

To resolve the issue:

1. Copy the `sqlite3.dll` file from `\Anaconda3\Library\bin`.
2. Paste the file into the `".\Anaconda\Dlls\"` directory.

This solution applies if you are using Anaconda.