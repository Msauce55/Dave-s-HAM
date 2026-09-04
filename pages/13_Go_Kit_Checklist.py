import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Go-Kit Checklist", page_icon="🎒", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], .main { background: transparent !important; }
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
                          radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.95), transparent);
        background-size: 500px 300px; background-repeat: repeat; opacity: 0.7; z-index: 0; pointer-events: none;
    }
    .main .block-container { position: relative; z-index: 1; }
    h1, h2, h3 { color: #00f0ff !important; }
    .stApp, p, span, div, label { color: #ffffff !important; }
    section[data-testid="stSidebar"] { background: #05080f !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("🎒 Emergency & Portable Go-Kit Checklist")

st.subheader("Radio Equipment")
st.checkbox("Dual-band HT + speaker mic")
st.checkbox("Mobile radio + power leads")
st.checkbox("Extra batteries / power bank")
st.checkbox("Mag-mount or roll-up J-pole antenna")
st.checkbox("Coax adapters (PL-259, SMA, BNC)")

st.subheader("Power & Accessories")
st.checkbox("12V battery / LiFePO4")
st.checkbox("Solar panel + charge controller")
st.checkbox("Anderson Powerpole connectors")
st.checkbox("Multimeter")

st.subheader("Documentation & Personal")
st.checkbox("Printed band plan + frequency list")
st.checkbox("ICS forms (205, 213, 214)")
st.checkbox("Notebook + pens")
st.checkbox("Headlamp / flashlight")
st.checkbox("First aid kit")
st.checkbox("Water + snacks")
st.checkbox("License copy + ID")

st.success("Check items off as you pack. Stay prepared!")