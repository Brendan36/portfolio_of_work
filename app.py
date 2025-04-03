import streamlit as st
from page_views import home, be_me, be_fair, be_money_wise, portfolio

# Page config
st.set_page_config(
    page_title="| be |",
    layout="wide",
    page_icon="be_labs/assets/logo_be_chrome_dark.png"
)

# Sidebar navigation
st.sidebar.title("🧭 | be | Navigation")
choice = st.sidebar.radio("Go to", [
    "🏠 Home",
    "📂 Portfolio",
    "🌍 | be | me",
    "🧠 | be | fair",
    "💰 | be | money wise"
])

# Routing dictionary
pages = {
    "🏠 Home": home.show,
    "📂 Portfolio": portfolio.show,
    "🌍 | be | me": be_me.show,
    "🧠 | be | fair": be_fair.show,
    "💰 | be | money wise": be_money_wise.show,
}

# Run selected page
pages[choice]()  # ✅ This calls the right page module
