import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Satellite & ISS", page_icon="🛰️", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], .main { background: transparent !important; }
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
                          radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.95), transparent);
        background-size: 500px 300px; background-repeat: repeat; opacity: 0.7; z-index: 0; pointer-events: none;
    }
    .main .block-container { position: relative; z-index: 1; }
    h1, h2, h3 { color: #00f0ff !important; }
    .stApp, p, span, div, label { color: #ffffff !important; }
    .stButton > button { background: linear-gradient(90deg, #00f0ff, #0099cc) !important; color: #0a1325 !important; width: 100%; }
    section[data-testid="stSidebar"] { background: #05080f !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("🛰️ Satellite & ISS Information")

st.subheader("International Space Station (ISS)")
st.markdown("""
**Voice Repeater (when active):**  
- Uplink: 145.990 MHz (67 Hz tone)  
- Downlink: 145.800 MHz  

**APRS Digipeater:** 145.825 MHz  

**Packet / SSTV** – Check current status
""")

st.subheader("Useful Tracking Sites")
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("N2YO Live Tracking", "https://www.n2yo.com", use_container_width=True)
    st.link_button("Heavens-Above", "https://www.heavens-above.com", use_container_width=True)
with c2:
    st.link_button("ISS Detector", "https://www.issdetector.com", use_container_width=True)
    st.link_button("AMSAT Live", "https://www.amsat.org", use_container_width=True)
with c3:
    st.link_button("SatNOGS Network", "https://network.satnogs.org", use_container_width=True)

st.info("Always verify current frequencies and schedules before attempting a contact.")