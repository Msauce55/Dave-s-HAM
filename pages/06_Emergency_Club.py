import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Emergency & Club", page_icon="🚨", layout="wide")
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
    """)
    st.warning("Follow your local Emergency Coordinator and served agency protocols.")