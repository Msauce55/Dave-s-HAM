import streamlit as st
from datetime import datetime

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