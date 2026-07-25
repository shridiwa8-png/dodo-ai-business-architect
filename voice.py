import os
import tempfile
import streamlit as st
from google import genai

def record_voice():
    """
    Record voice and transcribe it using Gemini.
    Returns the transcript as a string.
    """

    st.markdown("## 🎙️ Voice Input (Optional)")

    audio = st.audio_input(
        "Record your voice",
        label_visibility="collapsed"
    )

    if audio is None:
        return ""

    api_key = (
        st.secrets.get("GEMINI_API_KEY")
        or os.getenv("GEMINI_API_KEY")
    )

    if not api_key:
        st.error("Missing GEMINI_API_KEY")
        return ""

    try:
        client = genai.Client(api_key=api_key)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio.getbuffer())
            audio_path = tmp.name

        uploaded_audio = client.files.upload(
            file=audio_path
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                uploaded_audio,
                "Transcribe this audio exactly. Do not summarize."
            ]
        )

        os.remove(audio_path)

        transcript = response.text.strip()

        st.success("✅ Voice transcribed successfully!")

        st.text_area(
            "Transcript",
            transcript,
            height=150
        )

        return transcript

    except Exception as e:
        return f"Voice transcription failed: {e}"