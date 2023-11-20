import requests

api_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange?fields=country,exchange_rate, record_date&filter=record_date:gte:2000-01-01"

parameters = {
    'fields': 'country,exchange_rate,record_date',
}

all_data = []

page_number = 1

## DO NOT RUN WILL MAKE TOO MANY API REQUESTS

# while True:

#     parameters['page[number]'] = page_number

#     response = requests.get(api_url, params=parameters)

#     if response.status_code == 200:

#         data = response.json()

#         if 'data' in data:
#             exchange_rates_data = data['data']

#             all_data.extend(exchange_rates_data)

#             links = data.get('links', {})
#             if 'next' not in links:
#                 break
#             else:
#                 page_number += 1
#         else:
#             print("No 'data' key found in the response.")
#             break
#     else:
#         print(f"Error: {response.status_code}")
#         break
