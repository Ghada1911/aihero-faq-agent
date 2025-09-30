---
id: 45bd267149
question: 'Parquet: “Parquet column ''ehail_fee'' has type DOUBLE which does not match
  the target cpp_type INT64”'
sort_order: 13
---

Reason: Parquet files have their own schema. Some Parquet files for green data have records with decimals in the `ehail_fee` column.

There are some possible fixes:

1. **Drop `ehail_fee` column**
   
   Drop the `ehail_fee` column, as it is not used. For instance, when creating a partitioned table from the external table in BigQuery:
   
   ```sql
   SELECT * EXCEPT (ehail_fee) FROM...
   ```

2. **Modify SQL model**
   
   Modify `stg_green_tripdata.sql` model with this line:
   
   ```sql
   CAST(0 AS NUMERIC) AS ehail_fee
   ```

3. **Modify Airflow DAG**
   
   Modify the Airflow DAG to make the conversion and avoid the error:
   
   ```python
   pv.read_csv(src_file, convert_options=pv.ConvertOptions(column_types={'ehail_fee': 'float64'}))
   ```

4. **Using Pandas**
   
   Fix using Pandas when importing the file from CSV into a DataFrame:

   ```python
   pd.from_csv(..., dtype=type_dict)
   ```
   
   Note: Regular `int64` in Pandas (from the numpy library) does not accept null values (NaN). Use Pandas `Int64` instead. The `type_dict` is a Python dictionary mapping column names to dtypes.

Sources:

- [Pandas read_csv Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Nullable integer data type — pandas 1.5.3 documentation](https://pandas.pydata.org/docs/user_guide/integer_na.html)