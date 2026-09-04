import streamlit as st
import pandas as pd

st.set_page_config(page_title="Repeaters", page_icon="📶", layout="wide")
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
col1, col2 = st.columns(2)
with col1:
    st.markdown("**DMR**  \nColor Code usually 1  \nTime Slot 1 or 2")
    st.markdown("**Yaesu System Fusion**  \nDN / VW modes  \nWires-X rooms")
with col2:
    st.markdown("**D-STAR**  \nModules A/B/C  \nReflectors REF/XRF/DCS")
    st.markdown("**EchoLink / IRLP**  \nNode numbers")