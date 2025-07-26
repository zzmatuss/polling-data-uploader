from google.cloud import bigquery
import streamlit as st
import json

def upload_to_bigquery(rows):
    credentials_dict = json.loads(st.secrets["bigquery"]["credentials"])
    client = bigquery.Client.from_service_account_info(credentials_dict)

    table_id = f"{st.secrets['bigquery']['project_id']}.{st.secrets['bigquery']['dataset']}.{st.secrets['bigquery']['table']}"

    errors = client.insert_rows_json(table_id, rows)

    if errors:
        return False, f"Errors while inserting rows: {errors}"
    else:
        return True, f"Inserted {len(rows)} row(s) into {table_id}"
