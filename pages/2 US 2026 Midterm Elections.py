"""
# US Election
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="2028 US Election", layout="wide")


csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/2026MidtermHouse.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2026 US House Majority",
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

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/2026MidtermSenate.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2026 US Senate Majority",
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

st.info("Sources: [House Control 2026 Midterm Elections](https://www.sportsbet.com.au/betting/politics/us-politics/house-control-2026-midterm-elections-9863732) and [Senate Control 2026 Mid Terms](https://www.sportsbet.com.au/betting/politics/us-politics/senate-control-2026-mid-terms-9863728)")