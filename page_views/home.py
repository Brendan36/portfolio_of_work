import streamlit as st


def show():
    # Logo Header
    st.image("assets/logo_be_chrome_dark.png", width=300)
    st.markdown("<h2 style='color:#D3D3D3;'>| be | your best</h2>", unsafe_allow_html=True)

    st.markdown("---")

    # Welcome Section
    st.markdown("### 🌱 Welcome to the be_labs ecosystem")
    st.markdown("""
    A platform suite built to inspire clarity, fairness, and action.  
    Rooted in truth. Designed for transparency. Powered by you.

    **Explore the tools:**
    """)

    # Visual Navigation with Columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/logo_smile_blue.png", width=120)
        st.markdown("#### 🌍 | be | me")
        st.write("Uncover truth. Ignite change.")
        st.button("Go to | be | me", on_click=lambda: st.session_state.update({'page': '🌍 | be | me'}))

    with col2:
        st.image("assets/logo_be_fair_playful.png", width=120)
        st.markdown("#### 🧠 | be | fair")
        st.write("Decode bias. Filter noise.")
        st.button("Go to | be | fair", on_click=lambda: st.session_state.update({'page': '🧠 | be | fair'}))

    with col3:
        st.image("assets/logo_be_your_best_bold.png", width=120)
        st.markdown("#### 💰 | be | money wise")
        st.write("Invest with purpose.")
        st.button("Go to | be | money wise", on_click=lambda: st.session_state.update({'page': '💰 | be | money wise'}))

    st.markdown("---")

    # Portfolio callout
    st.markdown("### 🧰 Want to see my builds?")
    st.write("Check out Streamlit apps, Python projects, and more.")
    st.button("Go to Portfolio", on_click=lambda: st.session_state.update({'page': '📂 Portfolio'}))

    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align:center;color:gray;'>Built with 💡 by Brendan | © 2025 | be |</p>",
        unsafe_allow_html=True
    )
