import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import timedelta

# --- 1. CONFIGURATION (Match these to your data.csv column names) ---
DATA_PATH = "data.csv.gz"
COL_MARKET = "market"       # e.g., "Event A"
COL_PARTY = "name"         # e.g., "Party 1"
COL_PRICE = "price"         # e.g., 125, 350
COL_TIME = "tstamp"      # e.g., "2026-11-23 12:00:00"
ARCHIVE_DAYS_THRESHOLD = 7  # Markets older than this go to Archive
TOP_N_PARTIES = 6

st.set_page_config(page_title="Market Odds Tracker", layout="wide")

# --- 2. LOAD & PROCESS DATA ---
@st.cache_data
def load_and_normalize_data(path):
    df = pd.read_csv(path)

    # <-- Place the second snippet right here -->
    df[COL_TIME] = pd.to_datetime(df[COL_TIME], errors="coerce")
    df = df.dropna(subset=[COL_TIME, COL_PRICE]).copy()
    df[COL_MARKET] = df[COL_MARKET].fillna(df["marketId"].astype(str))

    # Filter out invalid/zero prices
    df = df[df[COL_PRICE] > 0].copy()

    # Step 1: Convert price to raw implied odds (1 / price)
    df["raw_odds"] = 1.0 / df[COL_PRICE]

    # Step 2: Normalize so probabilities sum to 1 per market & timestamp
    market_time_totals = df.groupby([COL_MARKET, COL_TIME])["raw_odds"].transform("sum")
    df["probability"] = df["raw_odds"] / market_time_totals

    return df

df = load_and_normalize_data(DATA_PATH)

# --- 3. CLASSIFY ACTIVE VS. ARCHIVED MARKETS ---
latest_global_time = df[COL_TIME].max()
cutoff_time = latest_global_time - timedelta(days=ARCHIVE_DAYS_THRESHOLD)

market_last_seen = df.groupby(COL_MARKET)[COL_TIME].max()
active_markets = sorted(market_last_seen[market_last_seen >= cutoff_time].index.tolist())
archived_markets = sorted(market_last_seen[market_last_seen < cutoff_time].index.tolist())

# --- 4. UI & INTERACTIVE VISUALIZATION ---
st.title("Market Implied Probability Tracker")

view_mode = st.radio(
    "Select Market Status:",
    options=["Current Markets", "Archive (Historical Markets)"],
    horizontal=True
)

available_markets = active_markets if view_mode == "Current Markets" else archived_markets

if not available_markets:
    st.info(f"No markets found in {view_mode}.")
    st.stop()

selected_market = st.selectbox("Select a Market to Visualize:", available_markets)

# Filter data for selected market
market_df = df[df[COL_MARKET] == selected_market].copy()

# Determine Top 6 parties based on their most recent probability
latest_market_time = market_df[COL_TIME].max()
latest_snapshot = market_df[market_df[COL_TIME] == latest_market_time]
top_parties = (
    latest_snapshot.sort_values("probability", ascending=False)[COL_PARTY]
    .head(TOP_N_PARTIES)
    .tolist()
)

# Optional toggle to show all parties vs top 6
limit_to_top = st.checkbox(f"Limit to Top {TOP_N_PARTIES} parties", value=True)

top_method = st.radio(
    "Rank top parties by:",
    options=["Most recent probability", "Highest historical probability"],
    horizontal=True,
    disabled=not limit_to_top,
)

if limit_to_top:
    if top_method == "Most recent probability":
        latest_market_time = market_df[COL_TIME].max()
        latest_snapshot = market_df[market_df[COL_TIME] == latest_market_time]
        top_parties = (
            latest_snapshot.sort_values("probability", ascending=False)[COL_PARTY]
            .head(TOP_N_PARTIES)
            .tolist()
        )
    else:
        # Peak ("highest") probability reached across the market's history
        top_parties = (
            market_df.groupby(COL_PARTY)["probability"]
            .max()
            .sort_values(ascending=False)
            .head(TOP_N_PARTIES)
            .index.tolist()
        )

    plot_df = market_df[market_df[COL_PARTY].isin(top_parties)].copy()
else:
    plot_df = market_df.copy()

# Sort chronologically for clean line plotting
plot_df = plot_df.sort_values(COL_TIME)

# --- 5. PLOTLY INTERACTIVE CHART ---
plot_df = plot_df.copy()
plot_df["price_display"] = plot_df[COL_PRICE].round().astype("Int64")

fig = px.line(
    plot_df,
    x=COL_TIME,
    y="probability",
    color=COL_PARTY,
    title=f"{selected_market}",
    labels={
        COL_TIME: "Date / Time",
        "probability": "Implied Probability",
        COL_PARTY: "Outcome",
        "price_display": "Price",
    },
    hover_data={COL_PRICE: False, "price_display": True, "probability": ":.1%"},
)

fig.update_yaxes(tickformat=".0%", range=[0, 1])
fig.update_layout(hovermode="x unified", legend_title_text="Party / Outcome")

st.plotly_chart(fig, use_container_width=True)

# Optional: Show latest odds table below the chart
with st.expander("View Latest Snapshot Table"):
    summary_table = (
        latest_snapshot[[COL_PARTY, COL_PRICE, "probability"]]
        .sort_values("probability", ascending=False)
        .assign(
            **{
                COL_PRICE: lambda x: x[COL_PRICE].round().astype("Int64"),
                "probability": lambda x: (x["probability"] * 100).round(2).astype(str) + "%",
            }
        )
    )
    st.dataframe(summary_table, use_container_width=True, hide_index=True)