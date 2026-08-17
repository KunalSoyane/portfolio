import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Kunal Soyane | Data Scientist", page_icon="📊", layout="wide")

# --- GLOBAL STYLES ---
st.markdown("""
<style>
.project-banner {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
    border-radius: 16px;
    padding: 2.5rem 2rem;
    margin-bottom: 1.5rem;
}
.project-banner .icon { font-size: 2.75rem; margin-bottom: 0.25rem; }
.project-banner h1 { color: white !important; margin: 0 0 0.4rem 0; font-size: 2.1rem; }
.project-banner p { color: #E0E7FF; margin: 0; font-size: 1.05rem; }
.tech-chip {
    display: inline-block;
    background: #EEF2FF;
    color: #4338CA;
    border: 1px solid #C7D2FE;
    border-radius: 999px;
    padding: 0.3rem 0.9rem;
    margin: 0.2rem 0.35rem 0.2rem 0;
    font-size: 0.85rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# --- PROJECT DATA ---
# Fill in live_link / github_link for each project below once you have the real URLs.
PROJECTS = [
    {
        "nav": "📈 Kronos — Trading Bot",
        "icon": "📈",
        "title": "Kronos — Algorithmic Trading Bot",
        "tagline": "A live, self-trading NSE bot — from OHLCV bars to executed orders.",
        "problem": "Manual intraday trading on the NSE means reacting late, second-guessing every entry, and being at the mercy of emotion. I wanted a system that could watch the market and act on a defined edge, faster and more consistently than I could by hand.",
        "solution": [
            "Pulls live 5-minute OHLCV bars via the Upstox API and generates trade signals with LightGBM/transformer models trained using Triple Barrier labeling and KMeans-based regime detection.",
            "Validates every model with walk-forward cross-validation and isotonic calibration before it's allowed near live capital.",
            "Executes and manages positions automatically, with a Discord bot as the control room — entries, exits, and P&L in one channel.",
        ],
        "tech_stack": ["Python", "Upstox API", "LightGBM", "SQLite", "Discord.py", "GCP"],
        "live_link": None,
        "github_link": None,
    },
    {
        "nav": "🤖 Jarvis — AI Assistant",
        "icon": "🤖",
        "title": "Jarvis — Local AI Assistant",
        "tagline": "A fully local AI assistant — no cloud, no API calls, just your machine.",
        "problem": "Cloud-based assistants send everything you say to someone else's server. I wanted an assistant that lived entirely on my own hardware — CPU-only, 8GB of RAM, no exceptions.",
        "solution": [
            "Fine-tuned Llama 3.2 3B with Unsloth on a custom instruction dataset, rebuilt across three versions to fix failure modes, served locally through Ollama.",
            "Full voice loop: Silero for voice-activity detection, Whisper for transcription, Kokoro for text-to-speech.",
            "Acts on the OS directly through PyAutoGUI and keeps context with a ChromaDB memory store, wrapped in a lightweight Tkinter overlay.",
        ],
        "tech_stack": ["Python", "Llama 3.2 (fine-tuned)", "Ollama", "Whisper", "Silero VAD", "Kokoro TTS", "ChromaDB", "PyAutoGUI"],
        "live_link": None,
        "github_link": None,
    },
    {
        "nav": "📋 AI Resume Screener",
        "icon": "📋",
        "title": "AI Resume Screener",
        "tagline": "LLM-powered resume screening people actually paid for.",
        "problem": "Screening resumes against a job description is repetitive to do by hand, and most 'AI' tools for it just pipe your data to someone else's API.",
        "solution": [
            "Runs entirely on a locally-hosted Llama 3.2 via Ollama — no resume data leaves the machine it runs on.",
            "Scores and ranks candidates against a given job description, batch by batch.",
            "Validated with 40+ real users and priced at ₹199 per batch — the first project I've actually charged for.",
        ],
        "tech_stack": ["Python", "Ollama", "Llama 3.2", "NLP"],
        "live_link": None,
        "github_link": None,
    },
    {
        "nav": "🏏 Power BI — IPL Analytics",
        "icon": "🏏",
        "title": "Power BI — IPL Analytics",
        "tagline": "Fifteen years of IPL data, modeled from the ground up.",
        "status": "🔧 In progress — data modeling done, DAX & report layer next",
        "problem": "Most of my analytics work had been code-first. I wanted to get properly fluent in the tool most BI teams actually standardize on.",
        "solution": [
            "Built a star-schema data model in Power BI from a real 260K-row, 60+ column IPL dataset spanning 2008–2025, cleaned and shaped with Power Query.",
            "Working through the rest of the curriculum — DAX measures, visuals, and the interactive report layer — on top of that foundation.",
        ],
        "tech_stack": ["Power BI", "Power Query", "Data Modeling"],
        "live_link": None,
        "github_link": None,
    },
    {
        "nav": "🔍 stock_predictor",
        "icon": "🔍",
        "title": "stock_predictor — NSE Scanner",
        "tagline": "A LightGBM scanner that flags NSE setups worth a second look.",
        "problem": "Kronos trades one live pipeline. I wanted a lighter-weight scanner that could screen the wider NSE universe for setups worth a closer look, without the overhead of a full execution engine.",
        "solution": [
            "LightGBM binary classifier for the buy/no-buy call, with a regression-based magnitude gate handling the 'hold' case instead of a brittle third class.",
            "Rebuilt the pipeline (v2, across 8 files) after diagnosing why the original was outputting all-HOLD — imbalanced labels and gating logic that never let a signal through.",
        ],
        "tech_stack": ["Python", "LightGBM", "Pandas", "NumPy"],
        "live_link": None,
        "github_link": None,
    },
    {
        "nav": "🧪 ML Playground",
        "icon": "🧪",
        "title": "ML Playground",
        "tagline": "Five end-to-end scikit-learn pipelines, one place to see the fundamentals.",
        "problem": "Wanted one place that shows the scikit-learn fundamentals cleanly, instead of scattered across a dozen separate notebooks.",
        "solution": [
            "Five end-to-end pipelines covering the core scikit-learn workflow, from preprocessing through model evaluation.",
            "Built as a reference I still come back to when starting a new ML problem.",
        ],
        "tech_stack": ["Python", "Scikit-learn", "Pandas", "NumPy"],
        "live_link": None,
        "github_link": None,
    },
    {
        "nav": "🌿 AyurDietPro",
        "icon": "🌿",
        "title": "AyurDietPro",
        "tagline": "A full-stack diet-planning app built on Ayurvedic principles.",
        "problem": "Personalized diet guidance is usually locked behind an app or a consultation. I wanted to see what a lightweight, self-hosted version could look like.",
        "solution": [
            "FastAPI backend with SQLite handles user and diet data; React + Vite on the frontend.",
            "Containerized with Docker so the whole stack runs with one command.",
        ],
        "tech_stack": ["React", "Vite", "FastAPI", "Python", "SQLite", "Docker"],
        "live_link": None,
        "github_link": None,
    },
    {
        "nav": "📊 Sales Dashboard",
        "icon": "📊",
        "title": "Superstore Sales Dashboard",
        "tagline": "Turning raw retail data into KPIs you can actually act on.",
        "problem": "Raw transactional sales data doesn't tell you anything on its own — it needs to become trackable KPIs and visible trends before it's useful.",
        "solution": [
            "Time-series analysis tracking monthly sales growth.",
            "Interactive filters to drill down by region and category.",
            "Real-time KPI tracking for total sales and profit.",
        ],
        "tech_stack": ["Python", "Pandas", "Plotly Express", "Streamlit"],
        "live_link": "https://sales-dashboard-jzxwbcn4rlmmviss9evapp6.streamlit.app/",
        "github_link": "https://github.com/KunalSoyane/sales-dashboard",
    },
]

PROJECT_BY_NAV = {p["nav"]: p for p in PROJECTS}

# --- SIDEBAR (Navigation) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me"] + [p["nav"] for p in PROJECTS])

st.sidebar.write("---")
st.sidebar.write("📧 **Contact:** kunalviveksoyane@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/kunal-vivek-soyane/) | [GitHub](https://github.com/KunalSoyane)")


def render_project(p):
    st.markdown(f"""
    <div class="project-banner">
        <div class="icon">{p['icon']}</div>
        <h1>{p['title']}</h1>
        <p>{p['tagline']}</p>
    </div>
    """, unsafe_allow_html=True)

    if p.get("status"):
        st.caption(p["status"])

    st.markdown("### The Problem")
    st.write(p["problem"])

    st.markdown("### The Solution")
    for step in p["solution"]:
        st.write(f"- {step}")

    st.markdown("### Tech Stack")
    chips_html = "".join(f'<span class="tech-chip">{t}</span>' for t in p["tech_stack"])
    st.markdown(chips_html, unsafe_allow_html=True)

    st.write("")
    if p.get("live_link"):
        st.success(f"👉 **[Try the Live App]({p['live_link']})**")
    if p.get("github_link"):
        st.info(f"📂 **[View Source on GitHub]({p['github_link']})**")
    if not p.get("live_link") and not p.get("github_link"):
        st.caption("🔗 Links coming soon — add your repo/demo URL here.")


# --- PAGE: ABOUT ME ---
if page == "About Me":
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=200)

    with col2:
        st.title("👨‍💻 Hi, I'm Kunal Soyane")
        st.subheader("IT Engineering Student | Aspiring Data Scientist")
        st.write("""
        I'm a third-year IT engineering student who builds ML systems end-to-end —
        not just the training pipeline, but the deployment, the bug fixes, and the parts
        that only show up once something is actually running. Recent work spans a live
        algorithmic trading bot, a fully local fine-tuned AI assistant, and a tool people
        have paid real money to use.
        """)
        st.info("🎓 **Education:** B.Tech in IT — 3rd Year")

    st.write("---")
    st.subheader("Technical Skills")

    skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4)
    with skill_col1:
        st.write("🐍 **Core**")
        st.write("Python, SQL, Java")
    with skill_col2:
        st.write("🤖 **ML & Data**")
        st.write("Scikit-learn, LightGBM, Pandas, NumPy")
    with skill_col3:
        st.write("🧠 **LLMs & AI**")
        st.write("OpenAI, Gemini, Groq, Ollama, fine-tuning")
    with skill_col4:
        st.write("📊 **BI & Viz**")
        st.write("Power BI, Plotly, Streamlit")

# --- PROJECT PAGES ---
else:
    render_project(PROJECT_BY_NAV[page])
