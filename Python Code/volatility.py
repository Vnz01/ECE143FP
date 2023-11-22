import pandas as pd

### Change File Path for each dataset

'../Downloaded Database/E2U(MinuteData2012).csv'
'../Downloaded Database/E2U(MinuteData2013).csv'
'../Downloaded Database/E2U(MinuteData2014).csv'
'../Downloaded Database/E2U(MinuteData2015).csv'
'../Downloaded Database/E2U(MinuteData2016).csv'
'../Downloaded Database/E2U(MinuteData2017).csv'
'../Downloaded Database/E2U(MinuteData2018).csv'
'../Downloaded Database/E2U(MinuteData2019).csv'
'../Downloaded Database/E2U(MinuteData2020).csv'
'../Downloaded Database/E2U(MinuteData2021).csv'
'../Downloaded Database/E2U(MinuteData2022).csv'

data = pd.read_csv('../Downloaded Database/E2U(MinuteData2020).csv', header=None, names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])

data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])

data.set_index('datetime', inplace=True)

data['returns'] = data['close'].pct_change()

daily_volatility = data['returns'].resample('D').std()

average_daily_volatility = daily_volatility.mean()

print("Average Daily Volatility:", average_daily_volatility)