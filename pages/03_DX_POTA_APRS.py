import streamlit as st
import pandas as pd
import streamlit as st
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
st.set_page_config(page_title="DX / POTA / APRS", page_icon="📡", layout="wide")
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
    st.subheader("Recent DX Spots (sample data)")
    st.dataframe(pd.DataFrame(SAMPLE_DX), use_container_width=True, hide_index=True)
    st.info("In production: connect to a live DX cluster (DX Spider, reversebeacon, etc.)")

with tab2:
    st.subheader("Parks on the Air – Current Activators")
    st.dataframe(pd.DataFrame(SAMPLE_POTA), use_container_width=True, hide_index=True)
    st.markdown("[Official POTA](https://pota.app) • [SOTA Watch](https://sotawatch.sota.org.uk)")

with tab3:
    st.subheader("APRS Snapshot (demo)")
    aprs = pd.DataFrame({
        "lat": [41.76, 41.30, 41.55, 41.80],
        "lon": [-72.67, -72.92, -72.65, -72.55],
        "call": ["W1AW-1", "K1CT-9", "N1ABC-7", "W1STR-2"]
    })
    st.map(aprs, size=20)
    st.dataframe(aprs, hide_index=True)