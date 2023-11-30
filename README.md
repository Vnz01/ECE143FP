# ECE 143 - Exchange Rates during Significant Times

## File Structure:

> 2 Folders in the same directory, one titled Downloaded Database, another Python Code. These Python scripts call datasets that we extract from the web. Foreign Exchange rates over a certain time period

# How to run code?

> Git Clone https://github.com/Vnz01/ECE143FP.git

##

> Download zip file (run the python script, in terminal, needed to produce specific graphs accessing up to 16 different datasets)

# What do they do?

## DataDailyMonthly.py:

> Opens daily.csv and monthly.csv. Reads data and finds the unique countries available. Prompts, user to choose a daily or monthly file, a country, filter or not filter,start/end date. It outputs a graph with the chosen country currency compared to the USD. Used to analyze strength of currencies on specific dates, or make inferences on trends.

## Eur_to_GB.py:

> Opens Eur_to_GB.csv. After file is called, it outputs a graph of the EURO to the GB and highlights data during the time of the Brexit ERA. It also produces another graph, providing a closer look into the Brexit Era and highlights specific dates and events that happened during the time. Giving an analysis on how the exchange rate was affected at this time.

## eur_to_usd.py:

> This python script opens eur_to_usd.py. Users are prompt in the terminal to choose a specific start date and end date and outputs a graph of the EUR/USD over the time period specified. Closer analysis on dates and exchange rates. Edge cases and errors are accounted for, but there may be a bug with input end date being earlier than the input start date

## gdp_analaysis.py:

> This python script opens euro-daily-hist_1999_2022.csv and produce graphs of 10 countries currency's relative strength compared to the EURO. Produces 10 individual graphs and one graph with all the data overlapping.

## monthlyvol.py:

> This python scripts opens E2U(MinuteData2020).csv and produces a histogram for average daily volatility per month in 2020. Used for analysis for Covid Era.

## QuarterlyData.py:

> Python scripts outputs quarterly data for many different countries and currencies compared to USD. Very reliable data from the treasury although only quarterly data.

## volatility.py:

> Python scripts opens 11 different CSV files starting with E2U, to calculate the average daily volatility per year in the past decade. Starting from 2012-2022.

## APIRequest.py:

> Won't do anything. Script commented out. Although the script will call an API Request from treasury.gov to access specific filtered data. Not needed since we need mass amounts of data, and we don't want to flood open servers with large amounts of requests
