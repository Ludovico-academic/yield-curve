# hull-01-yield-curve

Interactive 3D **US Treasury yield curve surface** (1990–present) built in Python using **pandas** + **Plotly**.  
This is **Code 01** for University of Hull teaching materials.

## What it does
- Downloads US Treasury yield data (daily) from a public CSV source (no API key needed)
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

Install:
```bash
pip install pandas plotly
```

## How to run
```bash
python3 yieldCurve.py
```
