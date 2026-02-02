import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="Revenue Dashboard | Apr–Dec 2025", layout="wide")

# Compact layout styling
st.markdown(
    """
    <style>
      .block-container {padding-top: 0.6rem; padding-bottom: 0.5rem;}
      header[data-testid="stHeader"] {height: 0rem;}
      div[data-testid="stToolbar"] {visibility: hidden; height: 0rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# Header bar
st.markdown(
    """
    <div style="display:flex; align-items:baseline; gap:14px; margin-bottom:8px;">
      <div style="font-size:22px; font-weight:700;">Revenue Dashboard</div>
      <div style="font-size:16px; opacity:0.7;">Apr–Dec 2025</div>
    </div>
    """,
    unsafe_allow_html=True
)

BASE_DIR = Path(__file__).parent
DASH_DIR = BASE_DIR / "dashboards"

# -------------------------
# Dashboard order + mapping
# -------------------------
tabs_config = [
    ("📊 YTD Revenue", "YTD_Revenue_Chart_Fixed.html"),
    ("📈 QoQ Revenue ", "dashboard.html"),
    ("🔁 QoQ NRR (April Cohort)", "nrr.html"),
    ("📅 MoM Revenue", "MoM_Revenue_Dashboard_FINAL (1).html"),
    ("🧭 Pareto Drivers", "Pareto_Analysis_CORRECTED.html"),
    ("👥 Customer Segments", "Customer_Segmentation_Chart.html"),
    ("🔀 GC vs RC Growth", "GC_RC_Growth_Analysis.html"),
]

# Safety check
missing = [f for _, f in tabs_config if not (DASH_DIR / f).exists()]
if missing:
    st.error("Missing HTML files in dashboards folder:\n\n- " + "\n- ".join(missing))
    st.stop()

# -------------------------
# Tabs
# -------------------------
tab_labels = [t[0] for t in tabs_config]
tabs = st.tabs(tab_labels)

for tab, (_, filename) in zip(tabs, tabs_config):
    with tab:
        html = (DASH_DIR / filename).read_text(encoding="utf-8", errors="ignore")
        components.html(html, height=920, scrolling=True)
