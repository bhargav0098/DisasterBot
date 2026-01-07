import streamlit as st
import os
from google import genai
from google.genai.errors import ClientError

# ---------- CONFIG ----------
MODEL_NAME = "gemini-flash-latest"
API_KEY = os.environ.get("GOOGLE_API_KEY") or "YOUR_API_KEY_HERE"

client = genai.Client(api_key=API_KEY)

# ---------- SYSTEM PROMPT ----------
system_prompt = """
You are Disaster Response & Relief Explainer Bot.

Your job is ONLY to explain:
- disaster response workflows
- relief distribution processes
- evacuation guidelines
- preparedness and safety awareness

Rules:
- Be polite, calm, and summarized (2–6 sentences only).
- Explain processes — do NOT coordinate rescues.
- No alerts, no predictions, no live instructions.
- Do not give phone numbers unless the user already provides one.
- If unsure, say: “Please refer to official government guidance.”

If the question is unrelated to disasters, say:
“Sorry — I’m only designed to explain disaster response and relief processes.”
"""

# ---------- UI ----------
st.set_page_config(page_title="Disaster Response Explainer Bot", page_icon="🛟")

st.markdown(
    """
    ## 🛡️ Disaster Response & Relief Explainer Bot  
    **Learn how disaster systems work — calmly, clearly, responsibly.**  
    _(No alerts, no predictions, only awareness & guidance.)_
    """
)

prompt = st.text_area(
    "Ask your question",
    placeholder="Example: How is relief distributed during floods?",
    height=140
)

if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=[system_prompt, prompt]
            )

            st.success("Response:")
            st.write(response.text)

        except ClientError as e:
            if e.status_code == 429:
                st.error("Quota exhausted. Please wait and try again.")
            else:
                st.error(f"API Error: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")