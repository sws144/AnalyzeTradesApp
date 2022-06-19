"""
Analyze Trades Streamlit App - see README.md for details
"""

from src import predictresult as analyze_pred

import streamlit as st
import numpy as np
import pandas as pd

# tables
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

st.dataframe(df.style.highlight_max(axis=0))

st.line_chart(df)

# map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)

st.map(map_data)

# slider
x = st.slider("x")
st.write(x, "square is", x * x)

# checkbox
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    chart_data
