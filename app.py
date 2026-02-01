import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Executive Dashboard Portal", layout="wide")

st.title("📊 Executive Dashboard Portal")

BASE_DIR = Path(__file__).parent
DASH_DIR = BASE_DIR / "dashboards"

# Map filenames → clean titles
dashboard_map = {
    "dashboard.html": "🏠 Executive Overview",
    "MoM_Revenue_Dashboard_FINAL (1).html": "📈 Month-on-Month Revenue",
    "YTD_Revenue_Chart_Fixed.html": "📊 YTD Revenue",
    "GC_RC_Growth_Analysis.html": "🚀 Growth Analysis (GC vs RC)",
    "Pareto_Analysis_April_December (1).html": "🥇 Pareto Revenue Analysis",
    "Customer_Segmentation_Chart.html": "👥 Customer Segmentation",
    "nrr.html": "💰 Net Revenue Retention",
}

available_files = sorted((DASH_DIR).glob("*.html"))

# Keep only dashboards that exist
titles = []
files = []
for file in available_files:
    name = file.name
    if name in dashboard_map:
        titles.append(dashboard_map[name])
        files.append(file)

selected = st.sidebar.selectbox("Select Dashboard", titles)
selected_file = files[titles.index(selected)]

html = selected_file.read_text(encoding="utf-8", errors="ignore")

components.html(html, height=950, scrolling=True)
