import matplotlib.pyplot as plt
import numpy
import pandas
import csv

data = []
country = 'United Kingdom'

with open('../Downloaded Database/monthly.csv','r') as monthlyCSV:
    csv_reader = csv.reader(monthlyCSV)
    for row in csv_reader:
        if(row[1] == country):
            data.append(row)

dates = [entry[0] for entry in data]
exchange_rates = [float(entry[2]) for entry in data]

fig, ax = plt.subplots()

country = country + ' Exchange Rate with USD'

ax.plot(dates, exchange_rates, label=country, marker='o')

num_ticks = 10

step = len(dates) // num_ticks

date_labels = dates[::step]

ax.set_xticks(date_labels)

plt.xticks(rotation=45)

ax.set_xlabel('Dates')
ax.set_ylabel('Exchange Rate')
ax.set_title(country)

ax.legend()

plt.tight_layout()
plt.show()