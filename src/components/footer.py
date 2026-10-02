import streamlit as st


def _footer(text_color: str, pill_bg: str, pill_border: str, accent: str):
    st.markdown(
        f"""
        <style>
            .sc-footer {{
                margin-top: 3rem;
                padding: 1rem 0 1.5rem 0;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .sc-footer-pill {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 8px 20px;
                border-radius: 999px;
                background: {pill_bg};
                border: 1px solid {pill_border};
                backdrop-filter: blur(6px);
                color: {text_color};
                font-size: 0.9rem;
                font-weight: 500;
                letter-spacing: 0.3px;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }}
            .sc-footer-pill:hover {{
                transform: translateY(-2px);
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
            }}
            .sc-footer-pill .heart {{
                display: inline-block;
                animation: sc-beat 1.4s infinite;
            }}
            .sc-footer-pill .name {{
                font-weight: 700;
                color: {accent};
            }}
            .sc-footer-pill img {{
                height: 18px;
                width: auto;
            }}
            @keyframes sc-beat {{
                0%, 100% {{ transform: scale(1); }}
                50%      {{ transform: scale(1.25); }}
            }}
        </style>

        <div class="sc-footer">
            <div class="sc-footer-pill">
                <span>Created with</span>
                <span class="heart">❤️</span>
                <span>by</span>
                <span class="name">Mk_07</span>
                <!-- <span>×</span><img src="YOUR_APNACOLLEGE_LOGO_URL" alt="ApnaCollege"> -->
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_home():
    # Home background is #5865f2 -> light glass pill with white text
    _footer(
        text_color="#ffffff",
        pill_bg="rgba(255, 255, 255, 0.15)",
        pill_border="rgba(255, 255, 255, 0.35)",
        accent="#ffffff",
    )


def footer_dashboard():
    # Dashboard background is #e0e3ff -> navy text on a soft white pill
    _footer(
        text_color="#2E3175",
        pill_bg="rgba(255, 255, 255, 0.7)",
        pill_border="rgba(46, 49, 117, 0.2)",
        accent="#5865f2",
    )