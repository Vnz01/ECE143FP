import matplotlib.pyplot as plt
import csv
import re
from datetime import datetime, timedelta

def dateValidation(date_str):
    '''
    Function that takes in a string and int. It checks if the date string is in proper format or not

    Parameters: date1_str string and dayMonth int

    Return: bool T or F
    '''
    pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    
    if not bool(pattern.match(date_str)):
        return False
    
    try:
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        lower_bound = datetime(1990, 1, 2)
        upper_bound = datetime(2023, 11, 20)
        return lower_bound <= date_obj <= upper_bound
    except ValueError:
        return False  # Invalid date

rate = []
date = []
startDate = ""
endDate = ""

with open(f'../Downloaded Database/eur_to_usd.csv','r') as fileCSV:
    if(csv.reader(fileCSV)):
        csv_reader = csv.reader(fileCSV)
    else:
        raise Exception("Unable to read file")
    
    next(csv_reader)

    for row in csv_reader:
        date.append(row[0])
        rate.append(float(row[1]))

    fileCSV.close()

rate = rate[::-1]
date = date[::-1]

while(not dateValidation(startDate)):
    print("Between 01/02/1990 and 11/20/2023")
    print('Enter Start Date in format "MM/DD/YYYY":')
    startDate = input()
    print("\n")
while(not dateValidation(endDate)):
    print("Between 01/02/1990 and 11/20/2023")
    print('Enter End Date in format "MM/DD/YYYY":')
    endDate = input()
    print("\n")

start_datetime = datetime.strptime(startDate, '%m/%d/%Y')
end_datetime = datetime.strptime(endDate, '%m/%d/%Y')

filtered_rate = []
filtered_date = []

for d, r in zip(date, rate):
    date_obj = datetime.strptime(d, '%m/%d/%Y')
    if start_datetime <= date_obj <= end_datetime:
        filtered_date.append(d)
        filtered_rate.append(r)

rate = filtered_rate
date = filtered_date

#Plot code
fig, ax = plt.subplots()

dataLabel = 'EUR TO USD EXCHANGE RATE'

ax.plot(date, rate, label=dataLabel, marker='')

num_ticks = 10

if(len(date) > num_ticks):
    step = len(date) // num_ticks

    date_labels = date[::step]

    ax.set_xticks(date_labels)

plt.xticks(rotation=45)

ax.set_xlabel('Dates')
ax.set_ylabel('USD per EUR')
ax.set_title(dataLabel)

ax.legend()

plt.tight_layout()
plt.show()
