import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import math
import random

# -----------------------------------------------------------------------------
# Page Config
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Ham Radio Portal",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# Custom CSS - Mobile-first dark-friendly theme
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #a0aec0;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid #4a5568;
    }
    .stMetric {
        background-color: #1a202c;
        border-radius: 8px;
        padding: 10px;
    }
    div[data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
    }
    .success-box {
        background-color: #064e3b;
        border-left: 5px solid #10b981;
        padding: 12px;
        border-radius: 6px;
        margin: 8px 0;
    }
    .warning-box {
        background-color: #7c2d12;
        border-left: 5px solid #f97316;
        padding: 12px;
        border-radius: 6px;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Utility Functions
# -----------------------------------------------------------------------------
@st.cache_data(ttl=300)  # Cache 5 minutes
def fetch_solar_indices():
    """Fetch current solar / geomagnetic indices from NOAA SWPC."""
    try:
        # Planetary K-index (1-minute)
        k_url = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
        k_data = requests.get(k_url, timeout=8).json()
        latest_k = k_data[-1] if k_data else {}

        # Solar flux & more comprehensive data
        flux_url = "https://services.swpc.noaa.gov/json/f107_cm_flux.json"
        flux_data = requests.get(flux_url, timeout=8).json()
        latest_flux = flux_data[-1] if flux_data else {}

        # Daily solar indices (A-index etc.)
        daily_url = "https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json"
        daily = requests.get(daily_url, timeout=8).json()
        latest_daily = daily[-1] if daily else {}

        return {
            "k_index": latest_k.get("kp_index", "N/A"),
            "k_time": latest_k.get("time_tag", "N/A"),
            "sfi": latest_flux.get("flux", latest_daily.get("f10.7", "N/A")),
            "a_index": latest_daily.get("a_index", "N/A"),
            "ssn": latest_daily.get("ssn", "N/A"),
            "raw_k": k_data[-48:] if k_data else [],  # last ~48 min for chart
        }
    except Exception as e:
        return {
            "k_index": "—",
            "k_time": str(e)[:40],
            "sfi": "—",
            "a_index": "—",
            "ssn": "—",
            "raw_k": [],
            "error": str(e),
        }

@st.cache_data(ttl=600)
def lookup_callsign(call: str):
    """US callsign lookup via callook.info (free, no key)."""
    call = call.strip().upper()
    if not call:
        return None
    try:
        r = requests.get(f"https://callook.info/{call}/json", timeout=6)
        if r.status_code == 200:
            return r.json()
        return None
    except Exception:
        return None

def dipole_length_ft(freq_mhz: float) -> float:
    """Half-wave dipole length in feet (468 / f)."""
    return 468.0 / freq_mhz if freq_mhz > 0 else 0

def yagi_boom_estimate(freq_mhz: float, elements: int = 3) -> dict:
    """Very rough Yagi element spacing estimates."""
    wavelength_m = 300.0 / freq_mhz
    return {
        "reflector": round(wavelength_m * 0.5 * 3.28084, 2),  # ~0.5λ in feet
        "driven": round(wavelength_m * 0.47 * 3.28084, 2),
        "director": round(wavelength_m * 0.45 * 3.28084, 2),
        "boom_approx_ft": round(wavelength_m * 0.3 * (elements - 1) * 3.28084, 2),
    }

def coax_loss_db(freq_mhz: float, length_ft: float, loss_per_100ft: float) -> float:
    """Simple coax loss calculation."""
    return (loss_per_100ft / 100.0) * length_ft * math.sqrt(freq_mhz / 100.0)  # rough freq scaling

# Sample data (replace with live feeds / DB in production)
SAMPLE_REPEATERS = [
    {"Call": "W1AW", "Freq": "146.640", "Offset": "-0.600", "Tone": "88.5", "Mode": "FM", "City": "Newington, CT", "Status": "Active"},
    {"Call": "K1CT", "Freq": "147.150", "Offset": "+0.600", "Tone": "100.0", "Mode": "FM", "City": "Hartford, CT", "Status": "Active"},
    {"Call": "N1D", "Freq": "442.100", "Offset": "+5.000", "Tone": "110.9", "Mode": "FM", "City": "New Haven, CT", "Status": "Active"},
    {"Call": "W1ORH", "Freq": "145.450", "Offset": "-0.600", "Tone": "77.0", "Mode": "FM", "City": "Oxford, CT", "Status": "Active"},
    {"Call": "KB1AEV", "Freq": "146.730", "Offset": "-0.600", "Tone": "88.5", "Mode": "FM", "City": "Vernon, CT", "Status": "Active"},
    {"Call": "W1STR", "Freq": "447.525", "Offset": "-5.000", "Tone": "100.0", "Mode": "Fusion", "City": "Stamford, CT", "Status": "Active"},
]

SAMPLE_DX = [
    {"Spotter": "K1ABC", "DX": "P5DX", "Freq": "14.205", "Mode": "SSB", "Time": "14:32Z", "Note": "North Korea rare!"},
    {"Spotter": "W3LPL", "DX": "FT8WW", "Freq": "21.074", "Mode": "FT8", "Time": "14:28Z", "Note": "Crozet"},
    {"Spotter": "N7QXQ", "DX": "3Y0J", "Freq": "7.074", "Mode": "FT8", "Time": "14:15Z", "Note": "Bouvet"},
    {"Spotter": "K9CT", "DX": "VU4T", "Freq": "28.445", "Mode": "SSB", "Time": "14:05Z", "Note": "Andaman"},
    {"Spotter": "W1AW", "DX": "ZL1AA", "Freq": "14.220", "Mode": "SSB", "Time": "13:58Z", "Note": "New Zealand"},
]

SAMPLE_POTA = [
    {"Park": "US-0065", "Name": "Acadia NP", "Activator": "K1ABC", "Freq": "14.285", "Mode": "SSB", "Spots": 12},
    {"Park": "US-0015", "Name": "Yellowstone NP", "Activator": "W7XYZ", "Freq": "7.190", "Mode": "SSB", "Spots": 8},
    {"Park": "US-0041", "Name": "Great Smoky Mtns", "Activator": "N4ABC", "Freq": "14.074", "Mode": "FT8", "Spots": 22},
    {"Park": "US-0078", "Name": "Shenandoah NP", "Activator": "K4DEF", "Freq": "21.300", "Mode": "SSB", "Spots": 5},
]

SAMPLE_NETS = [
    {"Net": "ARES Statewide", "Day": "Sunday", "Time": "20:00 local", "Freq": "146.640", "Tone": "88.5", "NCS": "W1XYZ"},
    {"Net": "RACES Training", "Day": "Wednesday", "Time": "19:30 local", "Freq": "147.150", "Tone": "100.0", "NCS": "K1ABC"},
    {"Net": "Club 2m Net", "Day": "Thursday", "Time": "20:00 local", "Freq": "145.450", "Tone": "77.0", "NCS": "N1DEF"},
    {"Net": "HF Traffic Net", "Day": "Daily", "Time": "18:00 local", "Freq": "3.958", "Tone": "—", "NCS": "W1AW"},
]

SAMPLE_EVENTS = [
    {"Date": "2026-09-12", "Event": "VE License Exam Session", "Location": "Club Hall", "Notes": "All classes"},
    {"Date": "2026-09-19", "Event": "Monthly Club Meeting", "Location": "Community Center", "Notes": "Guest speaker: antennas"},
    {"Date": "2026-10-03", "Event": "Fall Hamfest", "Location": "Fairgrounds", "Notes": "Tables available"},
    {"Date": "2026-10-11", "Event": "ARES Simulated Emergency Test", "Location": "County EOC", "Notes": "Full activation"},
]

# Technician sample questions (real-style, abbreviated)
TECH_QUESTIONS = [
    {
        "q": "What is the ITU phonetic alphabet word for the letter 'B'?",
        "choices": ["Baker", "Bravo", "Boston", "Beta"],
        "answer": 1,
    },
    {
        "q": "What is the maximum power output permitted on the 70 cm band for Technician class?",
        "choices": ["50 watts", "200 watts", "1500 watts", "25 watts"],
        "answer": 2,
    },
    {
        "q": "Which of the following is a common use of the 2-meter band?",
        "choices": ["DX on 160 m", "Local FM repeaters", "AM broadcast", "Satellite only"],
        "answer": 1,
    },
    {
        "q": "What does CTCSS stand for?",
        "choices": ["Continuous Tone-Coded Squelch System", "Carrier Tone Control Signal System",
                    "Coded Transmission Control Sub-System", "Continuous Transmission Carrier Signal"],
        "answer": 0,
    },
    {
        "q": "What is the approximate length of a half-wave dipole for 146 MHz?",
        "choices": ["19 inches", "38 inches", "6 feet", "3 feet"],
        "answer": 1,
    },
]

# -----------------------------------------------------------------------------
# Sidebar Navigation
# -----------------------------------------------------------------------------
st.sidebar.markdown("## 📡 Ham Radio Portal")
st.sidebar.caption("Modern tools for operators & clubs")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home / Overview",
        "☀️ Space Weather & Propagation",
        "📡 DX / POTA / APRS Activity",
        "📶 Repeaters & Digital Modes",
        "🪪 Callsign & License Tools",
        "🚨 Emergency Comms & Club",
        "🔧 Calculators & Technical",
    ],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Mobile-friendly • Real-time NOAA data • "
    "Replace sample data with live DX cluster / RepeaterBook / POTA APIs in production."
)

# -----------------------------------------------------------------------------
# PAGE: Home
# -----------------------------------------------------------------------------
if page == "🏠 Home / Overview":
    st.markdown('<p class="main-header">📡 Ham Radio Portal</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Real-time tools for operators, students & clubs</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    solar = fetch_solar_indices()

    with col1:
        st.metric("Solar Flux (SFI)", solar.get("sfi", "—"), help="10.7 cm solar flux")
    with col2:
        st.metric("K-Index", solar.get("k_index", "—"), help="Geomagnetic activity (0-9)")
    with col3:
        st.metric("A-Index", solar.get("a_index", "—"))
    with col4:
        st.metric("Sunspot Number", solar.get("ssn", "—"))

    st.markdown("---")
    st.subheader("Quick Links")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Operations**")
        st.write("- Live DX Cluster spots")
        st.write("- POTA / SOTA activators")
        st.write("- Local repeater directory")
    with c2:
        st.markdown("**Learning**")
        st.write("- Callsign lookup (FCC)")
        st.write("- Practice exam questions")
        st.write("- Band plan reference")
    with c3:
        st.markdown("**Club & EmComm**")
        st.write("- ARES / RACES nets")
        st.write("- Club calendar")
        st.write("- Antenna & coax calculators")

    st.markdown("---")
    st.info(
        "💡 **Tip**: This portal is designed mobile-first. "
        "Key reference pages can be bookmarked or added to your home screen for quick field access. "
        "For true offline/PWA support, wrap with a service worker or use Streamlit sharing + browser cache."
    )

# -----------------------------------------------------------------------------
# PAGE: Space Weather & Propagation
# -----------------------------------------------------------------------------
elif page == "☀️ Space Weather & Propagation":
    st.markdown('<p class="main-header">☀️ Space Weather & Propagation</p>', unsafe_allow_html=True)
    st.caption("Data from NOAA Space Weather Prediction Center (SWPC)")

    solar = fetch_solar_indices()

    if "error" in solar:
        st.warning(f"Could not refresh live data: {solar['error']}. Showing last known / placeholders.")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Solar Flux Index (SFI)", solar.get("sfi", "—"))
    m2.metric("Planetary K-Index", solar.get("k_index", "—"))
    m3.metric("A-Index", solar.get("a_index", "—"))
    m4.metric("Sunspot Number", solar.get("ssn", "—"))

    st.markdown(f"**Last K-index update:** `{solar.get('k_time', 'N/A')}`")

    # Simple K-index trend
    if solar.get("raw_k"):
        df_k = pd.DataFrame(solar["raw_k"])
        if "kp_index" in df_k.columns and "time_tag" in df_k.columns:
            fig = px.line(df_k, x="time_tag", y="kp_index", title="Recent Planetary K-Index",
                          labels={"kp_index": "Kp", "time_tag": "Time (UTC)"})
            fig.update_layout(height=320, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Band Condition Guidance (rule-of-thumb)")

    try:
        k = float(solar.get("k_index", 3))
    except (TypeError, ValueError):
        k = 3.0

    if k <= 2:
        st.markdown('<div class="success-box">🟢 Quiet geomagnetic conditions — good for HF DX, especially higher bands.</div>', unsafe_allow_html=True)
    elif k <= 4:
        st.markdown('<div class="warning-box">🟡 Unsettled — mid-latitude paths may be noisy; lower bands still usable.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="warning-box">🔴 Storm levels — expect absorption and blackouts on polar / high-latitude paths.</div>', unsafe_allow_html=True)

    st.markdown("""
    **Quick propagation notes**
    - High SFI (>150) → 10 m / 12 m / 15 m open more often
    - Low K + high SFI → classic “DX weather”
    - Night-time → 40 m / 80 m long-path openings
    """)

    st.subheader("External Propagation Tools")
    st.markdown("""
    - [VOACAP Online](https://www.voacap.com/hf/) – point-to-point HF prediction  
    - [PropView / HamCAP](https://www.dxatlas.com/) – desktop prediction  
    - [NOAA SWPC Dashboard](https://www.swpc.noaa.gov/)  
    - [KC2G MUF Map](https://prop.kc2g.com/) – real-time MUF  
    """)

# -----------------------------------------------------------------------------
# PAGE: DX / POTA / APRS
# -----------------------------------------------------------------------------
elif page == "📡 DX / POTA / APRS Activity":
    st.markdown('<p class="main-header">📡 Operational Activity Dashboard</p>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["DX Cluster Spots", "POTA Activators", "APRS Snapshot"])

    with tab1:
        st.subheader("Recent DX Spots (sample / demo feed)")
        st.caption("In production: connect to DX Spider, CC Cluster, or websocket feed (e.g. dxheat, reversebeacon).")
        df_dx = pd.DataFrame(SAMPLE_DX)
        st.dataframe(df_dx, use_container_width=True, hide_index=True)

        band_filter = st.multiselect("Filter by band (demo)", ["10 m", "15 m", "20 m", "40 m", "80 m"], default=["20 m", "15 m"])
        st.info("Live filtered DX cluster integration would go here (Telnet or REST).")

    with tab2:
        st.subheader("Parks on the Air – Current Activators (sample)")
        df_pota = pd.DataFrame(SAMPLE_POTA)
        st.dataframe(df_pota, use_container_width=True, hide_index=True)
        st.markdown("[Official POTA spots](https://pota.app) • [SOTA](https://sotawatch.sota.org.uk)")

    with tab3:
        st.subheader("APRS Position Snapshot (demo map)")
        st.caption("Replace with live aprs.fi API or local digipeater feed.")

        # Demo APRS points (CT area)
        aprs_df = pd.DataFrame({
            "lat": [41.76, 41.30, 41.55, 41.80, 41.65],
            "lon": [-72.67, -72.92, -72.65, -72.55, -72.80],
            "call": ["W1AW-1", "K1CT-9", "N1ABC-7", "W1STR-2", "KB1AEV-10"],
        })
        st.map(aprs_df, size=20, color="#00d4ff")
        st.dataframe(aprs_df, hide_index=True)

# -----------------------------------------------------------------------------
# PAGE: Repeaters & Digital
# -----------------------------------------------------------------------------
elif page == "📶 Repeaters & Digital Modes":
    st.markdown('<p class="main-header">📶 Repeater & Frequency Directory</p>', unsafe_allow_html=True)

    search = st.text_input("Search by call, city, or frequency", placeholder="e.g. 146.64 or Hartford")
    df_rep = pd.DataFrame(SAMPLE_REPEATERS)

    if search:
        mask = df_rep.apply(lambda row: search.lower() in str(row).lower(), axis=1)
        df_rep = df_rep[mask]

    st.dataframe(df_rep, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("Digital Modes Quick Reference")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        **DMR**
        - Color Code (CC) usually 1
        - Time Slot 1 or 2
        - Talkgroup examples: 3100 (USA), local TG
        """)
        st.markdown("""
        **Yaesu System Fusion (C4FM)**
        - DN (digital narrow) / VW (voice wide)
        - Wires-X rooms
        """)
    with col_b:
        st.markdown("""
        **D-STAR**
        - Module A/B/C
        - Reflectors (REF, XRF, DCS)
        """)
        st.markdown("""
        **EchoLink / IRLP**
        - Node numbers
        - Conference bridges
        """)

    st.info("Production tip: integrate RepeaterBook API or local CSV/JSON maintained by the club.")

# -----------------------------------------------------------------------------
# PAGE: Callsign & License Tools
# -----------------------------------------------------------------------------
elif page == "🪪 Callsign & License Tools":
    st.markdown('<p class="main-header">🪪 Callsign Lookup & License Tools</p>', unsafe_allow_html=True)

    tab_lookup, tab_exam, tab_band = st.tabs(["Callsign Lookup", "Practice Exam", "Band Plan"])

    with tab_lookup:
        call = st.text_input("Enter US callsign", placeholder="W1AW", max_chars=10)
        if st.button("Lookup", type="primary") or call:
            if call:
                with st.spinner("Querying callook.info…"):
                    data = lookup_callsign(call)
                if data and data.get("status") == "VALID":
                    st.success(f"**{data.get('current', {}).get('callsign', call)}** is valid")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write("**Name / Club**")
                        st.write(data.get("name", "—"))
                        st.write("**Class**")
                        st.write(data.get("current", {}).get("operClass", "—"))
                        st.write("**Status**")
                        st.write(data.get("status", "—"))
                    with c2:
                        loc = data.get("location", {})
                        st.write("**Location**")
                        st.write(f"{loc.get('latitude', '—')}, {loc.get('longitude', '—')}")
                        st.write("**Grid**")
                        st.write(loc.get("gridsquare", "—"))
                        st.write("**Grant Date**")
                        st.write(data.get("otherInfo", {}).get("grantDate", "—"))
                elif data:
                    st.warning(f"Status: {data.get('status', 'Unknown')}")
                else:
                    st.error("Lookup failed or callsign not found.")

    with tab_exam:
        st.subheader("Technician Class – Sample Questions")
        st.caption("These are illustrative. Use official pools from NCVEC / ARRL for real study.")

        if "exam_score" not in st.session_state:
            st.session_state.exam_score = 0
            st.session_state.exam_total = 0
            st.session_state.q_index = 0

        q = TECH_QUESTIONS[st.session_state.q_index % len(TECH_QUESTIONS)]
        st.write(f"**Q{st.session_state.q_index + 1}:** {q['q']}")
        choice = st.radio("Select answer", q["choices"], key=f"q{st.session_state.q_index}")

        if st.button("Check Answer"):
            st.session_state.exam_total += 1
            if q["choices"].index(choice) == q["answer"]:
                st.success("Correct!")
                st.session_state.exam_score += 1
            else:
                st.error(f"Incorrect. Correct answer: **{q['choices'][q['answer']]}**")

        if st.button("Next Question"):
            st.session_state.q_index += 1
            st.rerun()

        if st.session_state.exam_total > 0:
            st.metric("Score", f"{st.session_state.exam_score} / {st.session_state.exam_total}")

    with tab_band:
        st.subheader("US Amateur Band Plan (summary)")
        st.markdown("""
        | Band | Frequency Range | Notes |
        |------|-----------------|-------|
        | 160 m | 1.800–2.000 MHz | CW, SSB, digital |
        | 80 m | 3.500–4.000 MHz | CW, SSB, digital |
        | 40 m | 7.000–7.300 MHz | CW, SSB, digital |
        | 20 m | 14.000–14.350 MHz | Major DX band |
        | 15 m | 21.000–21.450 MHz | DX |
        | 10 m | 28.000–29.700 MHz | Technician phone above 28.300 |
        | 6 m | 50.000–54.000 MHz | “Magic band” |
        | 2 m | 144.000–148.000 MHz | FM repeaters, SSB weak-signal |
        | 70 cm | 420.000–450.000 MHz | FM, digital, ATV |
        """)
        st.caption("Full official band plan: ARRL or FCC Part 97. Printable PDF recommended for field use.")

# -----------------------------------------------------------------------------
# PAGE: Emergency & Club
# -----------------------------------------------------------------------------
elif page == "🚨 Emergency Comms & Club":
    st.markdown('<p class="main-header">🚨 Emergency Communications & Club Ops</p>', unsafe_allow_html=True)

    tab_nets, tab_cal, tab_ares = st.tabs(["Net Schedules", "Club Calendar", "ARES / RACES"])

    with tab_nets:
        st.subheader("Local & Statewide Nets")
        st.dataframe(pd.DataFrame(SAMPLE_NETS), use_container_width=True, hide_index=True)
        st.info("Update frequencies and NCS callsigns to match your section / county plan.")

    with tab_cal:
        st.subheader("Upcoming Club Events")
        st.dataframe(pd.DataFrame(SAMPLE_EVENTS), use_container_width=True, hide_index=True)
        st.markdown("Add ICS-205 / ICS-213 forms and net control scripts to the club repository.")

    with tab_ares:
        st.subheader("ARES / RACES Quick Reference")
        st.markdown("""
        **Typical activation levels**
        1. Monitoring only  
        2. Stand-by / check-in net  
        3. Full deployment (shelter, EOC, damage assessment)

        **Recommended go-kit items**
        - HT + mobile dual-band  
        - Extra batteries / power bank  
        - Mag-mount or roll-up J-pole  
        - Printed ICS forms + band plan  
        - Notebook, pens, headlamp  

        **Key frequencies** (customize for your area)
        - Primary 2 m repeater  
        - Simplex tactical: 146.520  
        - HF liaison: 3.958 / 7.250 LSB (region dependent)
        """)
        st.warning("Always follow your local Emergency Coordinator and served-agency protocols.")

# -----------------------------------------------------------------------------
# PAGE: Calculators & Technical
# -----------------------------------------------------------------------------
elif page == "🔧 Calculators & Technical":
    st.markdown('<p class="main-header">🔧 Technical Reference & Calculators</p>', unsafe_allow_html=True)

    calc_type = st.selectbox(
        "Choose calculator",
        ["Half-wave Dipole", "Simple Yagi Estimate", "Coax Loss", "Wavelength / Frequency"],
    )

    if calc_type == "Half-wave Dipole":
        freq = st.number_input("Frequency (MHz)", min_value=1.0, max_value=1300.0, value=14.2, step=0.01)
        length = dipole_length_ft(freq)
        each_leg = length / 2
        st.metric("Total dipole length", f"{length:.2f} ft")
        st.metric("Each leg", f"{each_leg:.2f} ft")
        st.caption("Formula: 468 / f(MHz). For inverted-V, shorten ~2–5 %.")

    elif calc_type == "Simple Yagi Estimate":
        freq = st.number_input("Frequency (MHz)", min_value=50.0, max_value=1300.0, value=146.0, step=0.1)
        elems = st.slider("Number of elements", 3, 8, 3)
        est = yagi_boom_estimate(freq, elems)
        st.write(f"**Rough element lengths (feet)** for {freq} MHz")
        st.json(est)
        st.caption("These are starting points only. Use proper Yagi design software (YO, 4nec2, EZNEC) for final dimensions.")

    elif calc_type == "Coax Loss":
        freq = st.number_input("Frequency (MHz)", min_value=1.0, max_value=1300.0, value=146.0)
        length = st.number_input("Length (feet)", min_value=1.0, value=50.0)
        cable = st.selectbox("Cable type (loss @ 100 MHz / 100 ft approx)", {
            "RG-58": 4.5,
            "RG-8X": 3.0,
            "RG-213 / LMR-400": 1.5,
            "LMR-600": 0.9,
            "1/2\" hardline": 0.5,
        })
        loss_per_100 = {
            "RG-58": 4.5,
            "RG-8X": 3.0,
            "RG-213 / LMR-400": 1.5,
            "LMR-600": 0.9,
            "1/2\" hardline": 0.5,
        }[cable]
        loss = coax_loss_db(freq, length, loss_per_100)
        st.metric("Approximate loss", f"{loss:.2f} dB")
        st.caption("Rough estimate only – check manufacturer charts for exact figures.")

    else:  # Wavelength
        freq = st.number_input("Frequency (MHz)", min_value=0.1, max_value=3000.0, value=14.2)
        wl_m = 300.0 / freq
        wl_ft = wl_m * 3.28084
        st.metric("Wavelength", f"{wl_m:.2f} m  /  {wl_ft:.2f} ft")
        st.metric("¼ wavelength", f"{wl_m/4:.2f} m  /  {wl_ft/4:.2f} ft")
        st.metric("½ wavelength", f"{wl_m/2:.2f} m  /  {wl_ft/2:.2f} ft")

    st.markdown("---")
    st.subheader("Additional Resources")
    st.markdown("""
    - [ARRL Antenna Book](https://www.arrl.org)  
    - [QSL.net antenna notes](https://www.qsl.net)  
    - [VK3CPU Antenna Calculator collection](https://www.vk3cpu.net)  
    - Local club schematic / project repository (link your GitHub or shared drive here)
    """)

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.caption(
    f"Ham Radio Portal • Data refreshed periodically from public NOAA SWPC endpoints • "
    f"Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC • "
    "For educational & operational use. Not an official FCC or ARRL product."
)