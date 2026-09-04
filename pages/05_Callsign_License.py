import streamlit as st
import requests
from pathlib import Path

st.set_page_config(page_title="Callsign & License", page_icon="🪪", layout="wide")
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
st.title("🪪 Callsign Lookup & License Tools")

tab1, tab2, tab3 = st.tabs(["Callsign Lookup", "Practice Exam", "Band Plan"])

with tab1:
    call = st.text_input("Enter US callsign", placeholder="W1AW").strip().upper()
    if st.button("Lookup", type="primary") and call:
        try:
            r = requests.get(f"https://callook.info/{call}/json", timeout=6)
            data = r.json()
            if data.get("status") == "VALID":
                st.success(f"**{data['current']['callsign']}** is valid")
                c1, c2 = st.columns(2)
                with c1:
                    st.write("**Name:**", data.get("name", "—"))
                    st.write("**Class:**", data["current"].get("operClass", "—"))
                with c2:
                    loc = data.get("location", {})
                    st.write("**Grid:**", loc.get("gridsquare", "—"))
                    st.write("**Location:**", f"{loc.get('latitude')}, {loc.get('longitude')}")
            else:
                st.warning(f"Status: {data.get('status')}")
        except Exception as e:
            st.error(f"Lookup failed: {e}")

with tab2:
    st.subheader("Technician Sample Questions")
    questions = [
        {"q": "What is the ITU phonetic for 'B'?", "choices": ["Baker", "Bravo", "Boston", "Beta"], "answer": 1},
        {"q": "Max power on 70 cm for Technician?", "choices": ["50 W", "200 W", "1500 W", "25 W"], "answer": 2},
        {"q": "Common use of 2-meter band?", "choices": ["DX on 160m", "Local FM repeaters", "AM broadcast", "Satellite only"], "answer": 1},
    ]
    if "q_idx" not in st.session_state:
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.session_state.total = 0

    q = questions[st.session_state.q_idx % len(questions)]
    st.write(f"**Question:** {q['q']}")
    choice = st.radio("Answer", q["choices"], key=f"q{st.session_state.q_idx}")

    if st.button("Check Answer"):
        st.session_state.total += 1
        if q["choices"].index(choice) == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong. Correct: {q['choices'][q['answer']]}")

    if st.button("Next Question"):
        st.session_state.q_idx += 1
        st.rerun()

    if st.session_state.total:
        st.metric("Score", f"{st.session_state.score}/{st.session_state.total}")

with tab3:
    st.markdown("""
    | Band | Frequency | Notes |
    |------|-----------|-------|
    | 160 m | 1.8–2.0 MHz | CW, SSB, digital |
    | 80 m | 3.5–4.0 MHz | Night-time DX |
    | 40 m | 7.0–7.3 MHz | Workhorse band |
    | 20 m | 14.0–14.35 MHz | Primary DX |
    | 15 m | 21.0–21.45 MHz | Good when SFI high |
    | 10 m | 28.0–29.7 MHz | Technician phone > 28.3 |
    | 2 m | 144–148 MHz | FM repeaters |
    | 70 cm | 420–450 MHz | FM + digital |
    """)