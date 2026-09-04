import streamlit as st
from pathlib import Path
import random

st.set_page_config(page_title="Morse Trainer", page_icon="📡", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { 
        background-color: #05080f !important; 
        color: #ffffff; 
    }
    [data-testid="stAppViewContainer"], .main { 
        background: transparent !important; 
    }
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

    /* ===== FIX FOR CODE BLOCKS ===== */
    .stCodeBlock, pre, code {
        background-color: #0f2344 !important;
        color: #00f0ff !important;
        border: 1px solid #00f0ff55 !important;
        border-radius: 8px !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        padding: 12px !important;
    }

    .stTextInput input {
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

    section[data-testid="stSidebar"] { 
        background: #05080f !important; 
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("📡 Morse Code Trainer")

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

st.subheader("Letter → Morse")
letter = st.radio("Choose a letter", list(MORSE.keys()), horizontal=True)
st.code(MORSE[letter], language=None)

st.markdown("---")
st.subheader("Practice: What letter is this?")

if "morse_quiz" not in st.session_state:
    st.session_state.morse_quiz = random.choice(list(MORSE.keys()))

st.code(MORSE[st.session_state.morse_quiz], language=None)

guess = st.text_input("Type the letter").upper()

if st.button("Check Answer"):
    if guess == st.session_state.morse_quiz:
        st.success("Correct!")
    else:
        st.error(f"Wrong. It was **{st.session_state.morse_quiz}**")
    st.session_state.morse_quiz = random.choice(list(MORSE.keys()))
    st.rerun()