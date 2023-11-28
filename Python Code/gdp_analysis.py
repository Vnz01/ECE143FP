import matplotlib.pyplot as plt
import pandas as pd
# Loading the provided dataset again
file_path = '/content/euro-daily-hist_1999_2022.csv'
rates = pd.read_csv(file_path)


"""USA"""
# Renaming the relevant columns for the United States (US Dollar)
rates = rates.rename(columns={'[US dollar ]': "euro_to_usd"})

# Selecting and cleaning the data for US Dollar
euro_to_usd = rates[["Period\\Unit:", "euro_to_usd"]].copy()
euro_to_usd = euro_to_usd.rename(columns={'Period\\Unit:': 'date'})
euro_to_usd['date'] = pd.to_datetime(euro_to_usd['date'])
euro_to_usd["euro_to_usd"] = pd.to_numeric(euro_to_usd['euro_to_usd'], errors='coerce')
euro_to_usd = euro_to_usd.dropna(subset=['euro_to_usd'])
euro_to_usd = euro_to_usd.reset_index(drop=True)

# Adding a rolling mean column
euro_to_usd['rolling_mean'] = euro_to_usd['euro_to_usd'].rolling(50).mean()
euro_to_usd = euro_to_usd.dropna(subset=['rolling_mean'])

# Calculating the strength of the US Dollar against the Euro
euro_to_usd['usd_to_eur'] = 1/euro_to_usd['rolling_mean']

# Display basic info and plot
euro_to_usd.info()
plt.figure(figsize=(10, 4))
plt.plot(euro_to_usd['date'], euro_to_usd['usd_to_eur'])
plt.title('USD Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('USD to EUR')
plt.show()



"""CHINA"""


# Renaming the relevant columns for China (Chinese Yuan Renminbi)
rates = rates.rename(columns={'[Chinese yuan renminbi ]': "euro_to_cny"})

# Selecting and cleaning the data for Chinese Yuan
euro_to_cny = rates[["Period\\Unit:", "euro_to_cny"]].copy()
euro_to_cny = euro_to_cny.rename(columns={'Period\\Unit:': 'date'})
euro_to_cny['date'] = pd.to_datetime(euro_to_cny['date'])
euro_to_cny["euro_to_cny"] = pd.to_numeric(euro_to_cny['euro_to_cny'], errors='coerce')
euro_to_cny = euro_to_cny.dropna(subset=['euro_to_cny'])
euro_to_cny = euro_to_cny.reset_index(drop=True)

# Adding a rolling mean column for Chinese Yuan
euro_to_cny['rolling_mean'] = euro_to_cny['euro_to_cny'].rolling(50).mean()
euro_to_cny = euro_to_cny.dropna(subset=['rolling_mean'])

# Calculating the strength of the Chinese Yuan against the Euro
euro_to_cny['cny_to_eur'] = 1/euro_to_cny['rolling_mean']

# Plotting the strength of the Chinese Yuan against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_cny['date'], euro_to_cny['cny_to_eur'])
plt.title('CNY Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('CNY to EUR')
plt.show()

"""JAPAN"""

# Renaming the relevant columns for Japan (Japanese Yen)
rates = rates.rename(columns={'[Japanese yen ]': "euro_to_jpy"})

# Selecting and cleaning the data for Japanese Yen
euro_to_jpy = rates[["Period\\Unit:", "euro_to_jpy"]].copy()
euro_to_jpy = euro_to_jpy.rename(columns={'Period\\Unit:': 'date'})
euro_to_jpy['date'] = pd.to_datetime(euro_to_jpy['date'])
euro_to_jpy["euro_to_jpy"] = pd.to_numeric(euro_to_jpy['euro_to_jpy'], errors='coerce')
euro_to_jpy = euro_to_jpy.dropna(subset=['euro_to_jpy'])
euro_to_jpy = euro_to_jpy.reset_index(drop=True)

# Adding a rolling mean column for Japanese Yen
euro_to_jpy['rolling_mean'] = euro_to_jpy['euro_to_jpy'].rolling(50).mean()
euro_to_jpy = euro_to_jpy.dropna(subset=['rolling_mean'])

# Calculating the strength of the Japanese Yen against the Euro
euro_to_jpy['jpy_to_eur'] = 1/euro_to_jpy['rolling_mean']

# Plotting the strength of the Japanese Yen against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_jpy['date'], euro_to_jpy['jpy_to_eur'])
plt.title('JPY Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('JPY to EUR')
plt.show()


"""UNITED KINGDOM"""

# Renaming the relevant columns for the United Kingdom (Pound Sterling)
rates = rates.rename(columns={'[UK pound sterling ]': "euro_to_gbp"})

# Selecting and cleaning the data for Pound Sterling
euro_to_gbp = rates[["Period\\Unit:", "euro_to_gbp"]].copy()
euro_to_gbp = euro_to_gbp.rename(columns={'Period\\Unit:': 'date'})
euro_to_gbp['date'] = pd.to_datetime(euro_to_gbp['date'])
euro_to_gbp["euro_to_gbp"] = pd.to_numeric(euro_to_gbp['euro_to_gbp'], errors='coerce')
euro_to_gbp = euro_to_gbp.dropna(subset=['euro_to_gbp'])
euro_to_gbp = euro_to_gbp.reset_index(drop=True)

# Adding a rolling mean column for Pound Sterling
euro_to_gbp['rolling_mean'] = euro_to_gbp['euro_to_gbp'].rolling(50).mean()
euro_to_gbp = euro_to_gbp.dropna(subset=['rolling_mean'])

# Calculating the strength of the Pound Sterling against the Euro
euro_to_gbp['gbp_to_eur'] = 1/euro_to_gbp['rolling_mean']

# Plotting the strength of the Pound Sterling against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_gbp['date'], euro_to_gbp['gbp_to_eur'])
plt.title('GBP Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('GBP to EUR')
plt.show()


"""INDIA"""

# Renaming the relevant columns for India (Indian Rupee)
rates = rates.rename(columns={'[Indian rupee ]': "euro_to_inr"})

# Selecting and cleaning the data for Indian Rupee
euro_to_inr = rates[["Period\\Unit:", "euro_to_inr"]].copy()
euro_to_inr = euro_to_inr.rename(columns={'Period\\Unit:': 'date'})
euro_to_inr['date'] = pd.to_datetime(euro_to_inr['date'])
euro_to_inr["euro_to_inr"] = pd.to_numeric(euro_to_inr['euro_to_inr'], errors='coerce')
euro_to_inr = euro_to_inr.dropna(subset=['euro_to_inr'])
euro_to_inr = euro_to_inr.reset_index(drop=True)

# Adding a rolling mean column for Indian Rupee
euro_to_inr['rolling_mean'] = euro_to_inr['euro_to_inr'].rolling(50).mean()
euro_to_inr = euro_to_inr.dropna(subset=['rolling_mean'])

# Calculating the strength of the Indian Rupee against the Euro
euro_to_inr['inr_to_eur'] = 1/euro_to_inr['rolling_mean']

# Plotting the strength of the Indian Rupee against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_inr['date'], euro_to_inr['inr_to_eur'])
plt.title('INR Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('INR to EUR')
plt.show()


"""BRAZIL"""

# Renaming the relevant columns for Brazil (Brazilian Real)
rates = rates.rename(columns={'[Brazilian real ]': "euro_to_brl"})

# Selecting and cleaning the data for Brazilian Real
euro_to_brl = rates[["Period\\Unit:", "euro_to_brl"]].copy()
euro_to_brl = euro_to_brl.rename(columns={'Period\\Unit:': 'date'})
euro_to_brl['date'] = pd.to_datetime(euro_to_brl['date'])
euro_to_brl["euro_to_brl"] = pd.to_numeric(euro_to_brl['euro_to_brl'], errors='coerce')
euro_to_brl = euro_to_brl.dropna(subset=['euro_to_brl'])
euro_to_brl = euro_to_brl.reset_index(drop=True)

# Adding a rolling mean column for Brazilian Real
euro_to_brl['rolling_mean'] = euro_to_brl['euro_to_brl'].rolling(50).mean()
euro_to_brl = euro_to_brl.dropna(subset=['rolling_mean'])

# Calculating the strength of the Brazilian Real against the Euro
euro_to_brl['brl_to_eur'] = 1/euro_to_brl['rolling_mean']

# Plotting the strength of the Brazilian Real against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_brl['date'], euro_to_brl['brl_to_eur'])
plt.title('BRL Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('BRL to EUR')
plt.show()


"""CANADA"""
# Renaming the relevant columns for Canada (Canadian Dollar)
rates = rates.rename(columns={'[Canadian dollar ]': "euro_to_cad"})

# Selecting and cleaning the data for Canadian Dollar
euro_to_cad = rates[["Period\\Unit:", "euro_to_cad"]].copy()
euro_to_cad = euro_to_cad.rename(columns={'Period\\Unit:': 'date'})
euro_to_cad['date'] = pd.to_datetime(euro_to_cad['date'])
euro_to_cad["euro_to_cad"] = pd.to_numeric(euro_to_cad['euro_to_cad'], errors='coerce')
euro_to_cad = euro_to_cad.dropna(subset=['euro_to_cad'])
euro_to_cad = euro_to_cad.reset_index(drop=True)

# Adding a rolling mean column for Canadian Dollar
euro_to_cad['rolling_mean'] = euro_to_cad['euro_to_cad'].rolling(50).mean()
euro_to_cad = euro_to_cad.dropna(subset=['rolling_mean'])

# Calculating the strength of the Canadian Dollar against the Euro
euro_to_cad['cad_to_eur'] = 1/euro_to_cad['rolling_mean']

# Plotting the strength of the Canadian Dollar against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_cad['date'], euro_to_cad['cad_to_eur'])
plt.title('CAD Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('CAD to EUR')
plt.show()


"""RUSSIA"""
# Renaming the relevant columns for Russia (Russian Rouble)
rates = rates.rename(columns={'[Russian rouble ]': "euro_to_rub"})

# Selecting and cleaning the data for Russian Rouble
euro_to_rub = rates[["Period\\Unit:", "euro_to_rub"]].copy()
euro_to_rub = euro_to_rub.rename(columns={'Period\\Unit:': 'date'})
euro_to_rub['date'] = pd.to_datetime(euro_to_rub['date'])
euro_to_rub["euro_to_rub"] = pd.to_numeric(euro_to_rub['euro_to_rub'], errors='coerce')
euro_to_rub = euro_to_rub.dropna(subset=['euro_to_rub'])
euro_to_rub = euro_to_rub.reset_index(drop=True)

# Adding a rolling mean column for Russian Rouble
euro_to_rub['rolling_mean'] = euro_to_rub['euro_to_rub'].rolling(50).mean()
euro_to_rub = euro_to_rub.dropna(subset=['rolling_mean'])

# Calculating the strength of the Russian Rouble against the Euro
euro_to_rub['rub_to_eur'] = 1/euro_to_rub['rolling_mean']

# Plotting the strength of the Russian Rouble against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_rub['date'], euro_to_rub['rub_to_eur'])
plt.title('RUB Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('RUB to EUR')
plt.show()

"""SOUTH KOREA"""
# Renaming the relevant columns for South Korea (Korean Won)
rates = rates.rename(columns={'[Korean won ]': "euro_to_krw"})

# Selecting and cleaning the data for Korean Won
euro_to_krw = rates[["Period\\Unit:", "euro_to_krw"]].copy()
euro_to_krw = euro_to_krw.rename(columns={'Period\\Unit:': 'date'})
euro_to_krw['date'] = pd.to_datetime(euro_to_krw['date'])
euro_to_krw["euro_to_krw"] = pd.to_numeric(euro_to_krw['euro_to_krw'], errors='coerce')
euro_to_krw = euro_to_krw.dropna(subset=['euro_to_krw'])
euro_to_krw = euro_to_krw.reset_index(drop=True)

# Adding a rolling mean column for Korean Won
euro_to_krw['rolling_mean'] = euro_to_krw['euro_to_krw'].rolling(50).mean()
euro_to_krw = euro_to_krw.dropna(subset=['rolling_mean'])

# Calculating the strength of the Korean Won against the Euro
euro_to_krw['krw_to_eur'] = 1/euro_to_krw['rolling_mean']

# Plotting the strength of the Korean Won against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_krw['date'], euro_to_krw['krw_to_eur'])
plt.title('KRW Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('KRW to EUR')
plt.show()


"""AUSTRALIA"""
# Renaming the relevant columns for Australia (Australian Dollar)
rates = rates.rename(columns={'[Australian dollar ]': "euro_to_aud"})

# Selecting and cleaning the data for Australian Dollar
euro_to_aud = rates[["Period\\Unit:", "euro_to_aud"]].copy()
euro_to_aud = euro_to_aud.rename(columns={'Period\\Unit:': 'date'})
euro_to_aud['date'] = pd.to_datetime(euro_to_aud['date'])
euro_to_aud["euro_to_aud"] = pd.to_numeric(euro_to_aud['euro_to_aud'], errors='coerce')
euro_to_aud = euro_to_aud.dropna(subset=['euro_to_aud'])
euro_to_aud = euro_to_aud.reset_index(drop=True)

# Adding a rolling mean column for Australian Dollar
euro_to_aud['rolling_mean'] = euro_to_aud['euro_to_aud'].rolling(50).mean()
euro_to_aud = euro_to_aud.dropna(subset=['rolling_mean'])

# Calculating the strength of the Australian Dollar against the Euro
euro_to_aud['aud_to_eur'] = 1/euro_to_aud['rolling_mean']

# Plotting the strength of the Australian Dollar against the Euro
plt.figure(figsize=(10, 4))
plt.plot(euro_to_aud['date'], euro_to_aud['aud_to_eur'])
plt.title('AUD Strength Against EUR (Rolling Mean)')
plt.xlabel('Date')
plt.ylabel('AUD to EUR')
plt.show()



"""Combined Plot"""

# Combining the currency strength data for all the mentioned countries
combined_data = pd.DataFrame({
    'Date': euro_to_usd['date'],
    'USD to EUR': euro_to_usd['usd_to_eur'],
    'CNY to EUR': euro_to_cny['cny_to_eur'],
    'JPY to EUR': euro_to_jpy['jpy_to_eur'],
    'INR to EUR': euro_to_inr['inr_to_eur'],
    'GBP to EUR': euro_to_gbp['gbp_to_eur'],
    'BRL to EUR': euro_to_brl['brl_to_eur'],
    'CAD to EUR': euro_to_cad['cad_to_eur'],
    'RUB to EUR': euro_to_rub['rub_to_eur'],
    'KRW to EUR': euro_to_krw['krw_to_eur'],
    'AUD to EUR': euro_to_aud['aud_to_eur']
})

# Plotting the combined data
plt.figure(figsize=(15, 8))
for currency in combined_data.columns[1:]:
    plt.plot(combined_data['Date'], combined_data[currency], label=currency)

plt.title('Currency Strength Against EUR (2005-2023)')
plt.xlabel('Date')
plt.ylabel('Currency to EUR')
plt.legend()
plt.show()
