"""
# Chance of Majority Government
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Chance of Majority Government in 2024 Australian Election", layout="wide")


csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/Majority.csv"



# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    y=["Yes"],
    title="Chance of a Mjority Government in 2024 Australian Election",
)

# Display chart
#fig = px.line(df)
fig.update_traces(selector=dict(name="Yes"), line=dict(color="red", dash="solid"))


fig.update_layout(
    yaxis=dict(
        tickformat=".0%",
        range=[0, 1]
    ),
    yaxis_title="Likelihood (%)",
    xaxis_title="Date"
)

st.plotly_chart(fig, use_container_width=True)

st.info("Source: [Majority Government](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/majority-government-8878114)")