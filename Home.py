import streamlit as st
import requests
from datetime import datetime
from pathlib import Path

import streamlit as st
from pathlib import Path
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="Dave's Ham",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Logo Path
LOGO_PATH = Path("assets/daves_ham_logo.png")

# Improved CSS with lighter blue and starfield background
st.markdown("""
<style>
    /* Starfield Background */
    .stApp {
        background: radial-gradient(circle at 20% 30%, rgba(0, 229, 255, 0.08) 0%, transparent 50%),
                    radial-gradient(circle at 80% 70%, rgba(255, 107, 0, 0.06) 0%, transparent 50%),
                    #0b1426;
        background-attachment: fixed;
        color: #e0f7ff;
    }

    /* Add subtle stars */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: transparent;
        background-image: 
            radial-gradient(white, rgba(255,255,255,0.9) 1px, transparent 0),
            radial-gradient(white, rgba(255,255,255,0.8) 1px, transparent 0);
        background-size: 80px 80px, 120px 120px;
        background-position: 0 0, 40px 60px;
        opacity: 0.15;
        pointer-events: none;
        z-index: 0;
    }

    /* Logo area */
    .logo-container {
        padding: 1rem 0 0.5rem 1.5rem;
    }

    /* Lighter, more visible blue */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #00e5ff !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #08101f;
        border-right: 2px solid #00e5ff33;
    }

    /* Cards & Metrics */
    div[data-testid="stMetric"] {
        background: #13233f;
        border: 1px solid #00e5ff44;
        border-radius: 12px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #00e5ff, #00b8cc);
        color: #0b1426;
        font-weight: 700;
        border: none;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff7b00, #ff9d33);
        color: white;
    }

    /* Input fields */
    .stTextInput input, .stTextArea textarea, .stSelectbox, .stNumberInput {
        background-color: #13233f !important;
        color: #e0f7ff !important;
        border: 1px solid #00e5ff55 !important;
    }
</style>
""", unsafe_allow_html=True)

# ========== Smaller Logo in Top-Left Corner ==========
col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=180)   # Smaller size - adjust as needed
    else:
        st.markdown("**📡 Dave's Ham**")

st.markdown("---")

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
