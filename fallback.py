"""
fallback.py - Resilient Groq Call Handler
"""
import os
import streamlit as st
from groq import Groq
from config import GROQ_PRIMARY_MODEL, GROQ_FALLBACK_MODELS

def execute_groq_request(contents_payload):
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if not api_key:
        return "⚠️ Missing GROQ_API_KEY in secrets.toml or environment."

    client = Groq(api_key=api_key)
    models_to_try = [GROQ_PRIMARY_MODEL] + [m for m in GROQ_FALLBACK_MODELS if m != GROQ_PRIMARY_MODEL]
    last_error = ""

    for model in models_to_try:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": contents_payload
                    }
                ]
            )
            if response and response.choices and response.choices[0].message.content:
                return response.choices[0].message.content
        except Exception as e:
            last_error = str(e)
            if any(err in last_error for err in ["429", "503", "rate_limit_exceeded", "service_unavailable"]):
                continue
            else:
                return f"⚠️ API Error ({model}): {last_error}"

    return f"⚠️ Service temporarily unavailable across models. Last Error: {last_error}"