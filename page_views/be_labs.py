import streamlit as st
from streamlit import caption
from page_views import (
    home, about, portfolio, contact_me
)


def show():
    from utils.toast_manager import handle_redirect_toast
    # 1) Show any toasts from previous navigation…
    handle_redirect_toast()
    params = st.query_params
    if params.get("page", [""])[0] == "about":
        st.session_state["redirect_page"] = "🔍 About"
        st.session_state["redirected_from"] = "🏠 Home"
        st.experimental_set_query_params()
        st.rerun()

    if params.get("page", [""])[0] == "portfolio":
        st.session_state["redirect_page"] = "📂 Portfolio"
        st.session_state["redirected_from"] = "🏠 Home"
        st.experimental_set_query_params()
        st.rerun()

    if params.get("page", [""])[0] == "contact":
        st.session_state["redirect_page"] = "📧 Contact me"
        st.session_state["redirected_from"] = "🏠 Home"
        st.experimental_set_query_params()
        st.rerun()

    page_key = params.get("page", [""])[0]
    page_map = {
        "about": ("🔍 About", "🏠 Home"),
        "portfolio": ("📂 Portfolio", "🏠 Home"),
        "contact": ("📧 Contact me", "🏠 Home"),
    }
    if page_key in page_map:
        st.session_state["page"], st.session_state["redirected_from"] = page_map[page_key]
        st.experimental_set_query_params()  # clear it
        st.rerun()

    # Logo Header
    col1, col2, col3 = st.columns(3, vertical_alignment="center")

    with col1:
        # Wellcome Section
        st.markdown("## Welcome to | be |")
        st.image("images/logo_be_smile_white.png", width=150)

    with col2:
        st.image("images/logo_be_chrome_dark.png", width=300)


    st.markdown("""
        *Rooted in truth. Designed for transparency.*\n
        A platform suite built to inspire and enable clarity, fairness, and action.  

        *Explore* | be | *think-tank💡 (tools in production)*
        """)

    # Visual Navigation with Columns
    col1, col2, col3 = st.columns(3, vertical_alignment="center")

    with col1:
        st.image("images/logo_be_fair_playful.png", width=120)
        st.markdown("#### 🌍 | be | me")
        st.write("*... empowered & authentic*")
        st.write("Uncover truth. Ignite change.")

    with col2:
        st.image("images/logo_smile_blue.png", width=120)
        st.markdown("#### 🧠 | be | fair")
        st.write("*... because kindness matters*")
        st.write("Filter noise. Decode bias.")

    with col3:
        st.image("images/logo_be_your_best_bold.png", width=120)
        st.markdown("#### 💰 | be | money wise")
        st.write("*... ethical investing, redefined*")
        st.write("Invest ethically. Invest with purpose.")

    # st.markdown("---")

    # Visual Navigation with Columns
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌍 | be | me"):
            st.info("Coming soon... something amazing is being built!")
    with col2:
        if st.button("🧠 | be | fair"):
            st.info("Coming soon... something amazing is being built!")
    with col3:
        if st.button("💰 | be | money wise"):
            st.info("Coming soon... something amazing is being built!")
    st.markdown("---")

    # Portfolio callout
    st.markdown("### 🧰 Want to see my builds?")
    st.write("Check out my Streamlit apps, Python projects, and more.")
    if st.button("Go to Portfolio "):
        st.session_state["redirect_page"] = "📂 Portfolio"
        st.session_state["redirected_from"] = "🏠 Home"
        st.rerun()


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