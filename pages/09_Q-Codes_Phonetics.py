import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Q-Codes & Phonetics", page_icon="🔤", layout="wide")
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
st.title("🔤 Q-Codes, Phonetics & Prosigns")

tab1, tab2, tab3 = st.tabs(["Common Q-Codes", "ITU Phonetics", "RST & Prosigns"])

with tab1:
    st.subheader("Most Used Q-Codes")
    st.markdown("""
    | Code | Meaning |
    |------|--------|
    | QTH  | My location is... / What is your location? |
    | QRZ  | Who is calling me? |
    | QSL  | I acknowledge / Can you acknowledge? |
    | QRT  | I am stopping transmission |
    | QSY  | Change frequency |
    | QRM  | Man-made interference |
    | QRN  | Natural noise / static |
    | QSB  | Fading signal |
    | QRP  | Low power |
    | QRO  | High power |
    | QRX  | Wait a moment |
    | QRV  | I am ready |
    | QSO  | A contact |
    | QX  | I am busy |
    """)

with tab2:
    st.subheader("ITU Phonetic Alphabet")
    st.markdown("""
    A - Alpha  
    B - Bravo  
    C - Charlie  
    D - Delta  
    E - Echo  
    F - Foxtrot  
    G - Golf  
    H - Hotel  
    I - India  
    J - Juliett  
    K - Kilo  
    L - Lima  
    M - Mike  
    N - November  
    O - Oscar  
    P - Papa  
    Q - Quebec  
    R - Romeo  
    S - Sierra  
    T - Tango  
    U - Uniform  
    V - Victor  
    W - Whiskey  
    X - X-ray  
    Y - Yankee  
    Z - Zulu  
    """)

with tab3:
    st.subheader("RST System & Common Prosigns")
    st.markdown("""
    **RST Report**
    - Readability (1–5)
    - Strength (1–9)
    - Tone (1–9) — CW only

    **Common Prosigns**
    - AR → End of message
    - SK → End of contact
    - BT → Break / separator
    - KN → Go ahead only
    - CL → Closing station
    """)