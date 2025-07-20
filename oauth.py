import streamlit as st
import requests

def get_user_email():
    if "user_email" in st.session_state:
        return st.session_state["user_email"]

    client_id = st.secrets["google"]["client_id"]
    client_secret = st.secrets["google"]["client_secret"]
    redirect_uri = st.secrets.get("google", {}).get("redirect_uri", st.request.url)

    code = st.experimental_get_query_params().get("code", [None])[0]

    if not code:
        auth_url = (
            "https://accounts.google.com/o/oauth2/v2/auth"
            f"?client_id={client_id}"
            f"&redirect_uri={redirect_uri}"
            "&response_type=code"
            "&scope=openid%20email%20profile"
            f"&state=secure_state"
        )
        st.markdown(f"[Click here to authenticate with Google]({auth_url})")
        return None

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    response = requests.post(token_url, data=token_data)
    if response.status_code != 200:
        st.error("Failed to authenticate.")
        return None

    id_token = response.json().get("id_token", "")
    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {response.json()['access_token']}"}
    ).json()

    email = user_info.get("email", "")
    if email:
        st.session_state["user_email"] = email
        return email

    return None