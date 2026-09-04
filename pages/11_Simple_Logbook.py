import streamlit as st
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Simple Logbook", page_icon="📒", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], .main { background: transparent !important; }

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
    .stApp, p, span, div, label { color: #ffffff !important; }

    .stTextInput input, .stNumberInput input {
        background-color: #0f2344 !important;
        color: #ffffff !important;
        border: 1px solid #00f0ff66 !important;
    }

    .stButton > button {
        background: linear-gradient(90deg, #00d4ff, #0099cc) !important;
        color: #03101f !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff8c00, #ffaa00) !important;
        color: white !important;
    }

    section[data-testid="stSidebar"] { background: #05080f !important; border-right: 2px solid #00f0ff33; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("📒 Simple QSO Logbook")

if "logbook" not in st.session_state:
    st.session_state.logbook = []

with st.form("log_form", clear_on_submit=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        call = st.text_input("Callsign")
        freq = st.text_input("Frequency (MHz)")
    with c2:
        mode = st.radio("Mode", ["SSB", "CW", "FT8", "FM", "AM", "Other"], horizontal=True)
        rst_sent = st.text_input("RST Sent", "59")
    with c3:
        rst_rcvd = st.text_input("RST Received", "59")
        notes = st.text_input("Notes")

    if st.form_submit_button("Add QSO", type="primary"):
        if call:
            st.session_state.logbook.insert(0, {
                "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M"),
                "call": call.upper(),
                "freq": freq,
                "mode": mode,
                "rst_s": rst_sent,
                "rst_r": rst_rcvd,
                "notes": notes
            })
            st.success("QSO logged!")

st.subheader("Recent QSOs")
if st.session_state.logbook:
    for qso in st.session_state.logbook:
        st.write(f"**{qso['time']}Z** | **{qso['call']}** | {qso['freq']} MHz | {qso['mode']} | {qso['rst_s']}/{qso['rst_r']} | {qso['notes']}")
else:
    st.info("No QSOs logged yet.")