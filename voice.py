import os
import tempfile
import streamlit as st
from groq import Groq

def record_voice():
    """
    Record voice and transcribe it using Groq (Whisper).
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
        st.secrets.get("GROQ_API_KEY")
        or os.getenv("GROQ_API_KEY")
    )

    if not api_key:
        st.error("Missing GROQ_API_KEY")
        return ""

    try:
        client = Groq(api_key=api_key)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio.getbuffer())
            audio_path = tmp.name

        with open(audio_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(audio_path, file.read()),
                model="whisper-large-v3",
                prompt="Transcribe this audio exactly. Do not summarize.",
                response_format="json"
            )

        os.remove(audio_path)

        transcript = transcription.text.strip()

        st.success("✅ Voice transcribed successfully!")

        st.text_area(
            "Transcript",
            transcript,
            height=150
        )

        return transcript

    except Exception as e:
        return f"Voice transcription failed: {e}"