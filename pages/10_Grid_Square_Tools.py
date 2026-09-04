import streamlit as st
from pathlib import Path
import math

st.set_page_config(page_title="Grid Square Tools", page_icon="🗺️", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], .main { background: transparent !important; }
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
                          radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.95), transparent),
                          radial-gradient(1px 1px at 90px 40px, #aaddff, transparent);
        background-size: 500px 300px; background-repeat: repeat; opacity: 0.7; z-index: 0; pointer-events: none;
    }
    .stApp::after {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 20% 30%, rgba(0,200,255,0.12) 0%, transparent 50%),
                    radial-gradient(circle at 80% 70%, rgba(140,60,255,0.10) 0%, transparent 55%);
        z-index: 0; pointer-events: none;
    }
    .main .block-container { position: relative; z-index: 1; }
    h1, h2, h3 { color: #00f0ff !important; }
    .stApp, p, span, div, label { color: #ffffff !important; }
    .stNumberInput input { background-color: #0f2344 !important; color: #ffffff !important; }
    section[data-testid="stSidebar"] { background: #05080f !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("🗺️ Maidenhead Grid Square Tools")

st.subheader("Lat/Long → Grid Square")
lat = st.number_input("Latitude", -90.0, 90.0, 41.7, 0.0001)
lon = st.number_input("Longitude", -180.0, 180.0, -72.7, 0.0001)

def latlon_to_grid(lat, lon):
    lon += 180
    lat += 90
    grid = chr(ord('A') + int(lon / 20))
    grid += chr(ord('A') + int(lat / 10))
    grid += str(int((lon % 20) / 2))
    grid += str(int(lat % 10))
    grid += chr(ord('a') + int((lon % 2) * 12))
    grid += chr(ord('a') + int((lat % 1) * 24))
    return grid

if st.button("Calculate Grid"):
    st.success(f"**Grid Square:** `{latlon_to_grid(lat, lon)}`")

st.markdown("---")
st.subheader("Distance Between Two Grids (approx)")
grid1 = st.text_input("Grid 1", "FN31")
grid2 = st.text_input("Grid 2", "EM48")
st.caption("Simple approximation only – for precise distance use a proper calculator.")