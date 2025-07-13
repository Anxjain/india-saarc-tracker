
import streamlit as st
import pandas as pd
import os

st.title("India–SAARC Trade & Investment Tracker")
st.markdown("## Live World Bank Data (USD, in Millions)")

data_file = "India_SAARC_Tracker_Data.xlsx"

# Function to format numbers into millions
def format_millions(val):
    try:
        val = float(val)
        return f"{val / 1_000_000:,.2f} M"
    except:
        return val

if st.button("Refresh Data"):
    os.system("python india_saarc_data_script.py")

if os.path.exists(data_file):
    df = pd.read_excel(data_file)
    for col in df.columns:
        if col != "Country" and col != "Last Updated":
            df[col] = df[col].apply(format_millions)
    st.dataframe(df)
else:
    st.warning("Data file not found. Please refresh.")
