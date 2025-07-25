import streamlit as st
from oauth import get_user_email
from bigquery_utils import upload_to_bigquery
import pandas as pd

st.set_page_config(page_title="Polling Data Uploader", layout="centered")

# OAuth authentication
email = get_user_email()
if not email:
    st.stop()

st.success(f"Authenticated as {email}")

st.header("Polling Data Uploader")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    df_ok = df[df["flag"].str.lower() == "ok"]
    if not df_ok.empty and st.button("Upload OK-marked rows to BigQuery"):
        success, message = upload_to_bigquery(df_ok.to_dict(orient="records"))
        if success:
            st.success(message)
        else:
            st.error(f"Upload failed: {message}")