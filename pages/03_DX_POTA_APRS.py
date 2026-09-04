import streamlit as st
import pandas as pd

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