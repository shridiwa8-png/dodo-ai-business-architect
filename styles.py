import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#09090b;
        color:white;
    }

    h1,h2,h3{
        color:white;
    }

    textarea{
        border-radius:14px !important;
    }

    .stButton>button{

        width:100%;
        border-radius:12px;
        height:52px;

        background:#ffffff;
        color:#000000;

        font-weight:700;
        border:none;

    }

    .stButton>button:hover{

        background:#dddddd;

    }

    </style>
    """, unsafe_allow_html=True)
