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
st.set_page_config(page_title="Emergency & Club", page_icon="🚨", layout="wide")
st.title("🚨 Emergency Communications & Club Ops")

tab1, tab2, tab3 = st.tabs(["Net Schedules", "Club Calendar", "ARES / RACES"])

with tab1:
    nets = [
        {"Net": "ARES Statewide", "Day": "Sunday", "Time": "20:00 local", "Freq": "146.640", "Tone": "88.5"},
        {"Net": "RACES Training", "Day": "Wednesday", "Time": "19:30 local", "Freq": "147.150", "Tone": "100.0"},
        {"Net": "Club 2m Net", "Day": "Thursday", "Time": "20:00 local", "Freq": "145.450", "Tone": "77.0"},
    ]
    st.dataframe(pd.DataFrame(nets), use_container_width=True, hide_index=True)

with tab2:
    events = [
        {"Date": "2026-09-12", "Event": "VE License Exam", "Location": "Club Hall"},
        {"Date": "2026-09-19", "Event": "Monthly Club Meeting", "Location": "Community Center"},
        {"Date": "2026-10-03", "Event": "Fall Hamfest", "Location": "Fairgrounds"},
        {"Date": "2026-10-11", "Event": "ARES SET", "Location": "County EOC"},
    ]
    st.dataframe(pd.DataFrame(events), use_container_width=True, hide_index=True)

with tab3:
    st.markdown("""
    ### ARES / RACES Quick Reference
    **Activation Levels**
    1. Monitoring only  
    2. Stand-by / check-in net  
    3. Full deployment

    **Go-kit essentials**
    - Dual-band HT + mobile
    - Extra batteries / power bank
    - Mag-mount or roll-up antenna
    - Printed ICS forms + band plan
    - Headlamp, notepad, pens

    **Common tactical frequencies**
    - 146.520 simplex
    - Your primary 2 m repeater
    """)
    st.warning("Follow your local Emergency Coordinator and served agency protocols.")