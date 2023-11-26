# import pandas as pd
# import matplotlib.pyplot as plt

# dataArr = {}

# for x in range(12,23):
#     data = pd.read_csv(f'../Downloaded Database/E2U(MinuteData20{x}).csv', header=None, names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])

#     data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])

#     data.set_index('datetime', inplace=True)

#     data['returns'] = data['close'].pct_change()

#     daily_volatility = data['returns'].resample('D').std()

#     average_daily_volatility = daily_volatility.mean()

#     dataArr[f'Year 20{x}']=average_daily_volatility

# years = list(dataArr.keys())
# values = list(dataArr.values())

# plt.bar(years, values)
# plt.xlabel('Years')
# plt.ylabel('Values')
# plt.title('Average Daily Volatility for the past Decade')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
# plt.yscale('log')
# plt.show()





import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import numpy for logarithmic operations

dataArr = {}

for x in range(12, 23):
    data = pd.read_csv(f'../Downloaded Database/E2U(MinuteData20{x}).csv', header=None,
                       names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])

    data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])

    data.set_index('datetime', inplace=True)

    # Calculate logarithmic returns
    data['log_returns'] = np.log(data['close'] / data['close'].shift(1))

    daily_volatility = data['log_returns'].resample('D').std()

    average_daily_volatility = daily_volatility.mean()

    dataArr[f'20{x}'] = average_daily_volatility

years = list(dataArr.keys())
values = list(dataArr.values())

plt.bar(years, values)
plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Average Daily Volatility for the past Decade')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.yscale('log')
plt.show()
