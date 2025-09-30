---
id: 639151c1d1
question: 'AttributeError: ''DataFrame'' object has no attribute ''iteritems'''
sort_order: 30
---

Another alternative is to install pandas 2.0.1 (it worked well at the time of writing this), and it is compatible with Pyspark 3.5.1. Make sure to add or edit your environment variable like this:

```bash
export SPARK_HOME="${HOME}/spark/spark-3.5.1-bin-hadoop3"

export PATH="${SPARK_HOME}/bin:${PATH}"
```