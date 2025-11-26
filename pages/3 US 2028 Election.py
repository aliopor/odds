"""
# US Election
"""

# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="2028 US Election", layout="wide")

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/USParty.csv"

#st.title("Likely US Election Winner")

# Sidebar label and icon


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    y=["Democratic Party", "Republican Party"],
    title="Likely 2028 US Election Winning Party",
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
    yaxis_title="Likelihood (%)",
    xaxis_title="Date"
)

st.plotly_chart(fig, use_container_width=True)

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/USElection.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2028 US Election Winner",
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

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/2028DemocraticNominee.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2028 US Democratic Nominee",
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

csv_url = "https://raw.githubusercontent.com/aliopor/odds/refs/heads/main/2028RepublicanNominee.csv"


# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

fig = px.line(
    df,
    title="Likely 2028 US Republican Nominee",
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

st.info("Sources: [Presidential Election 2028 - Winning Party](https://www.sportsbet.com.au/betting/politics/us-politics/presidential-election-2028-winning-party-8732140), [US Presidential Election 2028](https://www.sportsbet.com.au/betting/politics/us-politics/us-presidential-election-2028-8699063), [Democratic Presidential Nominee 2028](https://www.sportsbet.com.au/betting/politics/us-politics/democratic-presidential-nominee-2028-9863647), and [Republican Presidential Nominee 2028](https://www.sportsbet.com.au/betting/politics/us-politics/republican-presidential-nominee-2028-9863709)")