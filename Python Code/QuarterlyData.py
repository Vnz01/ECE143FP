import matplotlib.pyplot as plt
import csv
import re
from datetime import datetime, timedelta

data = []
possibleCountry = []
chosenCountry = ""
dates = []
exchange_rates=[]

with open(f'../Downloaded Database/TreasuryQuarterlyData.csv','r') as fileCSV:
    csv_reader = csv.reader(fileCSV)

    next(csv_reader)

    for row in csv_reader:
        specificData = [row[3].upper(),datetime.strptime(row[5], '%Y-%m-%d'),float(row[4])]
        data.append(specificData)

    fileCSV.close()

for row in data:
    if(row[0] not in possibleCountry):
        possibleCountry.append(row[0])

for x in possibleCountry:
    print(x)

while(chosenCountry not in possibleCountry):
    print("\nPick a country:")
    chosenCountry = input().upper()

for row in data:
    if(row[0] == chosenCountry):
        dates.append(row[1])
        exchange_rates.append(row[2])



fig, ax = plt.subplots()

country = chosenCountry + ' Exchange Rate with USD (Quarterly)' 

ax.plot(dates, exchange_rates, label=country, marker='')

num_ticks = 10

if(len(dates) > num_ticks):
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