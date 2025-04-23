import streamlit as st
from utils.toast_manager import handle_redirect_toast
from page_views import (
    home, about, portfolio, contact_me,
    be_labs, be_me, be_fair, be_money_wise, dyk
)
def show():
    handle_redirect_toast()
    st.title("| be |")
    st.title("🧠 fair *©*")
    st.subheader("*because truth matters*")
    st.write("A browser assistant to detect bias, truth probability, and media sentiment in real-time.")
    st.write("Discover how to make informed decisions based on data-driven insights.")
    st.markdown("---")
    st.image("assets/fairy.png", width=150, caption="| be | fair *©*")
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
        st.button("💰 | be | money wise", on_click=lambda: st.session_state.update({'page': '💰 | be | money wise'}))
        # st.image("assets/logo_be_your_best_bold.png", width=120)



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