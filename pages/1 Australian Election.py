"""
# Likelihood of Forming Government
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

st.set_page_config(page_title="Likely Party to Form Government in 2028(?) Australian Election", layout="wide")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/formedGov.csv"

# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")
combined = pd.concat([priceData['Coalition'].dropna(), priceData['Liberal and/or Nationals'].dropna()])
df = pd.DataFrame({"combined":combined})
df = pd.concat([priceData, df], axis=1)
df.drop('Liberal and/or Nationals', axis=1, inplace=True)
df.rename(columns={'combined': 'Liberal and/or Nationals'}, inplace=True)


fig = px.line(
    df,
    y=["Labor", "Liberal and/or Nationals"],
    title="Likely Party to Form Government in 2028(?) Australian Election"
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

st.info("Source: [49th Parliament of Australia](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/49th-parliament-of-australia-9186904)")