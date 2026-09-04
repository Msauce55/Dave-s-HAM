import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Repeaters", page_icon="📶", layout="wide")
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
    h1, h2, h3 { color: #00f0ff !important; }
    .stApp, p, span, div, label { color: #ffffff !important; }
    [data-testid="stDataFrame"], [data-testid="stDataFrame"] *, table, th, td { color: #000000 !important; }
    section[data-testid="stSidebar"] { background: #05080f !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("📶 Repeater & Digital Modes Directory")

SAMPLE = [
    {"Call": "W1AW", "Freq": "146.640", "Offset": "-0.600", "Tone": "88.5", "Mode": "FM", "City": "Newington, CT"},
    {"Call": "K1CT", "Freq": "147.150", "Offset": "+0.600", "Tone": "100.0", "Mode": "FM", "City": "Hartford, CT"},
    {"Call": "N1D", "Freq": "442.100", "Offset": "+5.000", "Tone": "110.9", "Mode": "FM", "City": "New Haven, CT"},
    {"Call": "W1ORH", "Freq": "145.450", "Offset": "-0.600", "Tone": "77.0", "Mode": "FM", "City": "Oxford, CT"},
    {"Call": "W1STR", "Freq": "447.525", "Offset": "-5.000", "Tone": "100.0", "Mode": "Fusion", "City": "Stamford, CT"},
]
search = st.text_input("Search by call, city or frequency")
df = pd.DataFrame(SAMPLE)
if search:
    df = df[df.apply(lambda r: search.lower() in str(r).lower(), axis=1)]
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Digital Modes Quick Reference")
c1, c2 = st.columns(2)
with c1:
    st.markdown("**DMR**  \nColor Code usually 1  \nTime Slot 1 or 2")
with c2:
    st.markdown("**D-STAR / Fusion / EchoLink**  \nCommon digital modes")