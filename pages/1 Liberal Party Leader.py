"""
# US Election
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Liberal Party Leader", layout="wide")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/LiberalLeader.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely Liberal Party Leader After Peter Dutton",
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


st.info("Sources: [Liberal Leadership](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/liberal-leadership-9176759)")