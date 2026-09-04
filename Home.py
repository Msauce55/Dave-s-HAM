import streamlit as st
import requests
from datetime import datetime
from pathlib import Path

# ====================== PAGE CONFIG & STYLING ======================
st.set_page_config(
    page_title="Dave's Ham",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0f1b38 0%, #1a2a5e 40%, #0f1b38 100%);
        color: #ffffff;
    }
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-image: 
            radial-gradient(white 1px, transparent 1px),
            radial-gradient(white 1px, transparent 1px),
            radial-gradient(#a5d6ff 1px, transparent 1px);
        background-size: 90px 90px, 140px 140px, 200px 200px;
        background-position: 0 0, 30px 60px, 80px 120px;
        opacity: 0.25;
        pointer-events: none;
        z-index: -1;
    }
    h1, h2, h3 {
        color: #00f0ff !important;
    }
    .stApp, p, span, div, label, .stMarkdown {
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] {
        background: #0c1628;
        border-right: 2px solid #00f0ff33;
    }
    div[data-testid="stMetric"] {
        background: #1e3555;
        border: 1px solid #00f0ff44;
        border-radius: 12px;
        padding: 12px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #00f0ff, #00b8d4);
        color: #0b1f3d;
        font-weight: 700;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff8c00, #ffaa33);
        color: white;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox, .stNumberInput {
        background-color: #1e3555 !important;
        color: #ffffff !important;
        border: 1px solid #00f0ff55 !important;
    }
    .stCaption {
        color: #c0d8ff !important;
    }
</style>
""", unsafe_allow_html=True)

# Logo in top-left
col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=170)
    else:
        st.markdown("**📡 Dave's Ham**")

st.markdown("---")
# ====================== END STYLING ======================

st.title("Welcome to Dave's Ham Radio Portal")
st.caption("Real-time tools for amateur radio operators, students & clubs")

@st.cache_data(ttl=300)
def fetch_solar_indices():
    try:
        k_data = requests.get("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json", timeout=8).json()
        flux_data = requests.get("https://services.swpc.noaa.gov/json/f107_cm_flux.json", timeout=8).json()
        daily = requests.get("https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json", timeout=8).json()
        
        return {
            "sfi": flux_data[-1].get("flux", "—") if flux_data else "—",
            "k_index": k_data[-1].get("kp_index", "—") if k_data else "—",
            "a_index": daily[-1].get("a_index", "—") if daily else "—",
            "ssn": daily[-1].get("ssn", "—") if daily else "—",
        }
    except:
        return {"sfi": "—", "k_index": "—", "a_index": "—", "ssn": "—"}

solar = fetch_solar_indices()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Solar Flux Index (SFI)", solar["sfi"])
c2.metric("K-Index", solar["k_index"])
c3.metric("A-Index", solar["a_index"])
c4.metric("Sunspot Number", solar["ssn"])

st.markdown("---")
st.subheader("Quick Navigation")
st.markdown("""
Use the sidebar to explore:
- ☀️ Space Weather & Propagation  
- 📡 DX / POTA / APRS Activity  
- 📶 Repeaters & Digital Modes  
- 🪪 Callsign & License Tools  
- 🚨 Emergency Comms & Club  
- 🔧 Calculators & Technical  
- 📝 Dave's Blog
""")

st.caption(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC • Data from NOAA SWPC")