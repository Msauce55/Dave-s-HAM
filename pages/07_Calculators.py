import streamlit as st
import math
import streamlit as st
from pathlib import Path

# ---------- Page Config ----------
st.set_page_config(
    page_title="Dave's Ham",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Logo + Theme Colors (from the emblem) ----------
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    /* Main background - deep navy from the logo */
    .stApp {
        background: linear-gradient(180deg, #0a1628 0%, #0d1f3c 50%, #0a1628 100%);
        color: #e0f7ff;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #07101f 0%, #0d1f3c 100%);
        border-right: 1px solid #00c4ff33;
    }

    /* Headers */
    h1, h2, h3 {
        color: #00c4ff !important;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background: #13233f;
        border: 1px solid #00c4ff44;
        border-radius: 12px;
        padding: 12px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #00c4ff, #0090cc);
        color: #0a1628;
        font-weight: 700;
        border: none;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff6b00, #ff8c00);
        color: white;
    }

    /* Forms & inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox, .stNumberInput {
        background-color: #13233f !important;
        color: #e0f7ff !important;
        border: 1px solid #00c4ff55 !important;
    }

    /* Dataframes */
    .stDataFrame {
        background-color: #0d1f3c;
    }

    /* Success / Warning boxes */
    .stSuccess {
        background-color: #0d3320;
        border-left: 5px solid #00c4ff;
    }
    .stWarning {
        background-color: #3d2200;
        border-left: 5px solid #ff6b00;
    }

    /* Caption / secondary text */
    .stCaption, small {
        color: #7dd3fc !important;
    }

    /* Divider */
    hr {
        border-color: #00c4ff33;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Logo Header ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), use_container_width=True)
    else:
        st.markdown("### 📡 Dave's Ham Amateur Radio")
        st.caption("Logo not found – place it in assets/daves_ham_logo.png")

st.markdown("<br>", unsafe_allow_html=True)
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