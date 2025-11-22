import google.generativeai as genai
import streamlit as st

# 🔑 Your Gemini API key here
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

# ✅ Gemini model init
model = genai.GenerativeModel("models/gemini-1.5-flash")


def summarize_text(text):
    prompt = f"Summarize this research paper clearly and concisely:\n\n{text}"

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API Error: {str(e)}"
