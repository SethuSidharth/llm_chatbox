from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

def get_table_schema(dataset_name, table_name):
    table = client.get_table(f"{client.project}.{dataset_name}.{table_name}")
    schema_info = ", ".join([f"{field.name} ({field.field_type})" for field in table.schema])
    return schema_info

def execute_query(sql_query):
    try:
        query_job = client.query(sql_query)  # Make an API request.
        results = query_job.result()  # Wait for the job to complete.
        rows = [dict(row) for row in results]
        return rows
    except Exception as e:
        return {"error": str(e)}
