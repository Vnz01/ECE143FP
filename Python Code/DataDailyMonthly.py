import matplotlib.pyplot as plt
import numpy
import pandas
import csv
import re
from datetime import datetime, timedelta

def dateValidation(date_str, dayMonth):
    '''
    Function that takes in a string and int. It checks if the date string is in proper format or not

    Parameters: date1_str string and dayMonth int

    Return: bool T or F
    '''
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    
    if not bool(pattern.match(date_str)):
        return False
    
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        if(dayMonth == "1"):
            lower_bound = datetime(1971, 1, 1)
        else:
            lower_bound = datetime(1971, 1, 4)
        upper_bound = datetime(2017, 12, 1)
        return lower_bound <= date_obj <= upper_bound
    except ValueError:
        return False  # Invalid date

def monthApart(date1_str, date2_str):
    '''
    Function that takes in two formatted date string and check if they are a month apart

    Parameters: date1_str and date2_str of type string

    Return: bool T or F
    '''
    date_format = "%Y-%m-%d"

    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    month_difference = (date2.year - date1.year) * 12 + date2.month - date1.month

    return abs(month_difference) == 1

data = []
possibleCountry = []
country = ''
fileOpen = -1
filt = -1
looper1 = False
looper2 = False
looper3 = False

# User Interface to check which file to open
print("1. Monthly")
print("2. Daily")
while(fileOpen != "1" and fileOpen != "2"):
    print('Enter "1" or "2"')
    fileOpen = input()
    print(" ")

# Sets values to fileString
if(fileOpen == "1"):
    fileString = "monthly"
elif(fileOpen == "2"):
    fileString = "daily"

# Opens corresponding file
with open(f'../Downloaded Database/{fileString}.csv','r') as fileCSV:
    csv_reader = csv.reader(fileCSV)

    # Find all possible countries in dataset
    for row in csv_reader:
        if(row[1] not in possibleCountry):
            if(row[1] != 'Country'):
                possibleCountry.append(row[1])

    # User Interface to print all possible countries
    for i in possibleCountry:
        print(i)
    print(' ')
    fileCSV.seek(0)
    print('Enter a Country:')
    country = input()
    print(" ")
    while country not in possibleCountry:
        print('(Space and Case Sensitive) Enter a Country:')
        country = input()
        print(" ")

    # Get Data for Selected Country
    for row in csv_reader:
        if(row[1] == country):
            data.append(row)

# USER INPUT TO FILTER DATES
while(filt != "1" and filt != "2"):
    print("1. Don't Filter")
    print("2. Filter Dates")
    print('Enter "1" or "2":')
    filt = input()
    print(" ")

# Ask user to filter dates or not
if(filt == "1"):
    start_date = "1971-01-01" if fileOpen == "1" else "1971-01-04"
    end_date = "2017-12-01"
if(filt =="2"): 
    if(fileOpen == "1"):
        while(not looper3):
            while(not looper1):
                stringStart= "1971-01-01" if fileOpen == "1" else "1971-01-04"
                print(f"Earliest is ({stringStart})")
                print("Enter Start Date in format (YYYY-MM-DD):")
                start_date = input()
                print(" ")
                looper1 = dateValidation(start_date, fileOpen)
            while(not looper2):
                print("Latest is (2017-12-01)")
                print("enter END date in format (YYYY-MM-DD):")
                end_date = input()
                print(" ")
                looper2 = dateValidation(end_date, fileOpen)
            looper3 = monthApart(start_date,end_date)
            if(not looper3):
                print("Dates are not a month apart\n")
                looper1 = False
                looper2 = False
    elif(fileOpen == "2"):
        while(not looper1):
            stringStart= "1971-01-01" if fileOpen == "1" else "1971-01-04"
            print(f"Earliest is ({stringStart})")
            print("Enter Start Date in format (YYYY-MM-DD):")
            start_date = input()
            print(" ")
            looper1 = dateValidation(start_date, fileOpen)
        while(not looper2):
            print("Latest is (2017-12-01)")
            print("enter END date in format (YYYY-MM-DD):")
            end_date = input()
            print(" ")
            looper2 = dateValidation(end_date, fileOpen)

dates = [entry[0] for entry in data]
exchange_rates = [float(entry[2]) if entry[2].replace('.', '', 1).isdigit() else 0.0 for entry in data]

# Fill DATA holes with the previous data
for i in range(len(exchange_rates)):
    if(i != 0):
        if(exchange_rates[i] == 0.0):
            exchange_rates[i] = exchange_rates[i-1]

filtered_data = [(date, rate) for date, rate in zip(dates, exchange_rates) if start_date <= date <= end_date]

if not filtered_data:
    raise ValueError("No data found for the specified date range.")

dates, exchange_rates = zip(*filtered_data)

#Plot code
fig, ax = plt.subplots()

country = country + ' Exchange Rate with USD (' + fileString + ')' 

ax.plot(dates, exchange_rates, label=country, marker='o')

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