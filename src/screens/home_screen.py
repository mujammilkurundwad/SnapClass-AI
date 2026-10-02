import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def _style_home_cards():
    card_bg = "#FFFFFF"                      # container color
    card_border = "rgba(46, 49, 117, 0.12)"
    title_color = "#1E2155"                  # card title text
    desc_color = "#4752C4"                   # card description text

    st.markdown(
        f"""
        <style>
            /* Card container (only the keyed cards, not every block) */
            div[class*="st-key-card_"] {{
                background: {card_bg};
                border: 1px solid {card_border};
                border-radius: 24px;
                padding: 1.5rem 1rem 1.75rem 1rem;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
                transition: transform 0.25s ease, box-shadow 0.25s ease;
            }}
            div[class*="st-key-card_"]:hover {{
                transform: translateY(-6px);
                box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25);
            }}

            /* Center content inside the cards */
            div[class*="st-key-card_"] div[data-testid="stImage"] {{
                display: flex;
                justify-content: center;
                margin: 0.5rem 0 1rem 0;
            }}
            div[class*="st-key-card_"] div[data-testid="stImage"] img {{
                filter: drop-shadow(0 8px 14px rgba(0, 0, 0, 0.22));
                transition: transform 0.3s ease;
            }}
            div[class*="st-key-card_"]:hover div[data-testid="stImage"] img {{
                transform: scale(1.06);
            }}
            div[class*="st-key-card_"] div.stButton {{
                display: flex;
                justify-content: center;
            }}

            /* Card text */
            .sc-card-title {{
                text-align: center;
                color: {title_color};
                font-size: 1.7rem;
                font-weight: 800;
                margin: 0;
            }}
            .sc-card-desc {{
                text-align: center;
                color: {desc_color};
                font-size: 0.9rem;
                font-weight: 500;
                margin: 4px 0 0 0;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def _portal_card(title, desc, image_url, image_width, button_label, login_type):
    # key="card_..." is what the CSS above targets
    with st.container(border=True, key=f"card_{login_type}"):
        st.markdown(
            f"""
            <p class="sc-card-title">{title}</p>
            <p class="sc-card-desc">{desc}</p>
            """,
            unsafe_allow_html=True,
        )
        st.image(image_url, width=image_width)
        if st.button(
            button_label,
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
            key=f"btn_{login_type}",
        ):
            st.session_state["login_type"] = login_type
            st.rerun()


def home_screen():
    header_home()
    style_background_home()
    style_base_layout()
    _style_home_cards()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        _portal_card(
            title="I'm Student",
            desc="View your classes and attendance",
            image_url="https://i.ibb.co/844D9Lrt/mascot-student.png",
            image_width=120,
            button_label="Student Portal",
            login_type="student",
        )

    with col2:
        _portal_card(
            title="I'm Teacher",
            desc="Manage classes and take attendance",
            image_url="https://i.ibb.co/CsmQQV6X/mascot-prof.png",
            image_width=145,
            button_label="Teacher Portal",
            login_type="teacher",
        )

    footer_home()