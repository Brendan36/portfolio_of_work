import streamlit as st
import pandas as pd
import base64
import os
from utils.toast_manager import handle_redirect_toast


# Save screen width in session (requires JS workaround in a real app for true width)
if "screen_width" not in st.session_state:
    st.session_state.screen_width = 1200  # Fallback width; adjust as needed

def show():
    handle_redirect_toast()
    if st.session_state.get("redirected_from") == "🏠 Home":
        # st.success("✅ Welcome to the Portfolio! 🎯")
        st.toast("🚀 Loading Portfolio page...", icon="💼")
        del st.session_state["redirected_from"]
    st.markdown("""
        <style>
            body {
                background-color: #0f1117;
                color: #f4f4f4;
            }
            .project-card {
                background-color: #1c1e26;
                padding: 1.2rem;
                border-radius: 1rem;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
                margin-bottom: 2rem;
            }
            .project-card:hover {
                transform: translateY(-3px);
                box-shadow: 0px 6px 18px rgba(255, 255, 255, 0.08);
            }
            .tag-pill {
                display: inline-block;
                background-color: #333;
                border-radius: 10px;
                padding: 4px 10px;
                margin: 4px 6px 0 0;
                font-size: 12px;
                color: #09f;
                white-space: nowrap;
            }

            @media screen and (max-width: 768px) {
                .project-card {
                    padding: 1rem;
                    font-size: 14px;
                }
                .tag-pill {
                    font-size: 11px;
                    padding: 3px 8px;
                }
                img {
                    max-width: 100%;
                    border-radius: 0.5rem;
                }
            }
        </style>
    """, unsafe_allow_html=True)
    # ─── Page Header ───
    col1, col2 = st.columns(2)
    with col1:
        st.title("📂 Portfolio")
        st.caption("A growing clean & playful overview of tools, automations, and impact-driven apps.")
        st.caption("*- All projects in different phases of development -*")
    with col2:
        audio_file_path = "assets/We Deserve To Dream.mp3"
        with open(audio_file_path, "rb") as f:
            audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()

        audio_player_base64 = f"""
            <audio autoplay loop controls>
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
            </audio>
        """
        st.write("*Background music:*")
        st.markdown(audio_player_base64, unsafe_allow_html=True)
        st.write("*Artist: Xavier Rudd*")
        st.write("*Song: We Deserve to Dream*")

    st.markdown("---")

    # ─── Page Content ───
    try:
        df = pd.read_csv("portfolio_data.csv", sep=';')
    except FileNotFoundError:
        st.error("🚫 portfolio_data.csv not found.")
        return

    # Ensure optional columns exist
    df['tags'] = df.get('tags', '')
    df['category'] = df['category'].fillna("Uncategorized")
    df['featured'] = df.get('featured', False)

    # Unique categories/tags
    all_tags = sorted(set(";".join(df['tags'].dropna()).split(";")))
    all_categories = sorted(df['category'].dropna().unique())

    # Sidebar filters
    with st.sidebar:
        st.markdown("### 🎛 Filter Projects")
        selected_category = st.selectbox("📁 Category", ["All"] + all_categories)
        selected_tags = st.multiselect("🏷️ Tags", all_tags)

    # Apply filters
    filtered_df = df.copy()
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df['category'] == selected_category]
    for tag in selected_tags:
        filtered_df = filtered_df[filtered_df['tags'].str.contains(tag, case=False, na=False)]

    # Sort featured first
    display_df = pd.concat([
        filtered_df[filtered_df['featured'] == True],
        filtered_df[filtered_df['featured'] != True]
    ])

    for _, row in display_df.iterrows():
        with st.container():
            # Determine layout: wide = side-by-side, narrow = stacked
            is_mobile = st.session_state.get('screen_width', 1200) < 768

            if is_mobile:
                col1 = st
                col2 = st
            else:
                col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown("<div class='project-card'>", unsafe_allow_html=True)
                st.subheader(row['title'])
                st.markdown(f"<p style='font-size:15px'>{row['description']}</p>", unsafe_allow_html=True)

                # Tag pills
                if row['tags']:
                    tags_html = ''.join(
                        f"<span class='tag-pill'>{tag.strip()}</span>" for tag in row['tags'].split(";")
                    )
                    st.markdown(tags_html, unsafe_allow_html=True)

                st.markdown("⭐ **Add to favorites** _(coming soon)_")
                st.markdown(f"[🔗 View Project]({row['url']})", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                image_path = f"images/{row['image']}"
                if os.path.exists(image_path):
                    if is_mobile:
                        st.image(image_path, use_container_width=True)
                    else:
                        st.image(image_path, width=440)  # Desktop: fixed width
                else:
                    st.info("📷 Image not found.")

            # st.markdown("---")

        # ─── Footer p/item ───
        col1, col2, col3 = st.columns([1, 2, 1])
        footer_html = """
            <p style="text-align:center; color:gray; font-size:0.8em; margin:0;">
              Built with 💡 by | be | © 2025
            </p>
            """
        col2.markdown(footer_html, unsafe_allow_html=True)
        st.markdown("---")

    # ─── Page Footer ───
    # st.markdown("---")
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