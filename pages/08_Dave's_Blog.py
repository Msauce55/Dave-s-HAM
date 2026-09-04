import streamlit as st
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Dave's Blog", page_icon="📝", layout="wide")
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
                          radial-gradient(1.5px 1.5px at 160px 120px, #ffffff, transparent),
                          radial-gradient(1px 1px at 300px 100px, #ffffff, transparent);
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
    .stApp, p, span, div, label { color: #ffffff !important; }
    .stForm, .stForm *, div[data-testid="stVerticalBlockBorderWrapper"] * { color: #000000 !important; }
    section[data-testid="stSidebar"] { background: #05080f !important; }
    .stButton > button { background: linear-gradient(90deg, #00f0ff, #0099cc); color: #0a1325; font-weight: 700; border-radius: 8px; }
    .stButton > button:hover { background: linear-gradient(90deg, #ff7700, #ffaa00); color: white; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 3, 1])
with col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=160)

st.markdown("---")
st.title("📝 Dave's Blog")
st.caption("Only those named Dave can post in the blog")

if "blog_posts" not in st.session_state:
    st.session_state.blog_posts = [{
        "author": "Dave",
        "title": "First Transmission from the Shack",
        "content": "Welcome to the official blog of Dave's Ham Radio Portal. Share your radio adventures, antenna builds, and DX stories here. 73!",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    }]

st.subheader("✍️ Add a New Post")
with st.form("new_post_form", clear_on_submit=True):
    author = st.text_input("Your Name", value="Dave")
    title = st.text_input("Post Title")
    content = st.text_area("Your Message", height=160)
    submitted = st.form_submit_button("Transmit Post", type="primary")
    if submitted and title.strip() and content.strip():
        st.session_state.blog_posts.insert(0, {
            "author": author.strip(),
            "title": title.strip(),
            "content": content.strip(),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        })
        st.success("📡 Post transmitted!")
        st.rerun()

st.markdown("---")
st.subheader("Recent Transmissions")
for post in st.session_state.blog_posts:
    with st.container(border=True):
        st.markdown(f"### {post['title']}")
        st.caption(f"de **{post['author']}** • {post['timestamp']}")
        st.write(post["content"])