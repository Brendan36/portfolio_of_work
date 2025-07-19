import base64
import streamlit as st
import pandas as pd
from streamlit import empty
from utils.toast_manager import handle_redirect_toast


# st.set_page_config(layout="wide")

def show():
    handle_redirect_toast()
    params = st.query_params
    if params.get("page", [""])[0] == "contact":
        st.session_state["redirect_page"] = "📧 Contact me"
        st.session_state["redirected_from"] = "🏠 Home"
        # clear it so we only fire once
        st.query_params.clear()
        st.rerun()

    # Logo Header
    # Visual Navigation with Columns
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.image("images/blue smiley.jpg", width=300)
    with col2:
        st.markdown("## Hi, I’m Brendan!")
        st.markdown("""###### 💡 Data-Driven Innovator""")
        st.markdown("""###### 🌍 Ethical Tech Builder""")
        st.markdown("""###### 🧠 AI-Powered Analyst""")
    st.markdown("---")

    st.markdown("""
        I’m a cross-disciplinary problem solver passionate about using technology and data to build systems enabling transparency, that empower people and promote sustainable outcomes. 
        
        With a foundation in data analytics, algorithmic trading, and AI, I'm creating tools to challenge norms... 
        
        My ongoing personal projects span from ethical trading bots to smart dashboards that visualize impact and decision-making in real time.
""")
    st.markdown("---")

    mission_statement = """
        Mission 🫡
        """
    st.header(mission_statement)
    # st.markdown("---")
    blurb = """
        To build systems that empower people and promote sustainable outcomes.\n
        """
    st.write(blurb)
    st.markdown("---")

    st.markdown("""#### 🧠 My inspiration for builds sits at the intersection of:""")
    st.markdown("""##### Finance & Sustainability (💰+🌱)""")
    st.write("""
        *Building algorithmic trading systems that prioritize ethical investment*""")
    st.markdown("""##### AI & Human Insight (🤖 + 👥) | Data & Technology (📊 + 💻)""")
    st.write("""
        *Applying machine learning, NLP, and statistical models to extract meaning from complex data*
        """)
    st.markdown("""##### Innovation & Integrity (🆕 + ♾️)""")
    st.write("""
        *Developing a project suite to spark reflection, fairness, and accountability*         
    """)
    st.markdown("""##### Education & Empowerment (👨‍🎓 + 🏋️‍♂️)""")
    st.write("""
        *Making data and tech more accessible*
        """)
    st.markdown("---")

    df = pd.read_csv('portfolio_data.csv', sep=';')  # read the csv file

    st.markdown("""
            Let’s connect if you’re working on:

            ✅ Ethical finance & fintech

            ✅ AI/ML for transparency and/or sustainability

            ✅ Bias detection, smart analytics, and/or responsible tech

            ✅ Data science, machine learning, and/or AI for social good

    """)
    st.button("contact me", on_click=lambda: st.session_state.update({'page': '📧 Contact me'}))

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