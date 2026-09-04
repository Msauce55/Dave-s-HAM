import streamlit as st
import requests
from datetime import datetime
from pathlib import Path

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
        background: #0a1325;
        color: #ffffff;
        position: relative;
    }
    
    /* Deep Space Background with Stars & Nebula */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: 
            radial-gradient(circle at 20% 30%, rgba(100, 200, 255, 0.12) 0%, transparent 50%),
            radial-gradient(circle at 70% 60%, rgba(180, 100, 255, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(0, 229, 255, 0.10) 0%, transparent 60%);
        z-index: -2;
    }
    
    /* Starfield */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-image: 
            radial-gradient(white 1px, transparent 1px),
            radial-gradient(white 1px, transparent 1px),
            radial-gradient(#bbeeff 1px, transparent 2px);
        background-size: 80px 80px, 150px 150px, 220px 220px;
        background-position: 0 0, 40px 70px, 90px 30px;
        opacity: 0.35;
        z-index: -1;
        pointer-events: none;
    }

    h1, h2, h3, h4 {
        color: #00f0ff !important;
    }
    
    .stApp, p, span, div, label, .stMarkdown {
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] {
        background: #0a1325;
        border-right: 2px solid #00f0ff33;
    }
    
    div[data-testid="stMetric"] {
        background: #132b4f;
        border: 1px solid #00f0ff44;
        border-radius: 12px;
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
        background-color: #132b4f !important;
        color: #ffffff !important;
        border: 1px solid #00f0ff55 !important;
    }
    
    .stCaption {
        color: #a8c8ff !important;
    }
</style>
""", unsafe_allow_html=True)

# Logo in top-left corner
col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=170)
    else:
        st.markdown("**📡 Dave's Ham**")

st.markdown("---")

st.title("Welcome to Dave's Ham Radio Portal")
st.caption("Real-time tools for amateur radio operators, students & clubs")

@st.cache_data(ttl=300)
def fetch_solar_indices():
    try:
        k = requests.get("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json", timeout=8).json()
        flux = requests.get("https://services.swpc.noaa.gov/json/f107_cm_flux.json", timeout=8).json()
        daily = requests.get("https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json", timeout=8).json()
        
        return {
            "sfi": flux[-1].get("flux", "—") if flux else "—",
            "k_index": k[-1].get("kp_index", "—") if k else "—",
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