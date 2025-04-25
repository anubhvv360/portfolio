import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Gen AI Apps Portfolio", page_icon = "👨‍💻", layout="wide")

# Common Introduction
st.title("Anubhav's Gen AI Apps")
st.write("Welcome to my portfolio of Gen AI applications. I create these apps using Streamlit, LangChain and Gemini. Below you'll find the applications, do take them for a test drive!")

with st.sidebar:
    st.image("assets/anubhav_photo.jpg", width=180)
    st.markdown("## About Me")
    st.write("Tech-savvy consultant with 3 years of experience building Oracle-based systems for finance and supply chain. I turn business needs into scalable solutions—managing everything from design to rollout. Comfortable wearing multiple hats, working cross-functionally, and delivering impact in fast-paced, agile environments.")

    # Timeline & contact omitted for brevity…

    st.markdown("## 🔗 LinkedIn Posts")

    # 1) Define your post URLs here
    linkedin_post_urls = [
        "https://www.linkedin.com/posts/anubhvv_just-a-few-days-ago-the-pgpm-cohort-of-2025-activity-7297110060512550912-2H-v",
        "https://www.linkedin.com/posts/anubhvv_elevating-my-expertise-proud-to-announce-activity-7213413516408414209-GDTD",
        "https://www.linkedin.com/posts/anubhvv_greatlakes-greatlakeschennai-convocationceremony-activity-7234535172702920704-2Qmq",
        "https://www.linkedin.com/posts/anubhvv_submission-deck-activity-7236213786834018304-yWi6"
        # add more URLs as needed
    ]

    # 2) Loop and embed each one
    for url in linkedin_post_urls:
        components.html(
            f"""
            <blockquote class="linkedin-post" data-lang="en">
              <a href="{url}"></a>
            </blockquote>
            <script src="https://platform.linkedin.com/badges/js/profile.js" async defer></script>
            """,
            height=300  # adjust height per post
        )

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
        "video_url": "https://youtu.be/6d411ybBAm4",
        "link": "https://swotanalysis.streamlit.app/"
    },
    {
        "name": "Resume Pivot Tool",
        "description": "Resume Pivot Tool helps you generate ATS‑friendly, domain‑specific projects grounded in your actual experience. Upload your resume and a target job description to extract core work, skills, and JD insights.",
        "video_url": "https://youtu.be/3nVtrSt3ddI",
        "link": "https://jdprojects2.streamlit.app/"
    },
    {
        "name": "Tell Me About Yourself Generator",
        "description": "This tool generates a unique, engaging, and personalized 'Tell Me About Yourself' introduction. Fill in the details and let AI craft a compelling response!",
        "video_url": "https://youtu.be/XY7ZjBra9rg",
        "link": "https://intro-agent.streamlit.app/"
    },
    {
        "name": "Karma Yoga Report Generator",
        "description": "This tool generates a Karma Yoga weekly report based on actual work done and the previous report. Karma Yoga is a social impact course at Great Lakes, Chennai. This tool helped students stay focused on on ground tasks instead of report writing and documentation.",
        "video_url": "https://youtu.be/XQW0tHtI2cM",
        "link": "https://karmayoga.streamlit.app/"
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

