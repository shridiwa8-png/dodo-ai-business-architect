"""
fallback.py - Resilient Gemini Call Handler
"""
import os
import streamlit as st
from google import genai
from config import GEMINI_PRIMARY_MODEL, GEMINI_FALLBACK_MODELS

def execute_gemini_request(contents_payload):
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ Missing GEMINI_API_KEY in secrets.toml or environment."

    client = genai.Client(api_key=api_key)
    models_to_try = [GEMINI_PRIMARY_MODEL] + [m for m in GEMINI_FALLBACK_MODELS if m != GEMINI_PRIMARY_MODEL]
    last_error = ""

    for model in models_to_try:
        try:
            response = client.models.generate_content(
                model=model,
                contents=contents_payload
            )
            if response and response.text:
                return response.text
        except Exception as e:
            last_error = str(e)
            if any(err in last_error for err in ["429", "503", "RESOURCE_EXHAUSTED", "UNAVAILABLE"]):
                continue
            else:
                return f"⚠️ API Error ({model}): {last_error}"

    return f"⚠️ Service temporarily unavailable across models. Last Error: {last_error}"