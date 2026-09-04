import streamlit as st
from pathlib import Path

st.set_page_config(page_title="HAM Articles", page_icon="📰", layout="wide")
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

    /* LINK BUTTONS */
    div[data-testid="stLinkButton"] > a {
        background: linear-gradient(90deg, #00d4ff, #0099cc) !important;
        color: #03101f !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        width: 100%;
    }
    div[data-testid="stLinkButton"] > a:hover {
        background: linear-gradient(90deg, #ff8c00, #ffaa00) !important;
        color: white !important;
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
st.title("📰 HAM Articles & Resources")
st.caption("Curated collection of the best amateur radio articles, news, and technical resources")

st.info("Click any button to open the resource in a new tab.")

st.header("📢 News & Current Events")
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("ARRL News", "https://www.arrl.org/news", use_container_width=True)
    st.link_button("ARRL Homepage", "https://www.arrl.org", use_container_width=True)
    st.link_button("QRZ.com", "https://www.qrz.com", use_container_width=True)
with c2:
    st.link_button("Amateur Radio Daily", "https://www.amateurradio.com", use_container_width=True)
    st.link_button("Southgate ARC News", "https://www.southgatearc.org", use_container_width=True)
    st.link_button("The Spectrum Monitor", "https://www.thespectrummonitor.com", use_container_width=True)
with c3:
    st.link_button("FCC Amateur Radio", "https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service", use_container_width=True)
    st.link_button("RSGB (UK)", "https://rsgb.org", use_container_width=True)
    st.link_button("IARU", "https://www.iaru.org", use_container_width=True)

st.header("🔧 Technical Articles & Projects")
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("ARRL Technical", "https://www.arrl.org/technical", use_container_width=True)
    st.link_button("OnAllBands", "https://www.onallbands.com", use_container_width=True)
    st.link_button("Ham Radio Workbench", "https://www.hamradioworkbench.com", use_container_width=True)
with c2:
    st.link_button("QSL.net Library", "https://www.qsl.net", use_container_width=True)
    st.link_button("eHam.net", "https://www.eham.net", use_container_width=True)
    st.link_button("VK3CPU Calculators", "https://www.vk3cpu.net", use_container_width=True)
with c3:
    st.link_button("AA5TB Notes", "https://www.aa5tb.com", use_container_width=True)
    st.link_button("W8JI Notes", "https://www.w8ji.com", use_container_width=True)
    st.link_button("K3LR Contest Station", "https://www.k3lr.com", use_container_width=True)

st.header("📡 Antenna Resources")
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("ARRL Antenna Book", "https://www.arrl.org/shop/ARRL-Antenna-Book", use_container_width=True)
    st.link_button("DX Engineering Tech", "https://www.dxengineering.com/tech-info", use_container_width=True)
with c2:
    st.link_button("Hexbeam Info", "https://www.hexbeam.com", use_container_width=True)
    st.link_button("Balun Designs", "https://www.balundesigns.com", use_container_width=True)
with c3:
    st.link_button("Common Mode Chokes", "https://www.karinya.net", use_container_width=True)

st.header("🌍 Operating, DX & Contesting")
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("Club Log", "https://clublog.org", use_container_width=True)
    st.link_button("DX Summit", "https://www.dxsummit.fi", use_container_width=True)
    st.link_button("POTA", "https://pota.app", use_container_width=True)
with c2:
    st.link_button("SOTA", "https://www.sota.org.uk", use_container_width=True)
    st.link_button("LOTW", "https://lotw.arrl.org", use_container_width=True)
    st.link_button("Contest Calendar", "https://www.contestcalendar.com", use_container_width=True)
with c3:
    st.link_button("Reverse Beacon Network", "https://www.reversebeacon.net", use_container_width=True)

st.header("📚 Licensing & Education")
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("ARRL Licensing", "https://www.arrl.org/licensing-education-training", use_container_width=True)
    st.link_button("HamStudy.org", "https://hamstudy.org", use_container_width=True)
with c2:
    st.link_button("QRZ Practice Exams", "https://www.qrz.com/hamtest", use_container_width=True)
    st.link_button("FCC Part 97", "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97", use_container_width=True)
with c3:
    st.link_button("KB6NU Guides", "https://kb6nu.com", use_container_width=True)
    st.link_button("Band Plan (ARRL)", "https://www.arrl.org/band-plan", use_container_width=True)

st.caption("73! This list can be expanded anytime.")