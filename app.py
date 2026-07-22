import os
import streamlit as st
from generator import generate_post

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI LinkedIn Generator",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Create outputs folder
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# Create folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# File path
file_path = os.path.join(OUTPUT_DIR, "generated_posts.txt")

# -----------------------------
# UI
# -----------------------------
st.title("🚀 AI LinkedIn Post Generator")

st.markdown(
    "Generate professional LinkedIn posts using Generative AI"
)

topic = st.text_input("Enter Topic")

industry = st.selectbox(
    "Industry",
    [
        "Artificial Intelligence",
        "Healthcare",
        "Finance",
        "Education",
        "Software Engineering",
        "Marketing"
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Inspirational",
        "Technical"
    ]
)

length = st.selectbox(
    "Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

audience = st.text_input(
    "Target Audience"
)

emoji = st.radio(
    "Use Emojis?",
    ["Yes", "No"]
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate Post"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):

            try:
                post = generate_post(
                    topic,
                    industry,
                    tone,
                    length,
                    audience,
                    emoji
                )

                st.success("Post Generated")

                st.text_area(
                    "LinkedIn Post",
                    value=post,
                    height=350
                )

                st.download_button(
                    label="Download Post",
                    data=post,
                    file_name="linkedin_post.txt"
                )

                # Save generated post
                with open(
                    file_path,
                    "a",
                    encoding="utf-8"
                ) as f:
                    f.write(post)
                    f.write("\n")
                    f.write("=" * 80)
                    f.write("\n\n")

                st.info(f"Post saved to: {file_path}")

            except Exception as e:
                st.error(f"Error: {e}")