import streamlit as st
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Dave's Blog", page_icon="📝", layout="wide")
LOGO_PATH = Path("assets/daves_ham_logo.png")

st.markdown("""
<style>
    .stApp { background: #05080f; color: #ffffff; }
    .stApp::before {
        content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 30% 20%, rgba(0,240,255,0.15) 0%, transparent 50%),
                    radial-gradient(circle at 70% 70%, rgba(180,80,255,0.12) 0%, transparent 60%);
        z-index: -2;
    }
    .stApp::after {
        content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(#ffffff 1px, transparent 1px),
                          radial-gradient(#88ddff 1px, transparent 2px);
        background-size: 70px 70px, 140px 140px;
        opacity: 0.42; z-index: -1; pointer-events: none;
    }
    h1, h2, h3 { color: #00f0ff !important; text-shadow: 0 0 12px rgba(0,240,255,0.5); }
    .stApp, p, span, div, label { color: #ffffff !important; }
    section[data-testid="stSidebar"] { background: #05080f; }
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
    st.session_state.blog_posts = [
        {
            "author": "Dave",
            "title": "First Transmission from the Shack",
            "content": "Welcome to the official blog of Dave's Ham Radio Portal. Share your radio adventures, antenna builds, and DX stories here. 73!",
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        }
    ]

st.subheader("✍️ Add a New Post")
with st.form("new_post_form", clear_on_submit=True):
    author = st.text_input("Your Name", value="Dave")
    title = st.text_input("Post Title")
    content = st.text_area("Your Message", height=160)
    submitted = st.form_submit_button("Transmit Post", type="primary")

    if submitted and title.strip() and content.strip():
        new_post = {
            "author": author.strip(),
            "title": title.strip(),
            "content": content.strip(),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        }
        st.session_state.blog_posts.insert(0, new_post)
        st.success("📡 Post transmitted!")
        st.rerun()

st.markdown("---")
st.subheader("Recent Transmissions")

for post in st.session_state.blog_posts:
    with st.container(border=True):
        st.markdown(f"### {post['title']}")
        st.caption(f"de **{post['author']}** • {post['timestamp']}")
        st.write(post["content"])
        st.markdown("---")