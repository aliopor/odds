"""
# Likelihood of Forming Government
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Likely Party to Form Government in 2024 Australian Election", layout="wide")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/formedGov.csv"

# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")



fig = px.line(
    df,
    y=["Labor", "Coalition"],
    title="Likely Party to Form Government in 2024 Australian Election"
)

# Display chart
#fig = px.line(df)
fig.update_traces(selector=dict(name="Labor"), line=dict(color="red", dash="solid"))
fig.update_traces(selector=dict(name="Coalition"), line=dict(color="blue", dash="solid"))

fig.update_layout(
    yaxis=dict(
        tickformat=".0%",
        range=[0, 1]
    ),
    yaxis_title="Likelihood (%)",
    xaxis_title="Date"
)

st.plotly_chart(fig, use_container_width=True)

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/TwoPartyPreferred.csv"

df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")
scenarios = df.tail(1).columns.tolist()
values = df.iloc[-1].tolist()

# Create the bell-shaped curve using a smooth line
fig = go.Figure()

# Add smooth line (interpolated)
fig.add_trace(go.Scatter(
    x=scenarios,
    y=values,
    mode='lines+markers',
    name="Likelihood",
    line=dict(shape='spline', color='royalblue', width=3),
    marker=dict(size=6)
))

fig.update_layout(
    title="Bell Curve of Vote Share Scenarios",
    xaxis_title="Scenario",
    yaxis_title="Value / Likelihood (%)",
    xaxis_tickangle=-45,
    template="simple_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.info("Source: [48th Parliament of Australia](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/48th-parliament-of-australia-8571604)")