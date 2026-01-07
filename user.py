import streamlit as st
import os
from google import genai
from google.genai.errors import ClientError

# ---------- CONFIG ----------
MODEL_NAME = "gemini-flash-latest"
API_KEY = os.environ.get("GOOGLE_API_KEY") or "AIzaSyC0ueP_aIuPucZGfITgLKwT-n1VdnBxcU0"

# ---------- CLIENT ----------
client = genai.Client(api_key=API_KEY)

st.title("Gemini Pro Chatbot (Quota Safe)")

prompt = st.text_area(
    "Ask your question",
    placeholder="Explain AI in simple words",
    height=120
)

if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt")
    else:
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )
            st.success("Response:")
            st.write(response.text)

        except ClientError as e:
            if e.status_code == 429:
                st.error(
                    "❌ Quota exhausted (429).\n\n"
                    "Free tier limit reached.\n"
                    "Please wait some time or try again later."
                )
            else:
                st.error(f"API Error: {e}")

        except Exception as e:
            st.error(f"Unexpected error: {e}")
