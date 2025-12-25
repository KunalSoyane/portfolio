import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Kunal Soyane | Data Scientist", page_icon="📊", layout="wide")

# --- SIDEBAR (Navigation) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Project 1: Resume Parser", "Project 2: Sales Dashboard"])

st.sidebar.write("---")
st.sidebar.write("📧 **Contact:** kunalviveksoyane@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/kunal-vivek-soyane/) | [GitHub](https://github.com/KunalSoyane)")

# --- PAGE 1: ABOUT ME ---
if page == "About Me":
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=200) # Placeholder profile pic
    
    with col2:
        st.title("👨‍💻 Hi, I'm Kunal Soyane")
        st.subheader("IT Engineering Student | Aspiring Data Scientist")
        st.write("""
        I am a 2nd-year student passionate about turning raw data into actionable insights.
        I solve problems using **Python, NLP, and Interactive Dashboards**.
        """)
        st.info("🎓 **Education:** B.Tech in IT (Current)")

    st.write("---")
    st.subheader("Technical Skills")
    
    skill_col1, skill_col2, skill_col3 = st.columns(3)
    with skill_col1:
        st.write("🐍 **Languages**")
        st.write("Python, SQL, Java")
    with skill_col2:
        st.write("📊 **Data Science**")
        st.write("Pandas, NumPy, Plotly, Streamlit")
    with skill_col3:
        st.write("🧠 **AI & NLP**")
        st.write("spaCy, Regex, Scikit-learn")

# --- PAGE 2: RESUME PARSER ---
elif page == "Project 1: Resume Parser":
    st.title("📄 AI Resume Parser")
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*c_fiB-YgbnMl6nntYGBMHQ.jpeg", caption="NLP Pipeline Architecture")
    
    st.markdown("""
    ### **The Problem**
    Recruiters spend hours manually screening resumes. I built an AI tool to automate this.
    
    ### **The Solution**
    A Streamlit app that:
    1. **Extracts** name, email, and phone using Regex.
    2. **Identifies** technical skills using spaCy (NLP).
    3. **Visualizes** the candidate's profile.
    
    ### **Tech Stack**
    - **Python** (Logic)
    - **spaCy** (Natural Language Processing)
    - **Streamlit** (Frontend)
    """)
    
    # YOUR ACTUAL LINK HERE
    st.success("👉 **[Click Here to Try the Live App](https://resume-parser-qy5vdto7j7zpirwtoqrrwe.streamlit.app/)**")
    st.info("📂 **[View Source Code on GitHub](https://github.com/KunalSoyane/resume-parser)**")

# --- PAGE 3: SALES DASHBOARD ---
elif page == "Project 2: Sales Dashboard":
    st.title("📊 Superstore Sales Dashboard")
    # You can add a screenshot of your dashboard here later!
    st.image("https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4960-b9f5-e50122f4815f.png", caption="Interactive Sales Analysis")
    
    st.markdown("""
    ### **The Goal**
    Transform raw sales data into business intelligence to track KPIs and trends.
    
    ### **Key Features**
    - 📈 **Time Series Analysis:** Tracks monthly sales growth.
    - 🔍 **Interactive Filters:** Drill down by Region and Category.
    - 💲 **KPI Tracking:** Real-time calculation of Total Sales & Profit.
    
    ### **Tech Stack**
    - **Pandas** (Data Cleaning & Resampling)
    - **Plotly Express** (Interactive Charts)
    """)
    
    # YOUR NEW LINK HERE
    st.success("👉 **[Click Here to Open Dashboard](https://sales-dashboard-jzxwbcn4rlmmviss9evapp6.streamlit.app/)**")
    st.info("📂 **[View Source Code on GitHub](https://github.com/KunalSoyane/sales-dashboard)**")