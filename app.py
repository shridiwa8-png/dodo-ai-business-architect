import streamlit as st

from dodo_engine import generate_recovery_plan
from ui import hero, user_profile, user_input_box
from uploads import upload_file
from voice import record_voice


# =========================
# DODO VERSION
# =========================

DODO_VERSION = "1.0.0"


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="DoDo",
    page_icon="🦤",
    layout="wide"
)


# =========================
# SESSION STORAGE
# =========================

if "blueprint" not in st.session_state:
    st.session_state.blueprint = None


# =========================
# HEADER
# =========================

hero()

st.caption(
    f"🦤 DoDo v{DODO_VERSION} | Business Execution Architect"
)


# =========================
# USER PROFILE
# =========================

profile = user_profile()


st.divider()


# =========================
# BUSINESS INPUT
# =========================

user_input = user_input_box()


st.divider()


# =========================
# FILE UPLOADS
# =========================

uploaded_files = upload_file()


st.divider()


# =========================
# VOICE INPUT
# =========================

voice_text = record_voice()


if voice_text:
    user_input += (
        "\n\nVoice Notes:\n"
        + voice_text
    )


# =========================
# BUILD BUTTON
# =========================

build = st.button(
    "⚡ Build My Execution System",
    type="primary",
    use_container_width=True
)


if build:
    if not user_input.strip():
        st.warning(
            "Please describe your business problem first."
        )
    else:
        with st.spinner(
            "🧠 DoDo is analyzing your business system..."
        ):
            try:
                result = generate_recovery_plan(
                    user_input=user_input,
                    profile=profile,
                    uploaded_files=uploaded_files
                )
                st.session_state.blueprint = result
            except Exception as e:
                st.error(
                    f"DoDo failed: {e}"
                )


# =========================
# DISPLAY RESULT
# =========================

if st.session_state.blueprint:

    st.divider()

    st.markdown(
        "# 📋 Execution Blueprint"
    )

    result = st.session_state.blueprint

    # =====================
    # QUICK STATUS CARD
    # =====================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Blueprint Status",
            "Generated"
        )

    with col2:
        st.metric(
            "AI Consultant",
            "DoDo"
        )

    with col3:
        st.metric(
            "Output Format",
            "Execution System"
        )

    st.divider()

    # =====================
    # BLUEPRINT OUTPUT
    # =====================

    st.markdown(result)

    st.divider()

    # =====================
    # DOWNLOAD
    # =====================

    st.download_button(
        label="⬇️ Download Blueprint",
        data=result,
        file_name="dodo_execution_blueprint.txt",
        mime="text/plain"
    )

    # =====================
    # CLEAR BUTTON
    # =====================

    if st.button(
        "🧹 Clear Blueprint"
    ):
        st.session_state.blueprint = None
        st.rerun()

    st.success(
        "System generated successfully."
    )