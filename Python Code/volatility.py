import pandas as pd

dataArr = {}

for x in range(12,23):
    data = pd.read_csv(f'../Downloaded Database/E2U(MinuteData20{x}).csv', header=None, names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])

    data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])

    data.set_index('datetime', inplace=True)

    data['returns'] = data['close'].pct_change()

    daily_volatility = data['returns'].resample('D').std()

    average_daily_volatility = daily_volatility.mean()

    dataArr[f'Year 20{x}']=average_daily_volatility

print(dataArr)