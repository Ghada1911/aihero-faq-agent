---
id: 02df9d0302
question: 'Docker: How do I store data persistently in Elasticsearch?'
sort_order: 11
---

When you stop the container, the data you previously added to Elasticsearch will be gone. To avoid this, add volume mapping:

1. Create a Docker volume:

   ```bash
   docker volume create elasticsearch_data
   ```

2. Run the Elasticsearch container with volume mapping:

   ```bash
   docker run -it \
   --rm \
   --name elasticsearch \
   -p 9200:9200 \
   -p 9300:9300 \
   -v elasticsearch_data:/usr/share/elasticsearch/data \
   -e "discovery.type=single-node" \
   -e "xpack.security.enabled=false" \
   docker.elastic.co/elasticsearch/elasticsearch:8.4.3
   ```