# ECE 143 - Exchange Rates during Significant Times

This repository contains Python scripts for analyzing foreign exchange rates over specific periods, focusing on significant global events and their impact on currency values.

## File Structure

- **Downloaded Database**: Contains datasets extracted from the web.
- **Python Code**: Python scripts for data analysis and graph generation.

## How to Run the Code

1. Clone the repository:

git clone https://github.com/Vnz01/ECE143FP.git


2. Download the zip file and run the Python scripts in the terminal. These scripts produce specific graphs by accessing up to 16 different datasets.

## Scripts Overview

### `DataDailyMonthly.py`
- Reads `daily.csv` and `monthly.csv`.
- Prompts the user to choose a file, country, filter options, and start/end dates.
- Generates a graph comparing the chosen country's currency to USD.
- Analyzes currency strength and trends.

### `Eur_to_GB.py`
- Analyzes the EURO to GB exchange rate.
- Highlights data during the Brexit era.
- Provides detailed analysis of exchange rate fluctuations related to Brexit events.

### `eur_to_usd.py`
- Analyzes the EUR/USD exchange rate over a user-specified time period.
- Handles edge cases and input errors (e.g., end date earlier than start date).

### `gdp_analysis.py`
- Analyzes 10 countries' currency strengths relative to the EURO.
- Generates individual and collective graphs from `euro-daily-hist_1999_2022.csv`.

### `monthlyvol.py`
- Analyzes average daily volatility per month in 2020.
- Generates a histogram from `E2U(MinuteData2020).csv`.
- Useful for COVID-era analysis.

### `QuarterlyData.py`
- Produces quarterly data for various countries and currencies compared to USD.
- Sources data from the U.S. Treasury.

### `volatility.py`
- Calculates average daily volatility per year from 2012-2022.
- Uses data from CSV files starting with `E2U`.

### `APIRequest.py`
- (Commented out) Would call an API request from treasury.gov.
- Aimed to access specific filtered data but not used to avoid server overload.

## Third-party Modules

- `requests`
- `matplotlib.pyplot as plt`
- `numpy`
- `pandas`
- `csv`
- `re`
- `datetime` from `datetime`, `timedelta`
