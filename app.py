import streamlit as st
from page_views import home, about, portfolio, contact_me, be_labs

from utils.toast_manager import handle_redirect_toast

NEW_URL = "https://brendan36.github.io/brendan_elario_portfolio/"

# --- page config
st.set_page_config(
    page_title="Portfolio Moved",
    layout="wide",
    page_icon="portfolio_of_work/images/small_logo_be_smile_white.png",
)

st.title("Portfolio Updated")

st.write(
    "My portfolio has moved to a faster GitHub Pages site."
)

st.markdown(
    f"""
    ### Redirecting...

    If you are not redirected automatically, click below:

    [Open Portfolio]({NEW_URL})
    """
)

st.markdown(
    f"""
    <meta http-equiv="refresh" content="3; url={NEW_URL}">
    """,
    unsafe_allow_html=True
)