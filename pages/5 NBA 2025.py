
# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="2025 NBA Winner", layout="wide")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/NBA.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2025 NBA Champion,
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


st.info("Source: [NBA Championship 24/25](https://www.sportsbet.com.au/betting/basketball-us/nba/nba-championship-2024-25-8282449)")