
import pandas as pd
import requests
from datetime import datetime

# World Bank indicators for trade and FDI in USD
INDICATORS = {
    "Exports (USD)": "NE.EXP.GNFS.CD",
    "Imports (USD)": "NE.IMP.GNFS.CD",
    "FDI Inflow (USD)": "BX.KLT.DINV.CD.WD",
    "FDI Outflow (USD)": "BM.KLT.DINV.CD.WD"
}

COUNTRIES = {
    "Bangladesh": "BGD",
    "Nepal": "NPL",
    "Bhutan": "BTN",
    "Sri Lanka": "LKA",
    "Maldives": "MDV",
    "Afghanistan": "AFG",
    "Pakistan": "PAK"
}

# Fetch most recent non-null value from World Bank API
def fetch_latest_value(country_code, indicator):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?format=json&per_page=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1 and data[1]:
            for entry in data[1]:
                value = entry.get("value")
                if value is not None:
                    return round(value, 2)
    return "N/A"

# Generate real tracker data
def generate_saarc_tracker_data():
    records = []
    for name, iso3 in COUNTRIES.items():
        row = {"Country": name}
        for label, indicator in INDICATORS.items():
            row[label] = fetch_latest_value(iso3, indicator)
        # Compute trade balance if both export and import are present
        exports = row["Exports (USD)"]
        imports = row["Imports (USD)"]
        if isinstance(exports, (int, float)) and isinstance(imports, (int, float)):
            row["Trade Balance (USD)"] = round(exports - imports, 2)
        else:
            row["Trade Balance (USD)"] = "N/A"
        row["Last Updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        records.append(row)
    return pd.DataFrame(records)

df = generate_saarc_tracker_data()
df.to_excel("India_SAARC_Tracker_Data.xlsx", index=False)
