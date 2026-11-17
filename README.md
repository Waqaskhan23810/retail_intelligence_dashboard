# Retail Intelligence Dashboard

This project provides a sales and profitability dashboard for retail performance analysis. It reads the cleaned retail dataset, applies filters, and presents KPIs and charts in a simple Streamlit interface.

## Features

- Sales and profit KPI overview
- Region and category filtering
- Customer age filtering
- Search by product, category, or region
- Timeline sales and profit trends
- Detailed order table for review

## Project structure

- `app.py` — Streamlit dashboard application
- `retail_filtered.csv` — retail transaction dataset
- `requirements.txt` — Python dependencies
- `tests/test_app.py` — smoke tests for data loading and summary logic

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:

   ```bash
   streamlit run app.py
   ```

4. Open the local URL shown by Streamlit in your browser.

## Data source

The dashboard uses the included retail dataset in `retail_filtered.csv`.

## Notes

This repository was cleaned and rebuilt into a proper runnable project instead of relying on a static exported HTML dashboard.
