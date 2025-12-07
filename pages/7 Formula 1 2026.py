"""
# US Election
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="2025 F1 Winner", layout="wide")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/F1Drivers-2026.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2026 F1 Drivers Champion",
)


fig.update_layout(
    yaxis=dict(
        tickformat=".0%",
        range=[0, 1]
    ),
    yaxis_title="Likelihood (%)",
    xaxis_title="Date"
)

st.plotly_chart(fig, use_container_width=True)

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/F1Const-2026.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2026 F1 Constructors Champion",
)


fig.update_layout(
    yaxis=dict(
        tickformat=".0%",
        range=[0, 1]
    ),
    yaxis_title="Likelihood (%)",
    xaxis_title="Date"
)

st.plotly_chart(fig, use_container_width=True)

st.info("Source: [F1 2026](https://www.sportsbet.com.au/betting/motor-racing/formula-1)")