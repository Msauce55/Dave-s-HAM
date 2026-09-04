import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="DX / POTA / APRS", page_icon="📡", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], .main { background: transparent !important; }

    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
                          radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.95), transparent),
                          radial-gradient(1px 1px at 90px 40px, #aaddff, transparent),
                          radial-gradient(1.5px 1.5px at 160px 120px, #ffffff, transparent);
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
    .stApp, p, span, div, label { color: #ffffff !important; }

    .stButton > button {
        background: linear-gradient(90deg, #00d4ff, #0099cc) !important;
        color: #03101f !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff8c00, #ffaa00) !important;
        color: white !important;
    }

    section[data-testid="stSidebar"] { background: #05080f !important; border-right: 2px solid #00f0ff33; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("📡 Operational Activity Dashboard")

SAMPLE_DX = [
    {"Spotter": "K1ABC", "DX": "P5DX", "Freq": "14.205", "Mode": "SSB", "Time": "14:32Z", "Note": "North Korea"},
    {"Spotter": "W3LPL", "DX": "FT8WW", "Freq": "21.074", "Mode": "FT8", "Time": "14:28Z", "Note": "Crozet"},
    {"Spotter": "N7QXQ", "DX": "3Y0J", "Freq": "7.074", "Mode": "FT8", "Time": "14:15Z", "Note": "Bouvet"},
    {"Spotter": "K9CT", "DX": "VU4T", "Freq": "28.445", "Mode": "SSB", "Time": "14:05Z", "Note": "Andaman"},
]

SAMPLE_POTA = [
    {"Park": "US-0065", "Name": "Acadia NP", "Activator": "K1ABC", "Freq": "14.285", "Mode": "SSB", "Spots": 12},
    {"Park": "US-0015", "Name": "Yellowstone NP", "Activator": "W7XYZ", "Freq": "7.190", "Mode": "SSB", "Spots": 8},
    {"Park": "US-0041", "Name": "Great Smoky Mtns", "Activator": "N4ABC", "Freq": "14.074", "Mode": "FT8", "Spots": 22},
]

tab1, tab2, tab3 = st.tabs(["DX Cluster Spots", "POTA Activators", "APRS Map"])

with tab1:
    st.subheader("Recent DX Spots (sample)")
    st.dataframe(pd.DataFrame(SAMPLE_DX), use_container_width=True, hide_index=True)
    st.info("In production: connect to a live DX cluster feed")

with tab2:
    st.subheader("Parks on the Air – Current Activators")
    st.dataframe(pd.DataFrame(SAMPLE_POTA), use_container_width=True, hide_index=True)
    st.markdown("[Official POTA](https://pota.app) • [SOTA](https://sotawatch.sota.org.uk)")

with tab3:
    st.subheader("APRS Snapshot (demo)")
    aprs = pd.DataFrame({
        "lat": [41.76, 41.30, 41.55, 41.80],
        "lon": [-72.67, -72.92, -72.65, -72.55],
        "call": ["W1AW-1", "K1CT-9", "N1ABC-7", "W1STR-2"]
    })
    st.map(aprs, size=20)
    st.dataframe(aprs, hide_index=True)