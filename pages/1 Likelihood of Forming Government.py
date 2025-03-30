"""
# Likelihood of Forming Government
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Likely Party to Form Government in 2024 Australian Election", layout="wide")

# Optional: Repeat the title for clarity or styling
st.markdown("### Likely Party to Form Government in 2024 Australian Election")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/formedGov.csv"

# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")



fig = px.line(
    df,
    y=["Labor", "Coalition"],
    title="Test",
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
    yaxis_title="Likelihood (%)"
)

st.plotly_chart(fig, use_container_width=True)

st.info("Source: [48th Parliament of Australia](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/48th-parliament-of-australia-8571604)")