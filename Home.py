import streamlit as st
import requests
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Dave's Ham", page_icon="📡", layout="wide", initial_sidebar_state="expanded")

LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main { background: transparent !important; }
    
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image:
            radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.95), transparent),
            radial-gradient(1px 1px at 50px 160px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 90px 40px, rgba(200,240,255,0.9), transparent),
            radial-gradient(1px 1px at 130px 80px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 160px 120px, rgba(255,255,255,0.85), transparent),
            radial-gradient(1px 1px at 200px 50px, #aaddff, transparent),
            radial-gradient(1.5px 1.5px at 220px 180px, #ffffff, transparent),
            radial-gradient(1px 1px at 300px 100px, rgba(255,255,255,0.9), transparent),
            radial-gradient(1.5px 1.5px at 350px 60px, #ffffff, transparent),
            radial-gradient(1px 1px at 400px 150px, #88ccff, transparent),
            radial-gradient(1.5px 1.5px at 450px 30px, #ffffff, transparent);
        background-size: 500px 300px; background-repeat: repeat; opacity: 0.7; z-index: 0; pointer-events: none;
    }
    .stApp::after {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 20% 30%, rgba(0,200,255,0.12) 0%, transparent 50%),
                    radial-gradient(circle at 80% 70%, rgba(140,60,255,0.10) 0%, transparent 55%);
        z-index: 0; pointer-events: none;
    }
    .main .block-container { position: relative; z-index: 1; }

    h1, h2, h3 { color: #00f0ff !important; text-shadow: 0 0 12px rgba(0,240,255,0.5); }
    .stApp, p, span, div, label, .stMarkdown { color: #ffffff !important; }

    [data-testid="stDataFrame"], [data-testid="stDataFrame"] *, table, th, td,
    div[data-testid="stVerticalBlockBorderWrapper"], div[data-testid="stVerticalBlockBorderWrapper"] *,
    .stForm, .stForm * { color: #000000 !important; }

    div[data-testid="stMetric"] { background: #0f2344 !important; border: 1px solid #00f0ff55; border-radius: 12px; }
    div[data-testid="stMetric"] * { color: #ffffff !important; }

    section[data-testid="stSidebar"] { background: #05080f !important; border-right: 2px solid #00f0ff33; }
    .stButton > button { background: linear-gradient(90deg, #00f0ff, #0099cc); color: #0a1325; font-weight: 700; border-radius: 8px; }
    .stButton > button:hover { background: linear-gradient(90deg, #ff7700, #ffaa00); color: white; }
    .stTextInput input, .stTextArea textarea { background-color: #0f2344 !important; color: #ffffff !important; border: 1px solid #00f0ff66 !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)
    else:
        st.markdown("**📡 Dave's Ham**")

st.markdown("---")
st.title("Welcome to Dave's Ham Radio Portal")
st.caption("📡 Connecting the world through the airwaves — from Earth to the cosmos")

@st.cache_data(ttl=300)
def fetch_solar():
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

solar = fetch_solar()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Solar Flux (SFI)", solar["sfi"])
c2.metric("K-Index", solar["k_index"])
c3.metric("A-Index", solar["a_index"])
c4.metric("Sunspot Number", solar["ssn"])

st.markdown("---")
st.subheader("📡 Quick Navigation")
st.markdown("""
- ☀️ Space Weather & Propagation  
- 📡 DX / POTA / APRS Activity  
- 📶 Repeaters & Digital Modes  
- 🪪 Callsign & License Tools  
- 🚨 Emergency Comms & Club  
- 🔧 Calculators & Technical  
- 📝 Dave's Blog
""")
st.caption(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC")