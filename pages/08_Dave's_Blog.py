import streamlit as st
from datetime import datetime
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
st.set_page_config(
    page_title="Dave's Blog",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Dave's Blog")
st.caption("Only those named Dave can post in the blog")  # humorous subtitle

# Initialize the blog storage (in-memory – resets when the app restarts or session ends)
if "blog_posts" not in st.session_state:
    st.session_state.blog_posts = [
        {
            "author": "Dave",
            "title": "Welcome to the Blog!",
            "content": "This is the first post. Anyone can add to the blog (the subtitle is just for fun).",
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        }
    ]

st.markdown("---")

# ---------- Add a new post ----------
st.subheader("Add a New Post")

with st.form("new_post_form", clear_on_submit=True):
    author = st.text_input("Your Name", placeholder="Dave (or anyone)")
    title = st.text_input("Post Title")
    content = st.text_area("What's on your mind?", height=150)
    
    submitted = st.form_submit_button("Post to Dave's Blog", type="primary")

    if submitted:
        if not author.strip() or not title.strip() or not content.strip():
            st.error("Please fill in all fields.")
        else:
            new_post = {
                "author": author.strip(),
                "title": title.strip(),
                "content": content.strip(),
                "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
            }
            # Add to the beginning so newest posts appear first
            st.session_state.blog_posts.insert(0, new_post)
            st.success("Post published!")
            st.rerun()

st.markdown("---")

# ---------- Display all posts ----------
st.subheader("All Posts")

if not st.session_state.blog_posts:
    st.info("No posts yet. Be the first to write something!")
else:
    for post in st.session_state.blog_posts:
        with st.container():
            st.markdown(f"### {post['title']}")
            st.caption(f"Posted by **{post['author']}** • {post['timestamp']}")
            st.write(post["content"])
            st.markdown("---")