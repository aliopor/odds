import streamlit as st
import pandas as pd

st.set_page_config(page_title="Election Dashboard", layout="wide")

st.title("🗳️ Welcome to the Election Timeseries Dashboard")
st.markdown("""
This dashboard visualizes election data trends over time.  
Use the sidebar to navigate between pages like:
- Coalition vs Labor
- Minor Parties Breakdown
- Full Timeseries

Data is auto-updated and powered by GitHub + Streamlit.
""")