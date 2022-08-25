import requests
import pprint
from datetime import datetime

nbu_url = ' https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json '
list_raw = requests.get(nbu_url)
list_ready = list_raw.json()
current_date = datetime.now().date()
print(f'Дата створення запиту {current_date}')
final_lst = []

for i in list_ready:
    currency = i['txt']
    currency_cost = i["rate"]
    final_str = f'{currency} to UAH: {currency_cost}'
    final_lst.append(final_str)
print(final_lst)




