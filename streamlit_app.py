import streamlit as st

st.set_page_config(
    page_title="Dashboard",     # Shown in browser tab
    page_icon="📊",             # Optional: sidebar icon
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to the Election Timeseries Dashboard")
st.markdown("""
This dashboard visualizes election data trends over time.  
Use the sidebar to navigate between pages.

All data from Sportsbet.
""")