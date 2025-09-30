---
id: 50507316aa
question: 'Homework: When I re-run the code in Jupyter notebook multiple times for
  homework#1, the index building code snippet fails.'
sort_order: 22
---

To resolve this issue, you can delete any existing index with the same name before creating a new one.

```python
# Check if the index exists and delete it if it does
if es_client.indices.exists(index=index_name):
    print(f"Deleting existing index: {index_name}")
    es_client.indices.delete(index=index_name)
    print(f"Index {index_name} deleted.")
```

If you encounter issues with the index getting messed up and seeing different score outputs, follow these steps:

1. Go to Docker Desktop and stop the Elasticsearch container.
2. Delete the container image and re-initiate the Elasticsearch container by following the instructions in '1.6 Searching with ElasticSearch'.
3. Change the name of the index in your code to something other than `index_name = "course-questions"`.   