import streamlit as st
import requests

st.set_page_config(
    page_title="Fraud Intelligence Dashboard"
)

st.title(
    "🏦 Fraud Intelligence Dashboard"
)

amount = st.number_input(
    "Amount",
    value=100.0
)

time = st.number_input(
    "Time",
    value=10.0
)

if st.button(
    "Predict Fraud"
):

    payload = {
        "Time": time,
        "Amount": amount
    }

    try:

        response = requests.post(
            "http://localhost:8000/predict",
            json={
                "data": payload
            },
            timeout=5
        )

        st.json(
            response.json()
        )

    except Exception:

        st.error(
            "FastAPI server is not running."
        )