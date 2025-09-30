---
id: b3bb998ae2
question: How to connect Pyspark with BigQuery?
sort_order: 13
---

To connect Pyspark with BigQuery, include the following line in the Pyspark configuration:

```python
# Example initialization of SparkSession variable

spark = (SparkSession.builder

    .master("...")
    .appName("...")
    
    # Add the following configuration
    .config("spark.jars.packages", "com.google.cloud.spark:spark-3.5-bigquery:0.37.0")
)
```