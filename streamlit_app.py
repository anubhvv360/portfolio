import streamlit as st

# Set page configuration
st.set_page_config(page_title="Gen AI Apps Portfolio", layout="centered")

# Common Introduction
st.title("Gen AI Apps Portfolio")
st.write("Welcome to my portfolio of Gen AI applications. Below you'll find individual sections for each app with a brief description, demo video, and a button to try out the app.")

# Define the portfolio apps
apps = [
    {
        "name": "Gen AI Chatbot",
        "description": "A conversational AI that assists with various tasks, from customer support to interactive learning.",
        "video_url": "https://www.example.com/path_to_your_chatbot_video.mp4",  # Replace with your video URL
        "link": "https://example.com/gen-ai-chatbot"  # Replace with your app link
    },
    {
        "name": "Gen AI Image Generator",
        "description": "Generates visually appealing images from text prompts using advanced AI techniques.",
        "video_url": "https://www.example.com/path_to_your_image_generator_video.mp4",  # Replace with your video URL
        "link": "https://example.com/gen-ai-image-generator"  # Replace with your app link
    },
    {
        "name": "Gen AI Data Analyzer",
        "description": "Provides in-depth analysis of complex data sets using AI-driven insights.",
        "video_url": "https://www.example.com/path_to_your_data_analyzer_video.mp4",  # Replace with your video URL
        "link": "https://example.com/gen-ai-data-analyzer"  # Replace with your app link
    }
]

# Iterate over each app to display its individual content
for app in apps:
    st.header(app["name"])
    st.write(app["description"])
    st.video(app["video_url"])
    
    # Create a clickable button that opens the app link in a new tab
    button_html = f"""
    <a href="{app["link"]}" target="_blank">
        <button style="padding: 10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:5px; cursor:pointer;">
            Try it out
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    st.markdown("---")
