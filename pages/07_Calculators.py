import streamlit as st
import math

st.set_page_config(page_title="Calculators", page_icon="🔧", layout="wide")
st.title("🔧 Technical Calculators")

calc = st.selectbox("Select calculator", [
    "Half-wave Dipole",
    "Simple Yagi Estimate",
    "Coax Loss",
    "Wavelength"
])

if calc == "Half-wave Dipole":
    freq = st.number_input("Frequency (MHz)", 1.0, 1300.0, 14.2, 0.01)
    length = 468 / freq
    st.metric("Total length", f"{length:.2f} ft")
    st.metric("Each leg", f"{length/2:.2f} ft")
    st.caption("Formula: 468 / f (MHz). Shorten 2–5% for inverted-V.")

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