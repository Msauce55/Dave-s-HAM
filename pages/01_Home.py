import streamlit as st
import requests
from datetime import datetime

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