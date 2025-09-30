---
id: 9179edaff3
question: 'Google Cloud BigQuery: Location Problems'
sort_order: 66
---

When running a query on BigQuery, you might encounter the error: **"This table is not on the specified location"**.

To resolve this issue, consider the following steps:

- **Check the Locations**: Ensure the locations of your bucket, datasets, and tables are consistent. They should all reside in the same location.

- **Modify Query Settings**:
  1. Go to the query window.
  2. Select **More** -> **Query Settings**.
  3. Select the correct location.

- **Verify Table Paths**: Double-check the paths in your query:
  1. Click on the table.
  2. Go to **Details**.
  3. Copy the correct path.