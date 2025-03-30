"""
# Likely Type of Government
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Likely Type of Government", layout="wide")

# Optional: Repeat the title for clarity or styling
st.title("Likely Type of Government")


csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/typeOfGov.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    y=["Coalition Majority", "Coalition Minority", "Labor Majority", "Labor Minority"],
    title="Election Trends",
)

# Display chart
#fig = px.line(df)
fig.update_traces(selector=dict(name="Labor Majority"), line=dict(color="red", dash="solid"))
fig.update_traces(selector=dict(name="Coalition Majority"), line=dict(color="blue", dash="solid"))
fig.update_traces(selector=dict(name="Labor Minority"), line=dict(color="red", dash="dash"))
fig.update_traces(selector=dict(name="Coalition Minority"), line=dict(color="blue", dash="dash"))

st.plotly_chart(fig, use_container_width=True)