# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

"""
# US Election
"""

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/USParty.csv"

st.title("Likely US Election Winner")
#st.set_page_config(page_title="US Election", layout="wide")

# Sidebar label and icon


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

# Display chart
fig = px.line(df)
st.plotly_chart(fig, use_container_width=True)