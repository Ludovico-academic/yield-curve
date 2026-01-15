"""
Hull_01_yieldCurve (University of Hull) — Code 01
Interactive 3D US Treasury yield curve surface (1990–present).

Dependencies:
    pip install pandas plotly pandas_datareader
"""

import pandas as pd
import plotly.graph_objects as go
from pandas_datareader import data as web

# FRED tickers for US Treasury constant maturity yields
fred_series = {
    "1M":  "DGS1MO",
    "3M":  "DGS3MO",
    "6M":  "DGS6MO",
    "1Y":  "DGS1",
    "2Y":  "DGS2",
    "3Y":  "DGS3",
    "5Y":  "DGS5",
    "7Y":  "DGS7",
    "10Y": "DGS10",
    "20Y": "DGS20",
    "30Y": "DGS30",
}

# Download from FRED
start = "1990-01-01"
end = pd.Timestamp.today().strftime("%Y-%m-%d")

df = web.DataReader(list(fred_series.values()), "fred", start, end)

df = df.rename(columns={v: k for k, v in fred_series.items()})
df = df.resample("W").mean() # W➔week, comment it out for Daily obs

df = df.dropna()

x_map = {
    "1M": 1/12, "3M": 3/12, "6M": 6/12,
    "1Y": 1, "2Y": 2, "3Y": 3, "5Y": 5, "7Y": 7,
    "10Y": 10, "20Y": 20, "30Y": 30
}

cols_sorted = sorted(df.columns, key=lambda c: x_map[c])
df = df[cols_sorted]
x = [x_map[c] for c in cols_sorted]

fig = go.Figure(
    data=[go.Surface(
        x=x,
        y=df.index,
        z=df.values,
        colorscale="Greys",
        showscale=False
    )]
)

fig.update_layout(
    title="US Treasury Yield Curve (3D surface, 1990–present)",
    margin=dict(l=0, r=0, t=60, b=0),
    scene=dict(
        xaxis_title="Maturity (years)",
        yaxis_title="Date",
        zaxis_title="Yield (%)",
        xaxis=dict(autorange="reversed"),
        aspectmode="manual",
        aspectratio=dict(x=2.4, y=2.8, z=1.0),
        camera=dict(
            eye=dict(x=1.90, y=2.95, z=.76),
            center=dict(x=0, y=0, z=-.4),
            up=dict(x=0, y=0, z=1)
        )
    ),
)


fig.show()
