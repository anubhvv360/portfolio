import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(
    page_title="Gen AI Apps Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main header and intro
st.title("Anubhav's Gen AI Apps")
st.write(
    "Welcome to my portfolio of Gen AI applications. "
    "I create these apps using Streamlit, LangChain and Gemini. "
    "Below you'll find the applications—do take them for a test drive!"
)

# Sidebar with photo, summary, timeline, contact and LinkedIn posts
with st.sidebar:
    st.markdown(
    """
    <div style="display:flex; justify-content:center;">
        <img 
            src="https://raw.githubusercontent.com/anubhvv360/portfolio/main/assets/anubhav_photo.png" 
            width="180"
        >
    </div>
    """,
    unsafe_allow_html=True
    )
    #st.image("https://raw.githubusercontent.com/anubhvv360/portfolio/main/assets/anubhav_photo.png", width=180)
    st.markdown("## About Me")
    st.write(
        "Tech-savvy consultant with 3 years of experience building Oracle-based systems for finance and supply chain. I turn business needs into scalable solutions—managing everything from design to rollout. Comfortable wearing multiple hats, working cross-functionally, and delivering impact in fast-paced, agile environments."
    )

    st.markdown("### 📅 Professional Journey")
    st.markdown(
        """
        - **2025–Present:** Consultant at Accenture Avanade
        - **2024–2025:** _MBA_ — Great Lakes Institute of Management, Chennai
        - **2023–2024:** Certificate Programme in Project Management (_CPPM_) — IIM Indore, Executive Education
        - **2022–2024:** Consultant at Genpact
        - **2021–2022:** Senior Associate at Genpact
        - **2018–2021:** _BBA Finance_ — Symbiosis Centre for Management Studies, Noida
        """
    )

    st.markdown("### 📬 Contact")
    st.markdown(
        """
        - ✉️ [anubhav.verma360@gmail.com](mailto:anubhav.verma360@gmail.com)  
        - 📱 +91-87004-48744
        - 📱 +971-55-880-5548
        - 🔗 [LinkedIn](https://www.linkedin.com/in/anubhvv/)
        """
    )

    #st.markdown("### 🔗 LinkedIn Posts")
# 1) Paste in the exact iframe-src URLs LinkedIn provides (you can append ?compact=1 if you like)
    linkedin_iframes = [
        "https://www.linkedin.com/embed/feed/update/urn:li:share:7297070217476681728?collapsed=1",
        "https://www.linkedin.com/embed/feed/update/urn:li:share:7234535171226525697?collapsed=1",
        "https://www.linkedin.com/embed/feed/update/urn:li:share:7213290956660297729?collapsed=1",
        "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7235718807384637440?collapsed=1",
    ]

    # 2) Loop and inject each as an iframe
    for src in linkedin_iframes:
        components.html(
            f'''
            <iframe 
              src="{src}" 
              height="400" 
              width="100%" 
              frameborder="0" 
              allowfullscreen="" 
              title="LinkedIn post"
            ></iframe>
            ''',
            height=420  # a little taller than the iframe itself
        )

# List of Gen AI apps to display
apps = [
    {
        "name": "Procurement AI Agent",
        "description": "This AI-driven tool automates TransGlobal Industries' procurement using GenAI (LLMs, LangChain, Streamlit). It converts business needs into technical specs, generates RFPs, streamlines vendor selection, evaluates bids, and simulates negotiations—boosting efficiency, accuracy, and speed.",
        "video_url": "https://youtu.be/YBKi49rBEg4",
        "link": "https://procurementagent.streamlit.app/"
    },
    {
        "name": "SWOT Analysis Agent",
        "description": "This LLM-powered AI Agent performs a detailed SWOT analysis, offering structured insights into a company's Strengths, Weaknesses, Opportunities, and Threats to aid strategic decision-making.",
        "video_url": "https://youtu.be/6d411ybBAm4",
        "link": "https://swotanalysis.streamlit.app/"
    },
    {
        "name": "Resume Pivot Tool",
        "description": "Resume Pivot Tool helps you generate ATS-friendly, domain-specific projects grounded in your actual experience. Upload your resume and a target job description to extract core work, skills, and JD insights.",
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
        "description": "This tool generates a Karma Yoga weekly report based on actual work done and the previous report. Karma Yoga is a social impact course at Great Lakes, Chennai. This tool helped students stay focused on on-ground tasks instead of report writing.",
        "video_url": "https://youtu.be/XQW0tHtI2cM",
        "link": "https://karmayoga.streamlit.app/"
    }
]

# Render each app section with video + a gradient button
for app in apps:
    st.header(app["name"])
    st.write(app["description"])
    st.video(app["video_url"])

    link = app["link"]
    button_html = f'''
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

    <a href="{link}" target="_blank">
      <button class="gradient-button">
        Try it out
      </button>
    </a>
    '''
    st.markdown(button_html, unsafe_allow_html=True)
    st.markdown("---")

st.markdown("""
    <style>
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .animated-gradient {
        background: linear-gradient(90deg, blue, purple, blue);
        background-size: 300% 300%;
        animation: gradientAnimation 8s ease infinite;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        color: white;
        font-weight: normal;
        font-size: 18px;
    }
    </style>

    <div class="animated-gradient">
        Made with ❤️ by Anubhav Verma
    </div>
""", unsafe_allow_html=True)
