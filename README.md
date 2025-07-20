# Streamlit BigQuery Uploader

A secure Streamlit app for uploading polling data directly to BigQuery, authenticated via Google OAuth.

## Features

- Google OAuth login
- Upload polling data via CSV
- Filter by "ok" flag
- Send data to BigQuery
- Streamlit Cloud compatible

## Setup

1. Create a Google Cloud project with OAuth2 and BigQuery enabled
2. Set up OAuth client (use your Streamlit app URL as redirect URI)
3. Add credentials to Streamlit Cloud secrets

## Secrets (Streamlit Cloud format)

```
[google]
client_id = "YOUR_GOOGLE_CLIENT_ID"
client_secret = "YOUR_GOOGLE_CLIENT_SECRET"

[bigquery]
project_id = "myfirstproject-271018"
dataset = "opinion_model_svk"
table = "elections_2027"
credentials = """{ ... }"""  # Your GCP service account key
```