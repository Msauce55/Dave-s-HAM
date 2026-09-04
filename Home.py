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
        background: #05080f;
        color: #ffffff;
        overflow: hidden;
    }
    
    /* Deep Space + Nebula */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: radial-gradient(circle at 30% 20%, rgba(0, 240, 255, 0.15) 0%, transparent 50%),
                    radial-gradient(circle at 70% 70%, rgba(180, 80, 255, 0.12) 0%, transparent 60%),
                    radial-gradient(circle at 20% 80%, rgba(0, 180, 255, 0.10) 0%, transparent 70%);
        z-index: -2;
    }
    
    /* Dense Starfield */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-image: 
            radial-gradient(#ffffff 1px, transparent 1px),
            radial-gradient(#ffffff 1px, transparent 1px),
            radial-gradient(#88ddff 1px, transparent 2px),
            radial-gradient(#ffddaa 1px, transparent 2px);
        background-size: 70px 70px, 120px 120px, 180px 180px, 250px 250px;
        background-position: 0 0, 35px 55px, 80px 30px, 120px 90px;
        opacity: 0.45;
        z-index: -1;
        pointer-events: none;
    }

    /* Radio Wave Effect */
    .radio-waves {
        position: fixed;
        top: 15%;
        right: 10%;
        width: 180px;
        height: 180px;
        border: 2px solid rgba(0, 240, 255, 0.15);
        border-radius: 50%;
        animation: pulse 8s infinite ease-in-out;
        z-index: -1;
        opacity: 0.3;
    }

    @keyframes pulse {
        0% { transform: scale(0.8); opacity: 0.2; }
        50% { transform: scale(1.3); opacity: 0.4; }
        100% { transform: scale(0.8); opacity: 0.2; }
    }

    h1, h2, h3, h4 {
        color: #00f0ff !important;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.5);
    }
    
    .stApp, p, span, div, label, .stMarkdown {
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] {
        background: #05080f;
        border-right: 3px solid #00f0ff33;
    }
    
    div[data-testid="stMetric"] {
        background: #0f2344;
        border: 1px solid #00f0ff55;
        border-radius: 12px;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #00f0ff, #0099cc);
        color: #0a1325;
        font-weight: 700;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff7700, #ffaa00);
        color: white;
    }
    
    .stTextInput input, .stTextArea textarea {
        background-color: #0f2344 !important;
        color: #ffffff !important;
        border: 1px solid #00f0ff66 !important;
    }
</style>
""", unsafe_allow_html=True)

# Logo
col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=170)
    else:
        st.markdown("**📡 Dave's Ham**")

st.markdown('<div class="radio-waves"></div>', unsafe_allow_html=True)
st.markdown("---")

st.title("Welcome to Dave's Ham Radio Portal")
st.caption("📡 Connecting the world through the airwaves — from Earth to the cosmos")

@st.cache_data(ttl=300)
def fetch_solar_indices():
    try:
        k = requests.get("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json", timeout=10).json()
        flux = requests.get("https://services.swpc.noaa.gov/json/f107_cm_flux.json", timeout=10).json()
        daily = requests.get("https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json", timeout=10).json()
        
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
st.subheader("📡 Quick Navigation")
st.markdown("""
- ☀️ **Space Weather & Propagation**  
- 📡 **DX / POTA / APRS Activity**  
- 📶 **Repeaters & Digital Modes**  
- 🪪 **Callsign & License Tools**  
- 🚨 **Emergency Comms & Club**  
- 🔧 **Calculators & Technical**  
- 📝 **Dave's Blog**
""")

st.caption(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC • Powered by the Ionosphere")