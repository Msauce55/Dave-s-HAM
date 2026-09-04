import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Repeaters", page_icon="📶", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background: #05080f; color: #ffffff; }
    .stApp::before {
        content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 30% 20%, rgba(0,240,255,0.12) 0%, transparent 50%),
                    radial-gradient(circle at 70% 70%, rgba(180,80,255,0.10) 0%, transparent 60%);
        z-index: -2;
    }
    .stApp::after {
        content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(#ffffff 1px, transparent 1px),
                          radial-gradient(#88ddff 1px, transparent 2px);
        background-size: 80px 80px, 160px 160px;
        opacity: 0.4; z-index: -1; pointer-events: none;
    }
    h1, h2, h3 { color: #00f0ff !important; }
    .stApp, p, span, div, label { color: #ffffff !important; }
    section[data-testid="stSidebar"] { background: #05080f; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("📶 Repeater & Digital Modes Directory")

SAMPLE_REPEATERS = [
    {"Call": "W1AW", "Freq": "146.640", "Offset": "-0.600", "Tone": "88.5", "Mode": "FM", "City": "Newington, CT", "Status": "Active"},
    {"Call": "K1CT", "Freq": "147.150", "Offset": "+0.600", "Tone": "100.0", "Mode": "FM", "City": "Hartford, CT", "Status": "Active"},
    {"Call": "N1D", "Freq": "442.100", "Offset": "+5.000", "Tone": "110.9", "Mode": "FM", "City": "New Haven, CT", "Status": "Active"},
    {"Call": "W1ORH", "Freq": "145.450", "Offset": "-0.600", "Tone": "77.0", "Mode": "FM", "City": "Oxford, CT", "Status": "Active"},
    {"Call": "W1STR", "Freq": "447.525", "Offset": "-5.000", "Tone": "100.0", "Mode": "Fusion", "City": "Stamford, CT", "Status": "Active"},
]

search = st.text_input("Search by call, city or frequency")
df = pd.DataFrame(SAMPLE_REPEATERS)
if search:
    df = df[df.apply(lambda r: search.lower() in str(r).lower(), axis=1)]

st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Digital Modes Quick Reference")
c1, c2 = st.columns(2)
with c1:
    st.markdown("**DMR**  \nColor Code usually 1  \nTime Slot 1 or 2")
    st.markdown("**Yaesu System Fusion**  \nDN / VW modes")
with c2:
    st.markdown("**D-STAR**  \nModules A/B/C")
    st.markdown("**EchoLink / IRLP**  \nNode numbers")