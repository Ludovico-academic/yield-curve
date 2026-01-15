# hull-01-yield-curve

Interactive 3D **US Treasury yield curve surface** (1990–present) built in Python (pandas + Plotly), using **pandas_datareader** to pull data from FRED (Federal Reserve Economic Data).
This is **Code 01** for University of Hull teaching materials.

## What it does
- Downloads daily US Treasury yield data from **FRED**
  - Uses constant maturity Treasury series (DGS tickers)
  - No API key required
- Builds a 3D surface:
  - **x** = maturity (years)  
  - **y** = date  
  - **z** = yield (%)
- Optional weekly resampling for faster rendering
- Greyscale (black & white) surface, no colour bar
- Fixed camera angle + zoom suitable for lectures

## Requirements
- Python 3.9+ recommended (works with newer versions as well)
- Packages:
  - `pandas`
  - `plotly`
  - `pandas_datareader`

Install:
```bash
pip install pandas plotly pandas_datareader
```

## How to run
```bash
python3 yieldCurve.py
```
