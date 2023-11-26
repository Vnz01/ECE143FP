import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a DataFrame
data = pd.read_csv("../Downloaded Database/E2U(MinuteData2020).csv", header=None,
                   names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])

# Combine date and time columns and convert to datetime
data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])
data.set_index('datetime', inplace=True)

# Calculate logarithmic returns
data['log_returns'] = np.log(data['close'] / data['close'].shift(1))

# Resample daily and calculate daily volatility
daily_volatility = data['log_returns'].resample('D').std()

# Resample monthly and calculate average monthly volatility
monthly_volatility = daily_volatility.resample('M').mean()

# Plot the data
plt.bar(monthly_volatility.index.strftime('%B'), monthly_volatility.values)
plt.xlabel('Months')
plt.ylabel('Average Daily Volatility')
plt.title('Average Daily Volatility per Month in 2020')
plt.xticks(rotation=45)
plt.show()