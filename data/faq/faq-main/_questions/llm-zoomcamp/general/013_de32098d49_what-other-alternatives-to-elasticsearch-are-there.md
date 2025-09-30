---
id: de32098d49
question: What other alternatives to ElasticSearch are there?
sort_order: 13
---

You could use some of these free alternatives to Elasticsearch:

- [Milvus](https://milvus.io/): An open-source library with similar functionalities to Elasticsearch.

- [OpenSearch](https://opensearch.org/): Another free open-source library that provides the same functionalities as Elasticsearch.

### Additional Considerations:

If you start using `multi-qa-distilbert-cos-v1` from [huggingface.co](https://huggingface.co/sentence-transformers/multi-qa-distilbert-cos-v1) and create embeddings to index them, consider the following:

- If the model is updated by the author, the indexed embeddings may become incompatible, requiring re-indexing.

- To prevent this, save the model locally. This ensures that your code continues to work even if the cloud model changes.