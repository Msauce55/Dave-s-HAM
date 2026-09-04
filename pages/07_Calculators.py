import streamlit as st
import math
from pathlib import Path

st.set_page_config(page_title="Calculators", page_icon="🔧", layout="wide")
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
st.title("🔧 Technical Calculators")

calc = st.selectbox("Select calculator", ["Half-wave Dipole", "Simple Yagi Estimate", "Coax Loss", "Wavelength"])

if calc == "Half-wave Dipole":
    freq = st.number_input("Frequency (MHz)", 1.0, 1300.0, 14.2, 0.01)
    length = 468 / freq
    st.metric("Total length", f"{length:.2f} ft")
    st.metric("Each leg", f"{length/2:.2f} ft")
    st.caption("Formula: 468 / f (MHz)")

elif calc == "Simple Yagi Estimate":
    freq = st.number_input("Frequency (MHz)", 50.0, 1300.0, 146.0)
    elems = st.slider("Elements", 3, 8, 3)
    wl = 300 / freq
    st.write(f"**Rough lengths in feet for {freq} MHz**")
    st.json({
        "Reflector": round(wl * 0.5 * 3.28084, 2),
        "Driven": round(wl * 0.47 * 3.28084, 2),
        "Director": round(wl * 0.45 * 3.28084, 2),
        "Boom approx": round(wl * 0.3 * (elems-1) * 3.28084, 2)
    })

elif calc == "Coax Loss":
    freq = st.number_input("Frequency (MHz)", 1.0, 1300.0, 146.0)
    length = st.number_input("Length (ft)", 1.0, 500.0, 50.0)
    cable = st.selectbox("Cable", ["RG-58", "RG-8X", "RG-213 / LMR-400", "LMR-600"])
    loss100 = {"RG-58": 4.5, "RG-8X": 3.0, "RG-213 / LMR-400": 1.5, "LMR-600": 0.9}[cable]
    loss = (loss100 / 100) * length * math.sqrt(freq / 100)
    st.metric("Approx loss", f"{loss:.2f} dB")

else:
    freq = st.number_input("Frequency (MHz)", 0.1, 3000.0, 14.2)
    wl_m = 300 / freq
    st.metric("Full wavelength", f"{wl_m:.2f} m / {wl_m*3.28084:.2f} ft")
    st.metric("½ wavelength", f"{wl_m/2:.2f} m / {wl_m*3.28084/2:.2f} ft")
    st.metric("¼ wavelength", f"{wl_m/4:.2f} m / {wl_m*3.28084/4:.2f} ft")