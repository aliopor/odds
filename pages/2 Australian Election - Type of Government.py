"""
# Likely Type of Government
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Likely Type of Government in 2024 Australian Election", layout="wide")


csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/typeOfGov.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    y=["Coalition Majority", "Coalition Minority", "Labor Majority", "Labor Minority"],
    title="Likely Type of Government in 2024 Australian Election",
)

# Display chart
#fig = px.line(df)
fig.update_traces(selector=dict(name="Labor Majority"), line=dict(color="red", dash="solid"))
fig.update_traces(selector=dict(name="Coalition Majority"), line=dict(color="blue", dash="solid"))
fig.update_traces(selector=dict(name="Labor Minority"), line=dict(color="red", dash="dashdot"))
fig.update_traces(selector=dict(name="Coalition Minority"), line=dict(color="blue", dash="dashdot"))

fig.update_layout(
    yaxis=dict(
        tickformat=".0%",
        range=[0, 1]
    ),
    yaxis_title="Likelihood (%)",
    xaxis_title="Date"
)

st.plotly_chart(fig, use_container_width=True)

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/Majority.csv"



# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    y=["Yes"],
    title="Chance of a Majority Government in 2024 Australian Election",
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

st.info("Sources: [Type of Government Formed](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/type-of-government-formed-8878095) and [Majority Government](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/majority-government-8878114)")