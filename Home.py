import streamlit as st
import requests
from datetime import datetime
from pathlib import Path

# ---------- Page Config ----------
st.set_page_config(
    page_title="Dave's Ham",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Logo + Theme Colors (from the emblem) ----------
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    /* Main background - deep navy from the logo */
    .stApp {
        background: linear-gradient(180deg, #0a1628 0%, #0d1f3c 50%, #0a1628 100%);
        color: #e0f7ff;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #07101f 0%, #0d1f3c 100%);
        border-right: 1px solid #00c4ff33;
    }

    /* Headers */
    h1, h2, h3 {
        color: #00c4ff !important;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background: #13233f;
        border: 1px solid #00c4ff44;
        border-radius: 12px;
        padding: 12px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #00c4ff, #0090cc);
        color: #0a1628;
        font-weight: 700;
        border: none;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff6b00, #ff8c00);
        color: white;
    }

    /* Forms & inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox, .stNumberInput {
        background-color: #13233f !important;
        color: #e0f7ff !important;
        border: 1px solid #00c4ff55 !important;
    }

    /* Dataframes */
    .stDataFrame {
        background-color: #0d1f3c;
    }

    /* Success / Warning boxes */
    .stSuccess {
        background-color: #0d3320;
        border-left: 5px solid #00c4ff;
    }
    .stWarning {
        background-color: #3d2200;
        border-left: 5px solid #ff6b00;
    }

    /* Caption / secondary text */
    .stCaption, small {
        color: #7dd3fc !important;
    }

    /* Divider */
    hr {
        border-color: #00c4ff33;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Logo Header ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), use_container_width=True)
    else:
        st.markdown("### 📡 Dave's Ham Amateur Radio")
        st.caption("Logo not found – place it in assets/daves_ham_logo.png")

st.markdown("<br>", unsafe_allow_html=True)
st.set_page_config(
    page_title="Ham Radio Portal",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main-header {font-size: 2.2rem; font-weight: 700; color: #00d4ff;}
    .sub-header {font-size: 1.1rem; color: #a0aec0; margin-bottom: 1.5rem;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def fetch_solar_indices():
    try:
        k_data = requests.get("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json", timeout=8).json()
        flux_data = requests.get("https://services.swpc.noaa.gov/json/f107_cm_flux.json", timeout=8).json()
        daily = requests.get("https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json", timeout=8).json()
        
        latest_k = k_data[-1] if k_data else {}
        latest_flux = flux_data[-1] if flux_data else {}
        latest_daily = daily[-1] if daily else {}

        return {
            "k_index": latest_k.get("kp_index", "—"),
            "sfi": latest_flux.get("flux", latest_daily.get("f10.7", "—")),
            "a_index": latest_daily.get("a_index", "—"),
            "ssn": latest_daily.get("ssn", "—"),
        }
    except Exception:
        return {"k_index": "—", "sfi": "—", "a_index": "—", "ssn": "—"}

st.markdown('<p class="main-header">📡 Ham Radio Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Real-time tools for operators, students & clubs</p>', unsafe_allow_html=True)

solar = fetch_solar_indices()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Solar Flux (SFI)", solar["sfi"])
col2.metric("K-Index", solar["k_index"])
col3.metric("A-Index", solar["a_index"])
col4.metric("Sunspot Number", solar["ssn"])

st.markdown("---")
st.subheader("Quick Navigation")
st.write("Use the sidebar to open the different tools:")
st.markdown("""
- ☀️ **Space Weather & Propagation**
- 📡 **DX / POTA / APRS Activity**
- 📶 **Repeaters & Digital Modes**
- 🪪 **Callsign & License Tools**
- 🚨 **Emergency Comms & Club**
- 🔧 **Calculators & Technical**
""")

st.markdown("---")
st.caption(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC • Data from NOAA SWPC")
