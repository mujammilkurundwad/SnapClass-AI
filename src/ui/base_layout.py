import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background: #5865F2 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background: #E0E3FF !important;
            }

            /* Readable text on the light background (content only, not buttons) */
            .stApp h2, .stApp h3, .stApp h4,
            .stApp label,
            .stApp [data-testid="stWidgetLabel"] p,
            .stApp [data-testid="stMarkdownContainer"] p {
                color: #2E3175;
            }

            /* Light inputs instead of dark */
            .stApp div[data-baseweb="input"],
            .stApp div[data-baseweb="base-input"],
            .stApp .stTextInput input {
                background-color: #FFFFFF !important;
                color: #2E3175 !important;
                border-radius: 1rem !important;
            }
            .stApp div[data-baseweb="input"] {
                border: 1px solid rgba(46, 49, 117, 0.25) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            /* Hide Streamlit's default top bar and footer */
            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            /* Typography */
            html, body, .stApp, p, h3, h4, label, button {
                font-family: 'Outfit', sans-serif;
            }

            /* :not(.sc-title) keeps these rules off the SnapClass header title,
               which sets its own size and color in header.py */
            h1:not(.sc-title) {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h1.sc-title {
                font-family: 'Climate Crisis', sans-serif !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 1.6rem !important;
                line-height: 1.15 !important;
                letter-spacing: 1px !important;
                margin-bottom: 0rem !important;
            }

            /* Shared button shape (only Streamlit buttons, not icons inside inputs) */
            div.stButton > button {
                border-radius: 1.5rem !important;
                padding: 10px 20px !important;
                border: none !important;
                font-weight: 600 !important;
                transition: transform 0.25s ease-in-out,
                            background-color 0.25s ease-in-out,
                            box-shadow 0.25s ease-in-out !important;
            }
            div.stButton > button:hover {
                transform: scale(1.05);
            }

            /* Primary: navy */
            div.stButton > button[kind="primary"],
            div.stButton > button[data-testid="stBaseButton-primary"] {
                background-color: #2E3175 !important;
                color: #FFFFFF !important;
            }
            div.stButton > button[kind="primary"]:hover,
            div.stButton > button[data-testid="stBaseButton-primary"]:hover {
                background-color: #1E2155 !important;
                box-shadow: 0 6px 16px rgba(46, 49, 117, 0.35) !important;
            }

            /* Secondary: outlined navy (e.g. "Go back to Home") */
            div.stButton > button[kind="secondary"],
            div.stButton > button[data-testid="stBaseButton-secondary"] {
                background-color: #FFFFFF !important;
                color: #2E3175 !important;
                border: 2px solid #2E3175 !important;
            }
            div.stButton > button[kind="secondary"]:hover,
            div.stButton > button[data-testid="stBaseButton-secondary"]:hover {
                background-color: #E0E3FF !important;
            }

            /* Tertiary: black */
            div.stButton > button[kind="tertiary"],
            div.stButton > button[data-testid="stBaseButton-tertiary"] {
                background-color: #000000 !important;
                color: #FFFFFF !important;
            }

            /* Button labels: keep text and icons the button's own color.
               Without this, the dashboard's navy <p> color leaks into them. */
            button[data-testid="stBaseButton-primary"] p,
            button[data-testid="stBaseButton-primary"] span,
            button[data-testid="stBaseButton-primary"] svg,
            button[data-testid="stBaseButton-tertiary"] p,
            button[data-testid="stBaseButton-tertiary"] span,
            button[data-testid="stBaseButton-tertiary"] svg,
            button[kind="primary"] p,
            button[kind="primary"] span,
            button[kind="tertiary"] p,
            button[kind="tertiary"] span {
                color: #FFFFFF !important;
                fill: #FFFFFF !important;
            }

            button[data-testid="stBaseButton-secondary"] p,
            button[data-testid="stBaseButton-secondary"] span,
            button[data-testid="stBaseButton-secondary"] svg,
            button[kind="secondary"] p,
            button[kind="secondary"] span {
                color: #2E3175 !important;
                fill: #2E3175 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )