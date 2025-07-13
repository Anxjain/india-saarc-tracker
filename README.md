
# India–SAARC Trade & Investment Tracker (Live World Bank Data)

This is a simple tracker that shows **live trade and FDI data (in USD)** between India and SAARC countries. It uses **official data from the World Bank**, displayed using a clean web app interface powered by **Streamlit**.

---

## 📦 What's Included

- `india_saarc_data_script.py` → Fetches latest exports, imports, FDI inflow/outflow from the World Bank API and saves to Excel.
- `india_saarc_streamlit_app.py` → Streamlit app that shows the data in a web dashboard and allows live refresh.

---

## 🧑‍💻 No Python Experience? No Problem!

Follow these **simple steps** to run it on your computer.

---

## ✅ Step 1: Install Python

Download and install Python from the official website:  
👉 https://www.python.org/downloads/

Make sure to check the box **"Add Python to PATH"** during installation.

---

## ✅ Step 2: Download Project Files

Download these two files and place them in one folder:
- `india_saarc_data_script.py`
- `india_saarc_streamlit_app.py`

---

## ✅ Step 3: Open Command Prompt (Terminal)

Navigate to the folder where you saved the files. Example:

```
cd Desktop\india-saarc-tracker
```

---

## ✅ Step 4: Install Required Libraries

Copy and paste this in the terminal:

```
pip install streamlit pandas openpyxl requests
```

This will install all necessary packages.

---

## ✅ Step 5: Launch the Tracker

Run this command:

```
streamlit run india_saarc_streamlit_app.py
```

Your browser will open with the live tracker showing updated data from the World Bank. Click the **"Refresh Data"** button anytime to fetch the latest numbers.

---

## 🧮 Output Example

- Exports, Imports, FDI values shown **in Millions of USD**
- Trade Balance is calculated as `Exports − Imports`
- All data is auto-fetched from World Bank — **no manual data entry**

---

## 💬 Support

If you face issues, make sure:
- Your internet connection is working (World Bank API needs online access)
- Python and libraries are installed correctly

Enjoy your tracker!
