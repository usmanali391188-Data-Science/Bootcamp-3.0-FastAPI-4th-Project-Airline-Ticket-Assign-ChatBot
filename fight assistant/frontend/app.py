import streamlit as st
import requests
import uuid
import re

st.set_page_config(page_title="Flight Assistant Chatbot", page_icon="✈️", layout="centered")
st.title("✈️ Flight Ticket Assistant AI")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []

backend_url = "http://127.0.0.1:8000"

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    res = requests.post(f"{backend_url}/chat", json={
        "session_id": st.session_state.session_id,
        "message": user_input
    })

    if res.status_code == 200:
        bot_reply = res.json().get("response", "")
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    else:
        st.session_state.messages.append({"role": "assistant", "content": f"❌ Error: {res.text}"})



for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

if any("form" in msg["content"].lower() or "fill" in msg["content"].lower() for msg in st.session_state.messages):
    st.markdown("### 📝 Flight Booking Form")

    with st.form("lead_form"):
        name = st.text_input("Your Name ")
        email = st.text_input("Email ")
        from_city = st.selectbox("From City ", ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Quetta"])
        to_city = st.selectbox("To City ", ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Quetta"])
        comment = st.text_area("Comment ")

        submit = st.form_submit_button("Submit Booking")

        if submit:
            if not name or not email:
                st.error("⚠️ Please fill in all required fields.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.warning("📧 Please enter a valid email address (e.g., name@example.com)")
            else:
                payload = {
                    "name": name,
                    "email": email,
                    "from_city": from_city,
                    "to_city": to_city,
                    "comment": comment
                }
                res = requests.post(f"{backend_url}/lead", json=payload)
                if res.status_code == 200:
                    st.success(" Your flight booking form was submitted successfully!")
                else:
                    st.error(f" Error: {res.text}")
