import streamlit as st
from datetime import date
from bigquery_utils import upload_to_bigquery
from validator import validate_input

st.set_page_config(page_title="Polling Data Uploader v1.1", layout="centered")

st.title("🗳️ Polling Data Uploader v1.1")

with st.form("poll_form"):
    st.subheader("General Info")
    agency = st.text_input("Agency")
    paid_by = st.text_input("Paid by")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", value=date.today())
    with col2:
        end_date = st.date_input("End Date", value=date.today())

    st.subheader("Segments")
    segments = {
        "sample": "1004",
        "smer–ssd": "19.8%",
        "participation": "0.689%",
        "ps": "24.1%",
        "hlas-sd": "12.5%",
        "rep": "5.7%",
        "kdh": "6.9%",
        "sas": "6.4%",
        "d": "4.6%",
        "as": "3.1%",
        "kú+sk+zľ": "6.0%",
        "sns": "4.1%",
        "sr": "2.9%",
    }

    segment_inputs = {}
    for segment, default in segments.items():
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            seg_name = st.text_input(f"Segment", value=segment, key=f"seg_{segment}")
        with col2:
            seg_value = st.text_input(f"Value", value=default, key=f"val_{segment}")
        with col3:
            seg_flag = st.checkbox("Include", value=True, key=f"flag_{segment}")
        segment_inputs[seg_name] = {"value": seg_value, "flag": seg_flag}

    submitted = st.form_submit_button("Upload")

if submitted:
    st.subheader("🔍 Validation Results")
    validated_data, errors = validate_input(agency, paid_by, start_date, end_date, segment_inputs)
    if errors:
        st.error("Fix the following errors before uploading:")
        for error in errors:
            st.write(f"- {error}")
    else:
        st.success("Validation passed. Uploading data...")
        upload_to_bigquery([validated_data])
        st.success("✅ Data uploaded successfully!")
