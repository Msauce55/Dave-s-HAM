import streamlit as st
import pandas as pd

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