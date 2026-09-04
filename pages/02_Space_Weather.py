import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Space Weather", page_icon="☀️", layout="wide")
st.title("☀️ Space Weather & Propagation")
st.caption("Live data from NOAA Space Weather Prediction Center")

@st.cache_data(ttl=300)
def fetch_solar():
    try:
        k_data = requests.get("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json", timeout=8).json()
        flux_data = requests.get("https://services.swpc.noaa.gov/json/f107_cm_flux.json", timeout=8).json()
        daily = requests.get("https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json", timeout=8).json()
        
        return {
            "k_index": k_data[-1].get("kp_index", "—") if k_data else "—",
            "k_time": k_data[-1].get("time_tag", "—") if k_data else "—",
            "sfi": flux_data[-1].get("flux", "—") if flux_data else "—",
            "a_index": daily[-1].get("a_index", "—") if daily else "—",
            "ssn": daily[-1].get("ssn", "—") if daily else "—",
            "raw_k": k_data[-60:] if k_data else [],
        }
    except Exception as e:
        return {"k_index": "—", "sfi": "—", "a_index": "—", "ssn": "—", "raw_k": [], "error": str(e)}

solar = fetch_solar()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Solar Flux (SFI)", solar["sfi"])
c2.metric("K-Index", solar["k_index"])
c3.metric("A-Index", solar["a_index"])
c4.metric("Sunspot Number", solar["ssn"])

st.write(f"**Last K-index update:** `{solar.get('k_time', 'N/A')}`")

if solar.get("raw_k"):
    df = pd.DataFrame(solar["raw_k"])
    if "kp_index" in df.columns:
        fig = px.line(df, x="time_tag", y="kp_index", title="Recent Planetary K-Index")
        st.plotly_chart(fig, use_container_width=True)

st.subheader("Band Condition Guidance")
try:
    k = float(solar["k_index"])
except:
    k = 3

if k <= 2:
    st.success("🟢 Quiet conditions — good for HF DX")
elif k <= 4:
    st.warning("🟡 Unsettled — mid-latitude paths may be noisy")
else:
    st.error("🔴 Storm levels — expect absorption on high-latitude paths")

st.markdown("""
**Useful external tools**
- [VOACAP Online](https://www.voacap.com/hf/)
- [KC2G Real-time MUF Map](https://prop.kc2g.com/)
- [NOAA SWPC](https://www.swpc.noaa.gov/)
""")