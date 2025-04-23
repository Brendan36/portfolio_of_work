import streamlit as st
from page_views import home, about, portfolio, contact_me, be_labs, be_me, be_fair, be_money_wise, dyk

from utils.toast_manager import handle_redirect_toast

# --- page config
st.set_page_config(
    page_title="| be |",
    layout="wide",
    page_icon="be_labs/assets/small_logo_be_smile_white.png",
)

# 1) Handle any footer‐link clicks via query‐param:
params = st.query_params
if "page" in params:
    page_param = params["page"][0]
    # map the URL slug → your session_state key
    param_to_page = {
        "about":     "🔍 About",
        "portfolio": "📂 Portfolio",
        "contact":   "📧 Contact me",
        "be_labs":   "💡 | be | labs",
        "be_me":     "🌍 | be | me",
        "be_fair":   "🧠 | be | fair",
        "be_money_wise": "💰 | be | money wise",
        "dyk":    "🤯 Did you know?",
    }
    if page_param in param_to_page:
        st.session_state["page"] = param_to_page[page_param]
        st.session_state["redirected_from"] = "🏠 Home"
    # clear so we only handle it once
    st.query_params.clear()

# 2) Show any pending toast from the redirect:
handle_redirect_toast()
# Routing dictionary
nav_pages = {
    "🏠 Home": home.show,
    "🔍 About": about.show,
    "📂 Portfolio": portfolio.show,
    "📧 Contact me": contact_me.show,
    "| be | ©": be_labs.show,


}
# Routing dictionary
pages = {
    "🏠 Home": home.show,
    "🔍 About": about.show,
    "📂 Portfolio": portfolio.show,
    "📧 Contact me": contact_me.show,
    "| be | ©": be_labs.show,
    "🌍 | be | me": be_me.show,
    "🧠 | be | fair": be_fair.show,
    "💰 | be | money wise": be_money_wise.show,
    "🤯 Did you know?": dyk.show,

}

# Handle redirect if set
if "redirect_page" in st.session_state:
    st.session_state["page"] = st.session_state["redirect_page"]
    del st.session_state["redirect_page"]

# Sidebar navigation
with st.sidebar:
    st.image("assets/small_logo_be_smile_white.png", width=50)
    choice = st.sidebar.radio(
        "Go to",
        list(nav_pages.keys()),
        index=list(pages.keys()).index(st.session_state.get("page", "🏠 Home")),
        key="page"
    )

# Run selected page
pages[choice]()  # ✅ This calls the right page module
