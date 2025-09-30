---
id: 2db8d0cd4d
question: 'ElasticSearch: ERROR: Elasticsearch exited unexpectedly'
sort_order: 9
---

If you encounter the error "Elasticsearch exited unexpectedly," it's likely due to insufficient RAM allocated to Elasticsearch.

### Solution 1: Specify RAM Size

Specify the RAM size in the configuration:

```bash
docker run -it \
  --rm \
  --name elasticsearch \
  -m 4GB \
  -p 9200:9200 \
  -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

You can also try using `-m 2GB`.

### Solution 2: Set Memory Lock to False

Another possible solution is to set the `memory_lock` to false:

```bash
docker run -it \
  --rm \
  --name elasticsearch \
  -p 9200:9200 \
  -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
  -e "bootstrap.memory_lock=false" \
  docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```