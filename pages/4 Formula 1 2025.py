"""
# US Election
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="2025 F1 Winner", layout="wide")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/F1.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2025 F1 Drivers Champion",
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

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/F1Constructors.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2025 F1 Constructors Champion",
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


st.info("Sources: [F1 Drivers Championship 2025](https://www.sportsbet.com.au/betting/motor-racing/formula-1/f1-drivers-championship-2025-8767626) and [F1 Constructors Championship 2025](https://www.sportsbet.com.au/betting/motor-racing/formula-1/f1-drivers-championship-2025-8767626)")