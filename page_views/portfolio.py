import streamlit as st
import pandas as pd
import os

def show():
    st.markdown("<style>body { background-color: #0f1117; color: #f4f4f4; }</style>", unsafe_allow_html=True)
    st.markdown("""
        <style>
            .project-card {
                background-color: #1c1e26;
                padding: 1.2rem;
                border-radius: 1rem;
                margin-top: 1rem;  /* 👈 Add this */
                box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
                transition: 0.3s ease-in-out;
            }
            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0px 6px 16px rgba(255, 255, 255, 0.08);
                border-left: 4px solid #09f;
            }
            .tag-pill {
                display: inline-block;
                background-color: #333;
                border-radius: 10px;
                padding: 4px 10px;
                margin-right: 6px;
                margin-top: 4px;
                font-size: 12px;
                color: #09f;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("📂 Portfolio")
    st.caption("A clean & playful overview of tools, automations, and impact-driven apps.")

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

    # Sidebar filter UI
    with st.sidebar:
        st.markdown("### 🎛 Filter Projects")
        selected_category = st.selectbox("📁 Category", ["All"] + all_categories)
        selected_tags = st.multiselect("🏷️ Tags", all_tags)

    # Filter logic
    filtered_df = df.copy()
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df['category'] == selected_category]

    for tag in selected_tags:
        filtered_df = filtered_df[filtered_df['tags'].str.contains(tag, case=False, na=False)]

    # Sort featured projects first
    featured_df = filtered_df[filtered_df['featured'] == True]
    others_df = filtered_df[filtered_df['featured'] != True]
    display_df = pd.concat([featured_df, others_df])

    # Display projects
    for _, row in display_df.iterrows():
        with st.container():
            col1, col2 = st.columns([2, 1])

            with col1:
                # st.markdown(f"<div class='project-card'>", unsafe_allow_html=True)  # START inside col1

                st.subheader(row['title'])
                st.markdown(f"<p style='font-size:15px'>{row['description']}</p>", unsafe_allow_html=True)

                if row['tags']:
                    tags_html = ''.join(
                        f"<span class='tag-pill'>{tag.strip()}</span>" for tag in row['tags'].split(";"))
                    st.markdown(tags_html, unsafe_allow_html=True)

                st.markdown("⭐ **Add to favorites** _(coming soon)_")
                st.markdown(f"[🔗 View Project]({row['url']})", unsafe_allow_html=True)
                # st.markdown("</div>", unsafe_allow_html=True)  # ✅ CLOSE inside col1

            with col2:
                image_path = f"images/{row['image']}"
                if os.path.exists(image_path):
                    st.image(image_path, use_container_width=True)
                else:
                    st.info("📷 Image not found.")

            st.markdown("---")
