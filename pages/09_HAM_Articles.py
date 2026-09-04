import streamlit as st
from pathlib import Path

st.set_page_config(page_title="HAM Articles", page_icon="📰", layout="wide")

LOGO_PATH = Path("assets/daves_ham_logo.png")

# ===== Space Theme CSS (same as the rest of the app) =====
st.markdown("""
<style>
    .stApp { background-color: #05080f !important; color: #ffffff; }
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main { background: transparent !important; }
    
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image:
            radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 40px 70px, rgba(255,255,255,0.95), transparent),
            radial-gradient(1px 1px at 50px 160px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 90px 40px, rgba(200,240,255,0.9), transparent),
            radial-gradient(1px 1px at 130px 80px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 160px 120px, rgba(255,255,255,0.85), transparent),
            radial-gradient(1px 1px at 200px 50px, #aaddff, transparent),
            radial-gradient(1.5px 1.5px at 220px 180px, #ffffff, transparent),
            radial-gradient(1px 1px at 300px 100px, rgba(255,255,255,0.9), transparent),
            radial-gradient(1.5px 1.5px at 350px 60px, #ffffff, transparent),
            radial-gradient(1px 1px at 400px 150px, #88ccff, transparent),
            radial-gradient(1.5px 1.5px at 450px 30px, #ffffff, transparent);
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

    section[data-testid="stSidebar"] { background: #05080f !important; border-right: 2px solid #00f0ff33; }

    .stButton > button {
        background: linear-gradient(90deg, #00f0ff, #0099cc);
        color: #0a1325;
        font-weight: 700;
        border-radius: 8px;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff7700, #ffaa00);
        color: white;
    }

    /* Make link buttons look nice */
    a {
        text-decoration: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Logo
col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)
    else:
        st.markdown("**📡 Dave's Ham**")

st.markdown("---")
st.title("📰 HAM Articles & Resources")
st.caption("Curated collection of the best amateur radio articles, news, and technical resources from around the web")

st.info("Click any button to open the article or website in a new tab.")

# ======================================================
# NEWS & CURRENT EVENTS
# ======================================================
st.header("📢 News & Current Events")

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("ARRL News (Official)", "https://www.arrl.org/news", use_container_width=True)
    st.link_button("ARRL Homepage", "https://www.arrl.org", use_container_width=True)
    st.link_button("QRZ.com News", "https://www.qrz.com", use_container_width=True)

with c2:
    st.link_button("Amateur Radio Daily", "https://www.amateurradio.com", use_container_width=True)
    st.link_button("Southgate ARC News", "https://www.southgatearc.org", use_container_width=True)
    st.link_button("The Spectrum Monitor", "https://www.thespectrummonitor.com", use_container_width=True)

with c3:
    st.link_button("FCC Amateur Radio Page", "https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service", use_container_width=True)
    st.link_button("RSGB News (UK)", "https://rsgb.org", use_container_width=True)
    st.link_button("IARU News", "https://www.iaru.org", use_container_width=True)

# ======================================================
# TECHNICAL & PROJECTS
# ======================================================
st.header("🔧 Technical Articles & Projects")

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("ARRL Technical Articles", "https://www.arrl.org/technical", use_container_width=True)
    st.link_button("OnAllBands (DX Engineering)", "https://www.onallbands.com", use_container_width=True)
    st.link_button("Ham Radio Workbench", "https://www.hamradioworkbench.com", use_container_width=True)

with c2:
    st.link_button("QSL.net Technical Library", "https://www.qsl.net", use_container_width=True)
    st.link_button("eHam.net Reviews & Articles", "https://www.eham.net", use_container_width=True)
    st.link_button("VK3CPU Antenna Calculators", "https://www.vk3cpu.net", use_container_width=True)

with c3:
    st.link_button("AA5TB Antenna Notes", "https://www.aa5tb.com", use_container_width=True)
    st.link_button("W8JI Antenna & Station Notes", "https://www.w8ji.com", use_container_width=True)
    st.link_button("K3LR Contest Station", "https://www.k3lr.com", use_container_width=True)

# ======================================================
# ANTENNAS (Most Popular Category)
# ======================================================
st.header("📡 Antenna Articles")

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("ARRL Antenna Book Info", "https://www.arrl.org/shop/ARRL-Antenna-Book", use_container_width=True)
    st.link_button("Classic Loop Skywire", "https://www.arrl.org", use_container_width=True)
    st.link_button("End-Fed Half-Wave Guides", "https://www.onallbands.com", use_container_width=True)

with c2:
    st.link_button("DX Engineering Antenna Articles", "https://www.dxengineering.com/tech-info", use_container_width=True)
    st.link_button("Force 12 / InnovAntennas", "https://www.force12inc.com", use_container_width=True)
    st.link_button("Hexbeam Information", "https://www.hexbeam.com", use_container_width=True)

with c3:
    st.link_button("Balun Designs & Theory", "https://www.balundesigns.com", use_container_width=True)
    st.link_button("Common Mode Chokes", "https://www.karinya.net", use_container_width=True)
    st.link_button("40m & 80m Inverted-V Guides", "https://www.arrl.org", use_container_width=True)

# ======================================================
# OPERATING & DX
# ======================================================
st.header("🌍 Operating, DX & Contesting")

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("Club Log", "https://clublog.org", use_container_width=True)
    st.link_button("DX Summit / Clusters", "https://www.dxsummit.fi", use_container_width=True)
    st.link_button("POTA Official Site", "https://pota.app", use_container_width=True)

with c2:
    st.link_button("SOTA Official Site", "https://www.sota.org.uk", use_container_width=True)
    st.link_button("LOTW (Logbook of The World)", "https://lotw.arrl.org", use_container_width=True)
    st.link_button("QRZ Logbook", "https://www.qrz.com/login", use_container_width=True)

with c3:
    st.link_button("Contest Calendar", "https://www.contestcalendar.com", use_container_width=True)
    st.link_button("WA7BNM Contest Calendar", "https://www.hornucopia.com/contestcal", use_container_width=True)
    st.link_button("Reverse Beacon Network", "https://www.reversebeacon.net", use_container_width=True)

# ======================================================
# LICENSING & EDUCATION
# ======================================================
st.header("📚 Licensing, Education & Beginners")

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("ARRL Licensing", "https://www.arrl.org/licensing-education-training", use_container_width=True)
    st.link_button("HamStudy.org", "https://hamstudy.org", use_container_width=True)
    st.link_button("QRZ Practice Exams", "https://www.qrz.com/hamtest", use_container_width=True)

with c2:
    st.link_button("FCC Part 97 Rules", "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97", use_container_width=True)
    st.link_button("Band Plan (ARRL)", "https://www.arrl.org/band-plan", use_container_width=True)
    st.link_button("Technician Question Pool", "https://www.ncvec.org", use_container_width=True)

with c3:
    st.link_button("Ham Radio Crash Course", "https://www.youtube.com/@HamRadioCrashCourse", use_container_width=True)
    st.link_button("KB6NU’s No-Nonsense Guides", "https://kb6nu.com", use_container_width=True)
    st.link_button("ARRL Handbook Info", "https://www.arrl.org/shop/ARRL-Handbook", use_container_width=True)

# ======================================================
# MAGAZINES & LONG-FORM
# ======================================================
st.header("📖 Magazines & Long-Form Content")

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("QST Magazine (ARRL)", "https://www.arrl.org/qst", use_container_width=True)
    st.link_button("QEX – Experiments", "https://www.arrl.org/qex", use_container_width=True)
    st.link_button("National Contest Journal", "https://www.arrl.org/ncj", use_container_width=True)

with c2:
    st.link_button("RadCom (RSGB)", "https://rsgb.org/main/publications-and-articles/radcom/", use_container_width=True)
    st.link_button("Practical Wireless", "https://www.radioenthusiast.co.uk", use_container_width=True)
    st.link_button("CQ Magazine", "https://www.cq-amateur-radio.com", use_container_width=True)

with c3:
    st.link_button("Amateur Radio Journal", "https://www.amateurradio.com", use_container_width=True)
    st.link_button("The Spectrum Monitor Archives", "https://www.thespectrummonitor.com", use_container_width=True)
    st.link_button("Nuts & Volts / Servo", "https://www.nutsvolts.com", use_container_width=True)

st.markdown("---")
st.caption("This is a curated list of high-quality amateur radio resources. New articles and sites can be added anytime. 73!")