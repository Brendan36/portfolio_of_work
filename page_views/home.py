import streamlit as st
from streamlit import caption

from utils.toast_manager import handle_redirect_toast


def show():
    handle_redirect_toast()
    params = st.query_params
    if params.get("page", [""])[0] == "contact":
        st.session_state["redirect_page"] = "📧 Contact me"
        st.session_state["redirected_from"] = "🏠 Home"
        # clear it so we only fire once
        st.experimental_set_query_params()
        st.rerun()

    # Logo Header
    st.image("images/logo_smile_silver.png", width=300)

    # Wellcome Section
    st.markdown("## 🌱 Welcome")

    st.markdown("---")
    col1, col2 = st.columns(2)
    # About callout
    with col1:
        st.markdown("### 🔍 Find out about me?")
        st.write("Check my bio and learn more about my work aspirations.")

        if st.button("Go to About "):
            st.session_state["redirect_page"] = "🔍 About"
            st.session_state["redirected_from"] = "🏠 Home"
            st.rerun()

    with col2:
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