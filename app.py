import streamlit as st
from nlp_model import generate_sql_query
from bigquery_client import execute_query, get_table_schema

st.title("AI Chatbot with BigQuery Integration")

# Example schema information retrieval
schema_info = get_table_schema("my_dataset_1", "country_wise_covid")

# Input from user
user_input = st.text_input("Ask a question about your data:")

if st.button("Submit"):
    if user_input:
        # Generate SQL query from user input and schema information
        sql_query = generate_sql_query(user_input, schema_info)
        
        st.text("Generated SQL Query:")
        st.code(sql_query)
        
        # Execute the SQL query on BigQuery
        results = execute_query(sql_query)
        
        st.text("Query Results:")
        if "error" in results:
            st.error(results["error"])
        else:
            st.write(results)
    else:
        st.warning("Please enter a question.")
