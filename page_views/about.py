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
    col1, col2, col3 = st.columns([1,3,1])
    with col1:
        st.image("images/blue smiley.jpg", width=300)
    with col2:
        st.markdown("## Hi, I’m Brendan!")
        st.markdown("""###### 💡 Data-Driven Innovator""")
        st.markdown("""###### 🌍 Ethical Tech Builder""")
        st.markdown("""###### 🧠 AI-Powered Analyst""")
    st.markdown("---")

    st.markdown("""
        I’m a cross-disciplinary problem solver passionate about using technology, transparency, and truth to build systems that empower people and promote sustainable outcomes. 
        
        With a foundation in data analytics, algorithmic trading, and AI, I'm creating tools to challenge norms — from ethical trading bots to smart dashboards that visualize impact and decision-making in real time.
        
        Currently pursuing a BSc (Hons) in Information Technology, I’m combining academic rigor with real-world experimentation — transforming code, data, and values into products that matter.
""")
    st.markdown("---")

    st.markdown("""#### 🧠 My work sits at the intersection of:""")
    st.markdown("""##### Finance & Sustainability (💰+🌱)""")
    st.write("""
        *Building algorithmic trading systems that prioritize ethical investment*""")
    st.markdown("""##### AI & Human Insight (🤖 + 👥) | Data & Technology (📊 + 💻)""")
    st.write("""
        *Applying machine learning, NLP, and statistical models to extract meaning from complex data*
        """)
    st.markdown("""##### Innovation & Integrity (🆕 + ♾️)""")
    st.write("""
        *Developing* | be | *the project suite to spark reflection, fairness, and accountability*         
    """)
    st.markdown("""##### Education & Empowerment (👨‍🎓 + 🏋️‍♂️)""")
    st.write("""
        *Making data and tech more accessible - drawing on 5+ years in the education sector*
        """)
    st.markdown("---")

    df = pd.read_csv('portfolio_data.csv', sep=';')  # read the csv file

    mission_statement = """
        Mission 🫡
        """
    st.header(mission_statement)
    st.markdown("---")
    blurb = """
        To inspire global collaboration so that we can all broaden our understanding of, and fuel the shifts that matter most.\n
    
        Let’s create a better world together!\n
    
        I'm slowly building | be | ©  a suite of applications that will be able to:\n
    
        1. Debunk the correlation between actual impact of the continuous commercialization of natural resources on the world and "sustainable" practices.\n
        2. Improve our understanding of the success stories of collectives and individuals who have extensively researched viable alternatives and have them implemented.\n
        3. Provide insights into the financial results of industries involved and by virtue, their impact while shining light on the environmental cost.\n
        4. Enable peer-to-peer collaboration and resource pooling while educating communities for support to empower new initiatives using sustainable alternatives to better the future. \n
        5. Demonstrate the power of collective action so we can easily quantify our impact and see the changes we are making in our world.\n 
        6. Enable - *collective kindness - the catalyst for change* - so we all have a say in our own pursuit of a better world utilizing the power of collective kindness.\n
        """
    st.write(blurb)
    st.markdown("---")
    st.markdown("""
            Let’s connect if you’re working on:

            ✅ Ethical finance & fintech

            ✅ AI/ML for transparency or sustainability

            ✅ Truth detection, smart analytics, or responsible tech

            ✅ Data science, machine learning, or AI for social good

    """)
    st.button("contact me", on_click=lambda: st.session_state.update({'page': '📧 Contact me'}))
    # st.markdown("---")

    # content3 = """
    #     💡| be | think-tank
    #     """
    #
    # st.header(content3)
    # st.markdown("###### *Projects in production by* 💡| be | labs")
    # # st.subheader("", divider='rainbow')
    # st.markdown("---")
    #
    # # Visual Navigation with Columns
    # col1, col2, col3 = st.columns(3)
    #
    # with col1:
    #     st.image("assets/logo_be_fair_playful.png", width=120)
    #     st.markdown("#### 🌍 | be | me")
    #     st.write("*... empowered & authentic*")
    #     st.write("Uncover truth. Ignite change.")
    #     st.write("choose")
    #     st.button("| be | me", on_click=lambda: st.session_state.update({'page': '🌍 | be | me'}))
    #
    # with col2:
    #     st.image("assets/logo_smile_blue.png", width=120)
    #     st.markdown("#### 🧠 | be | fair")
    #     st.write("*... because truth matters*")
    #     st.write("Decode bias. Filter noise.")
    #     st.write("choose")
    #     st.button("| be | fair", on_click=lambda: st.session_state.update({'page': '🧠 | be | fair'}))
    #
    # with col3:
    #     st.image("assets/logo_be_your_best_bold.png", width=120)
    #     st.markdown("#### 💰 | be | money wise")
    #     st.write("*... ethical investing, redefined*")
    #     st.write("Invest with purpose.")
    #     st.write("choose")
    #     st.button("| be | money wise", on_click=lambda: st.session_state.update({'page': '💰 | be | money wise'}))

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