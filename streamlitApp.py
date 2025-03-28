# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

csv_url = "https://github.com/aliopor/odds/blob/main/data.csv"

st.set_page_config(page_title="Time Series Dashboard", layout="wide")
st.title("Timeseries Dashboard")

#csvPath = os.path.join(csvPathname, "data.csv")

# Load CSV
df = pd.read_csv(csv_url, parse_dates=["tstamp"], index_col="tstamp")

# Display chart
fig = px.line(df)
st.plotly_chart(fig, use_container_width=True)