"""
Hull_01_yieldCurve (University of Hull) — Code 01
Interactive 3D US Treasury yield curve surface (1990–present).

Dependencies:
    pip install pandas plotly
"""

import pandas as pd
import plotly.graph_objects as go

url = "https://raw.githubusercontent.com/epogrebnyak/data-ust/master/ust.csv"
df = pd.read_csv(url, parse_dates=["date"]).set_index("date")

cols = [
    "BC_1MONTH","BC_3MONTH","BC_6MONTH","BC_1YEAR","BC_2YEAR","BC_3YEAR",
    "BC_5YEAR","BC_7YEAR","BC_10YEAR","BC_20YEAR","BC_30YEAR"
]
df = df[cols].dropna(how="all")
df = df.resample("W").mean() # W➔week, comment it out for Daily obs

x_map = {
    "BC_1MONTH": 1/12, "BC_3MONTH": 3/12, "BC_6MONTH": 6/12, "BC_1YEAR": 1,
    "BC_2YEAR": 2, "BC_3YEAR": 3, "BC_5YEAR": 5, "BC_7YEAR": 7,
    "BC_10YEAR": 10, "BC_20YEAR": 20, "BC_30YEAR": 30
}

cols_sorted = sorted(df.columns, key=lambda c: x_map[c])
df = df[cols_sorted]
x = [x_map[c] for c in cols_sorted]

fig = go.Figure(
    data=[go.Surface(x=x, y=df.index, z=df.values, colorscale="Greys", showscale=False)]
)

camera_preset = dict(
    eye=dict(x=1.26, y=1.82, z=0.63),
    up=dict(x=0, y=0, z=1)
)

fig.update_layout(
    title="US Treasury Yield Curve (3D surface, 1990–present)",
    width=1400,
    height=800,
    margin=dict(l=0, r=0, t=60, b=0),
    scene=dict(
        xaxis_title="Maturity (years)",
        yaxis_title="Date",
        zaxis_title="Yield (%)",
        xaxis=dict(autorange="reversed"),
        camera=camera_preset
    ),
)

fig.show()
