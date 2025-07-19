import streamlit as st
import pandas as pd
import time
from utils.send_mail import send_email
from utils.toast_manager import handle_redirect_toast

# ─── Contact Me Page ───

def show():
    handle_redirect_toast()
    # Page title and main header
    st.title("📧 Contact me")
    st.subheader("""
    I look forward to hearing from you.
    """)
    st.write("""
    To let me know more about your interests, please fill out the form below.
    """)

    df = pd.read_csv("topics.csv")

    # Define the form
    with st.form(key="contact_form"):
        guest_name = st.text_input("Name")
        email = st.text_input("Email")
        topic = st.selectbox("Please select a topic that you would like to discuss.", df["topic"])
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            # Send the email
            send_email(f"Subject: {topic.title()}\n\nFrom {guest_name}\nEmail address: {email}\n\n{message}")
            st.success("Thank you for your message! I'll get back to you as soon as I can.")
            time.sleep(3)  # Wait for 3 seconds
            st.rerun()  # Refresh the page to reset the form

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