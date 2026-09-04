import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Go-Kit Checklist", page_icon="🎒", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { 
        background-color: #05080f !important; 
        color: #ffffff; 
    }
    [data-testid="stAppViewContainer"], .main { 
        background: transparent !important; 
    }

    /* Stars */
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
                          radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.95), transparent),
                          radial-gradient(1px 1px at 90px 40px, #aaddff, transparent),
                          radial-gradient(1.5px 1.5px at 160px 120px, #ffffff, transparent);
        background-size: 500px 300px; 
        background-repeat: repeat; 
        opacity: 0.7; 
        z-index: 0; 
        pointer-events: none;
    }

    /* Nebula glow */
    .stApp::after {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 20% 30%, rgba(0,200,255,0.12) 0%, transparent 50%),
                    radial-gradient(circle at 80% 70%, rgba(140,60,255,0.10) 0%, transparent 55%);
        z-index: 0; 
        pointer-events: none;
    }

    .main .block-container { position: relative; z-index: 1; }

    h1, h2, h3 { 
        color: #00f0ff !important; 
        text-shadow: 0 0 12px rgba(0,240,255,0.5); 
    }
    .stApp, p, span, div, label { 
        color: #ffffff !important; 
    }

    /* Checkbox styling */
    .stCheckbox label {
        color: #ffffff !important;
        font-size: 1.05rem;
    }

    section[data-testid="stSidebar"] { 
        background: #05080f !important; 
        border-right: 2px solid #00f0ff33; 
    }
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
st.checkbox("External speaker")

st.subheader("Power & Accessories")
st.checkbox("12V battery / LiFePO4")
st.checkbox("Solar panel + charge controller")
st.checkbox("Anderson Powerpole connectors")
st.checkbox("Multimeter")
st.checkbox("Fuses and spare fuses")
st.checkbox("Power distribution block")

st.subheader("Documentation & Personal")
st.checkbox("Printed band plan + frequency list")
st.checkbox("ICS forms (205, 213, 214)")
st.checkbox("Notebook + pens / permanent markers")
st.checkbox("Headlamp / flashlight + extra batteries")
st.checkbox("First aid kit")
st.checkbox("Water + snacks")
st.checkbox("License copy + photo ID")
st.checkbox("Cash / small bills")
st.checkbox("Rain gear / jacket")

st.success("Check items off as you pack them. Stay prepared!")