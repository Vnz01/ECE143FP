import matplotlib.pyplot as plt
import numpy
import pandas
import csv

data = []
possibleCountry = []
country = ''

with open('../Downloaded Database/monthly.csv','r') as monthlyCSV:
    csv_reader = csv.reader(monthlyCSV)
    for row in csv_reader:
        if(row[1] not in possibleCountry):
            if(row[1] != 'Country'):
                possibleCountry.append(row[1])
monthlyCSV.close()

for i in possibleCountry:
    print(i)
print(' ')
print('Enter a Country:')
while country not in possibleCountry:
    country = input()

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