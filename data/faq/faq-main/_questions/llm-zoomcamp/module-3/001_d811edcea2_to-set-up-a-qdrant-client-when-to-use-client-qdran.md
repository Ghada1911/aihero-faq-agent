---
id: d811edcea2
question: To set up a Qdrant client, when to use `client = QdrantClient("http://localhost:6333")`
  vs `client = QdrantClient(":memory:")`?
sort_order: 1
---

Use the former if you are running Qdrant in Docker locally and need to connect your notebook to the Qdrant server running in Docker.

The latter option creates an in-memory Qdrant instance that runs inside your Python process. This means:

- It's only for testing or prototyping.
- It is not connected to your Docker-based Qdrant.
- It is wiped clean when the notebook or script stops.