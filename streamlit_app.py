import streamlit as st

# Set page configuration
st.set_page_config(page_title="Gen AI Apps Portfolio", page_icon = "👨‍💻", layout="centered")

# Common Introduction
st.title("Anubhav's Gen AI Apps")
st.write("Welcome to my portfolio of Gen AI applications. I create these apps using Streamlit, LangChain and Gemini. Below you'll find individual sections for each app with a brief description, demo video, and a button to try out the app.")

# Define the portfolio apps
apps = [
    {
        "name": "Procurement AI Agent",
        "description": "This AI-driven tool automates TransGlobal Industries' procurement using GenAI (LLMs, LangChain, Streamlit). It converts business needs into technical specs, generates RFPs, streamlines vendor selection, evaluates bids, and simulates negotiations—boosting efficiency, accuracy, and speed.",
        "video_url": "https://youtu.be/YBKi49rBEg4",  # Replace with your video URL
        "link": "https://procurementagent.streamlit.app/"  # Replace with your app link
    },
    {
        "name": "SWOT Analysis Agent",
        "description": "This LLM-powered AI Agent performs a detailed SWOT analysis, offering structured insights into a company's Strengths, Weaknesses, Opportunities, and Threats to aid strategic decision-making.",
        "video_url": "https://youtu.be/6d411ybBAm4",  # Replace with your video URL
        "link": "https://swotanalysis.streamlit.app/"  # Replace with your app link
    },
    {
        "name": "Tell Me About Yourself Generator",
        "description": "This tool generates a unique, engaging, and personalized 'Tell Me About Yourself' introduction. Fill in the details and let AI craft a compelling response!",
        "video_url": "https://youtu.be/XY7ZjBra9rg",  # Replace with your video URL
        "link": "https://intro-agent.streamlit.app/"  # Replace with your app link
    }
]

# Iterate over each app to display its individual content
for app in apps:
    st.header(app["name"])
    st.write(app["description"])
    st.video(app["video_url"])
    
    # Create a clickable button that opens the app link in a new tab
    button_html = f"""
    <style>
      .gradient-button {{
          padding: 10px 20px;
          font-size: 16px;
          color: white;
          border: none;
          border-radius: 5px;
          cursor: pointer;
          background: linear-gradient(45deg, purple, blue);
          background-size: 200% 200%;
          animation: gradientAnimation 3s ease infinite;
      }}
      @keyframes gradientAnimation {{
          0% {{ background-position: 0% 50%; }}
          50% {{ background-position: 100% 50%; }}
          100% {{ background-position: 0% 50%; }}
      }}
    </style>
    <a href="{app["link"]}" target="_blank">
        <button class="gradient-button">
            Try it out
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    st.markdown("---")
