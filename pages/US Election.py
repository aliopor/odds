"""
# US Election
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="US Election", layout="wide")

# Optional: Repeat the title for clarity or styling
st.title("US Election")


csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/USParty.csv"

#st.title("Likely US Election Winner")

# Sidebar label and icon


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    y=["Democratic Party", "Republican Party"],
)

# Display chart
#fig = px.line(df)
fig.update_traces(selector=dict(name="Republican Party"), line=dict(color="red", dash="solid"))
fig.update_traces(selector=dict(name="Democratic Party"), line=dict(color="blue", dash="solid"))


fig.update_layout(
    yaxis=dict(
        tickformat=".0%",
        range=[0, 1]
    ),
    yaxis_title="Likelihood (%)"
)

st.plotly_chart(fig, use_container_width=True)

st.info("Source: [Type of Government Formed](https://www.sportsbet.com.au/betting/politics/us-politics/presidential-election-2028-winning-party-8732140)")