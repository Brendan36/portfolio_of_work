from idlelib.configdialog import font_sample_text

import streamlit as st
from utils.toast_manager import handle_redirect_toast

def show():
    # 1) Show any toasts from previous navigation…
    handle_redirect_toast()

    # 2) Read the raw ?page=… param and map it to your actual page‑names
    params = st.query_params
    page_key = params.get("page", [""])[0]

    page_map = {
        "about": ("🔍 About", "🏠 Home"),
        "portfolio": ("📂 Portfolio", "🏠 Home"),
        "contact": ("🤳 Contact me", "🏠 Home"),
    }

    # 3) If it matches, set your session_state and rerun exactly once
    if page_key in page_map:
        st.session_state["page"], st.session_state["redirected_from"] = page_map[page_key]
        # clear the param so it doesn’t fire again
        st.experimental_set_query_params()
        st.rerun()

    st.title("| be |")
    st.title("💰 money wise *©*")

    st.subheader("*ethical investing, redefined*")
    st.write("Smart trading and investing built on sustainability, data, and ethical impact.")
    st.write("Discover how to make informed investment decisions that align with your values.")
    st.markdown("---")
    st.image("assets/smart_money.png",width=150, caption="| be | money wise *©*")
    st.write("more coming soon...")

    st.markdown("---")
    # Visual Navigation with Columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🏡 go home", on_click=lambda: st.session_state.update({'page': '🏠 Home'}))
        # st.image("assets/logo_be_chrome_dark.png", width=120)

    with col2:
        st.button("🌍 | be | me", on_click=lambda: st.session_state.update({'page': '🌍 | be | me'}))
        # st.image("assets/logo_smile_blue.png", width=120)

    with col3:
        st.button("🧠 | be | fair", on_click=lambda: st.session_state.update({'page': '🧠 | be | fair'}))
        # st.image("assets/logo_smile_blue.png", width=120)

    # ─── Footer ───
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    footer_html = """
            <p style="text-align:center; color:gray; font-size:0.8em; margin:0;">
              Built with 💡 by | be | © 2025
            </p>
            <p style="text-align:center; color:gray; font-size:0.8em; margin:0;">
             <a href="?page=about"     target="_self" style="color:gray; text-decoration:none;">| about</a> |
             <a href="?page=portfolio" target="_self" style="color:gray; text-decoration:none;">portfolio</a> |
             <a href="?page=contact"   target="_self" style="color:gray; text-decoration:none;">contact</a> | 
            </p>
            """
    col2.markdown(footer_html, unsafe_allow_html=True)