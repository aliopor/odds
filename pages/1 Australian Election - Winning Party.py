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

rename_map = {'Labor 45 or Less (Coalition 55 or more)':"Labor 45% or less", 'Labor 46 - Coalition 54' : "Labor 46%", 'Labor 47 - Coalition 53' : "Labor 47%", 'Labor 48 - Coalition 52': "Labor 48%", 'Labor 49 - Coalition 51': "Labor 49%", 'Labor 50 - Coalition 50': "Labor 50%", 'Labor 51 - Coalition 49' : "Labor 51%", 'Labor 52 - Coalition 48' : "Labor 52%", 'Labor 53 - Coalition 47':"Labor 53%", 'Labor 54 - Coalition 46' : "Labor 54%", 'Labor 55 or More (Coalition 45 or less)': "Labor 55% or more"}

df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")
df = df*100
scenarios = df.tail(1).columns.tolist()
scenariosRenamed = [rename_map.get(item, item) for item in scenarios]
category_order = {"x": scenariosRenamed} 
values = df.iloc[-1].tolist()

fig = go.Figure()

fig = px.bar(
    x=scenariosRenamed,
    y=values,
    labels={"x": "Scenario", "y": "Likelihood (%)"},
    title="Likely 2-Party Preferred Vote Share",
    category_orders={"x": scenarios}
)

fig.update_layout(
    xaxis_tickangle=-45,
    yaxis=dict(range=[0, max(values) * 1.1]),
    template="simple_white"
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.plotly_chart(fig, use_container_width=True)

#st.plotly_chart(fig, use_container_width=True)

st.info("Source: [48th Parliament of Australia](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/48th-parliament-of-australia-8571604) and [Two-Party Preferred Vote Percentage](https://www.sportsbet.com.au/betting/politics/australian-federal-politics/two-party-preferred-vote-percentage-9083891)")