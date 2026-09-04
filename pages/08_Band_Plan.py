import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Band Plan", page_icon="📋", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main { background: transparent !important; }

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

    h1, h2, h3 { color: #00f0ff !important; text-shadow: 0 0 12px rgba(0,240,255,0.5); }
    .stApp, p, span, div, label, .stMarkdown { color: #ffffff !important; }

    /* TABLES - black text */
    table, th, td, .stMarkdown table, .stMarkdown th, .stMarkdown td {
        color: #000000 !important;
        background-color: #f0f4f8 !important;
    }

    section[data-testid="stSidebar"] { background: #05080f !important; border-right: 2px solid #00f0ff33; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("📋 US Amateur Radio Band Plan")

license_class = st.radio("Select License Class", ["Technician", "General", "Amateur Extra"], horizontal=True)

if license_class == "Technician":
    st.subheader("Technician Class Privileges")
    st.markdown("""
    | Band | Frequency (MHz) | Modes Allowed |
    |------|------------------|---------------|
    | 80 m | 3.525 – 3.600 | CW only |
    | 40 m | 7.025 – 7.125 | CW only |
    | 15 m | 21.025 – 21.200 | CW only |
    | 10 m | 28.000 – 28.300 | CW, RTTY/Data |
    | 10 m | 28.300 – 28.500 | CW, Phone |
    | 6 m  | 50.0 – 54.0 | All modes |
    | 2 m  | 144.0 – 148.0 | All modes |
    | 1.25 m | 222.0 – 225.0 | All modes |
    | 70 cm | 420.0 – 450.0 | All modes |
    | 33 cm | 902 – 928 | All modes |
    | 23 cm | 1240 – 1300 | All modes |
    """)
elif license_class == "General":
    st.subheader("General Class Privileges (includes Technician +)")
    st.markdown("""
    | Band | Frequency (MHz) | Notes |
    |------|------------------|-------|
    | 160 m | 1.800 – 2.000 | All modes |
    | 80 m | 3.525 – 3.600 | CW |
    | 80 m | 3.800 – 4.000 | Phone |
    | 40 m | 7.025 – 7.125 | CW |
    | 40 m | 7.175 – 7.300 | Phone |
    | 20 m | 14.025 – 14.150 | CW/Data |
    | 20 m | 14.225 – 14.350 | Phone |
    | 15 m | 21.025 – 21.200 | CW/Data |
    | 15 m | 21.275 – 21.450 | Phone |
    | 10 m | 28.000 – 29.700 | All modes |
    + All Technician VHF/UHF privileges
    """)
else:
    st.subheader("Amateur Extra Class – Full Privileges")
    st.markdown("""
    Extra class operators have access to **all** amateur frequencies and modes authorized by the FCC.
    
    Key additional segments:
    - 80 m: 3.500 – 3.525 (CW)
    - 40 m: 7.000 – 7.025 (CW)
    - 20 m: 14.000 – 14.025 (CW)
    - 15 m: 21.000 – 21.025 (CW)
    - Full access to all HF, VHF, UHF, and microwave bands.
    """)

st.info("Always check the latest FCC rules and ARRL band plan for updates.")