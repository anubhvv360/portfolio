import streamlit as st

# Set page configuration
st.set_page_config(page_title="Gen AI Apps Portfolio", layout="centered")

# Title and Introduction
st.title("Gen AI Apps Portfolio")
st.write("""
Welcome to my portfolio of Gen AI applications. Explore the projects below by clicking on the buttons to be redirected to the respective app pages. 
Watch the walkthrough video for an overview of my work.
""")

# Walkthrough Video Section
st.header("Walkthrough Video")
# Replace the URL below with your own walkthrough video URL or use a local file path.
video_url = "https://www.example.com/path_to_your_video.mp4"
st.video(video_url)

# Portfolio Apps Section
st.header("Explore My Gen AI Apps")

# List of Gen AI apps with details
# apps = [
#     {
#         "name": "Procurement Agentic AI",
#         "link": "https://procurementagent.streamlit.app/",
#         "description": "A conversational AI that assists with various tasks, from customer support to interactive learning."
#     },
#     {
#         "name": "Gen AI Image Generator",
#         "link": "https://example.com/gen-ai-image-generator",
#         "description": "Generates visually appealing images from text prompts using advanced AI techniques."
#     },
#     {
#         "name": "Gen AI Data Analyzer",
#         "link": "https://example.com/gen-ai-data-analyzer",
#         "description": "Provides in-depth analysis of complex data sets using AI-driven insights."
#     }
# ]

# # Display each app with its description and a clickable button
# for app in apps:
#     st.subheader(app["name"])
#     st.write(app["description"])
    
#     # Create a clickable HTML button that opens the link in a new tab
#     button_html = f'''
#     <a href="{app["link"]}" target="_blank">
#         <button style="padding: 10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:5px; cursor:pointer;">
#             Visit {app["name"]}
#         </button>
#     </a>
#     '''
#     st.markdown(button_html, unsafe_allow_html=True)
#     st.markdown("---")
