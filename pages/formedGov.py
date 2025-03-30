"""
# Likelihood of Forming Government
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Likelihood of Forming Government", layout="wide")

# Optional: Repeat the title for clarity or styling
st.title("Likelihood of Forming Government")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/formedGov.csv"

# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")



fig = px.line(
    df,
    y=["Labor", "Coalition"],
    title="Election Trends",
)

# Display chart
#fig = px.line(df)
fig.update_traces(selector=dict(name="Labor"), line=dict(color="red", dash="solid"))
fig.update_traces(selector=dict(name="Coalition"), line=dict(color="blue", dash="solid"))

st.plotly_chart(fig, use_container_width=True)