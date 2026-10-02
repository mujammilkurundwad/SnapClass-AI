import streamlit as st

LOGO_URL = "https://i.ibb.co/YTYGn5qV/logo.png"


def _header(layout: str, logo_height: int, title_size: str, title_color: str,
            accent: str, subtitle_color: str):
    is_stacked = layout == "stacked"

    st.markdown(
        f"""
        <style>
            .sc-header {{
                display: flex;
                flex-direction: {"column" if is_stacked else "row"};
                align-items: center;
                justify-content: {"center" if is_stacked else "flex-start"};
                gap: {"12px" if is_stacked else "16px"};
                margin: {"2.5rem 0 2rem 0" if is_stacked else "0.5rem 0 1.5rem 0"};
            }}
            .sc-header img {{
                height: {logo_height}px;
                width: auto;
                flex-shrink: 0;
                filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.18));
                transition: transform 0.3s ease;
            }}
            .sc-header img:hover {{
                transform: scale(1.06) rotate(-3deg);
            }}
            .sc-header h1.sc-title {{
                margin: 0 !important;
                padding: 0 !important;
                font-size: {title_size} !important;
                line-height: 1.1 !important;
                letter-spacing: 2px !important;
                white-space: nowrap !important;
                color: {title_color} !important;
                text-align: {"center" if is_stacked else "left"};
            }}
            .sc-header .sc-divider {{
                width: 60px;
                height: 4px;
                border-radius: 999px;
                background: {accent};
                margin: {"8px auto 0 auto" if is_stacked else "8px 0 0 0"};
            }}
            .sc-header p.sc-subtitle {{
                margin: 6px 0 0 0 !important;
                font-size: 0.75rem !important;
                font-weight: 500;
                letter-spacing: 2px;
                text-transform: uppercase;
                white-space: nowrap;
                color: {subtitle_color} !important;
                text-align: {"center" if is_stacked else "left"};
            }}
        </style>

        <div class="sc-header">
            <img src="{LOGO_URL}" alt="SnapClass logo" />
            <div>
                <h1 class="sc-title">SNAP<br/>CLASS</h1>
                <div class="sc-divider"></div>
                <p class="sc-subtitle">Attendance made simple</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header_home():
    _header(
        layout="stacked",
        logo_height=100,
        title_size="2.6rem",
        title_color="#E0E3FF",
        accent="#FFFFFF",
        subtitle_color="rgba(224, 227, 255, 0.85)",
    )


def header_dashboard():
    _header(
        layout="inline",
        logo_height=70,
        title_size="1.8rem",
        title_color="#5865F2",
        accent="#2E3175",
        subtitle_color="#2E3175",
    )