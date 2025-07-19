import streamlit as st


def handle_redirect_toast():
    toast_map = {
        "🏠 Home": "🏡 Back to Home!",
        "🔍 About": "ℹ️ About page loaded",
        "📂 Portfolio": "💼 Welcome to my portfolio!",
        "📧 Contact me": "🤳 I'll get back to you as soon as I can!",
        "| be | labs💡 ": "🔍 Exploring be labs tools in production",
        "🌍 | be | me": "🌱 Exploring sustainability with | be | me",
        "🧠 | be | fair": "💡 Analyzing truth with | be | fair",
        "💰 | be | money wise": "📊 Ethical investing with | be | money wise"
    }

    redirected_from = st.session_state.get("redirected_from")

    if redirected_from:
        message = toast_map.get(st.session_state.get("page"), "🚀 Page loaded")
        if hasattr(st, "toast"):  # Streamlit 1.27+
            st.toast(message)
        else:
            st.success(message)

        # Clean up after showing it once
        del st.session_state["redirected_from"]