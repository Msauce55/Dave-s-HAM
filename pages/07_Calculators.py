import streamlit as st
import math
from pathlib import Path

st.set_page_config(page_title="Calculators", page_icon="🔧", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], .main { background: transparent !important; }
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
                          radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.9), transparent),
                          radial-gradient(1px 1px at 90px 40px, #aaddff, transparent);
        background-size: 500px 300px; background-repeat: repeat; opacity: 0.7; z-index: 0; pointer-events: none;
    }
    .main .block-container { position: relative; z-index: 1; }
    h1, h2, h3 { color: #00f0ff !important; }
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
    section[data-testid="stSidebar"] { background: #05080f !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("🔧 Technical Calculators")

calc = st.radio(
    "Select calculator",
    ["Half-wave Dipole", "Simple Yagi Estimate", "Coax Loss", "Wavelength"],
    horizontal=True
)

st.markdown("---")

if calc == "Half-wave Dipole":
    freq = st.number_input("Frequency (MHz)", 1.0, 1300.0, 14.2, 0.01)
    length = 468 / freq
    st.metric("Total length", f"{length:.2f} ft")
    st.metric("Each leg", f"{length/2:.2f} ft")
    st.caption("Formula: 468 / f (MHz)")

elif calc == "Simple Yagi Estimate":
    freq = st.number_input("Frequency (MHz)", 50.0, 1300.0, 146.0)
    elems = st.slider("Number of elements", 3, 8, 3)
    wl = 300 / freq
    st.write(f"**Approximate lengths for {freq} MHz:**")
    st.write(f"- Reflector: **{round(wl * 0.5 * 3.28084, 2)} ft**")
    st.write(f"- Driven element: **{round(wl * 0.47 * 3.28084, 2)} ft**")
    st.write(f"- Director: **{round(wl * 0.45 * 3.28084, 2)} ft**")
    st.write(f"- Boom (approx): **{round(wl * 0.3 * (elems-1) * 3.28084, 2)} ft**")

elif calc == "Coax Loss":
    freq = st.number_input("Frequency (MHz)", 1.0, 1300.0, 146.0)
    length = st.number_input("Length (feet)", 1.0, 500.0, 50.0)
    cable = st.radio("Cable type", ["RG-58", "RG-8X", "RG-213 / LMR-400", "LMR-600"], horizontal=True)
    loss100 = {"RG-58": 4.5, "RG-8X": 3.0, "RG-213 / LMR-400": 1.5, "LMR-600": 0.9}[cable]
    loss = (loss100 / 100) * length * math.sqrt(freq / 100)
    st.metric("Approximate loss", f"{loss:.2f} dB")

else:
    freq = st.number_input("Frequency (MHz)", 0.1, 3000.0, 14.2)
    wl_m = 300 / freq
    st.metric("Full wavelength", f"{wl_m:.2f} m  ({wl_m*3.28084:.2f} ft)")
    st.metric("½ wavelength", f"{wl_m/2:.2f} m")
    st.metric("¼ wavelength", f"{wl_m/4:.2f} m")