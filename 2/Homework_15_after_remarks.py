import requests
import pprint
from datetime import datetime


def currency_exchange(nbu_url):
    """This try/except check internet connection"""

    try:
        list_raw = requests.get(nbu_url)
    except requests.exceptions.ConnectionError:
        print('Check your internet connection')

    """This try/except check input data type and connection status code in range from 300-530"""
    try:
        list_raw = requests.get(nbu_url)
    except:
        list_raw = requests.get(nbu_url)
        if list_raw.headers['Content-Type'] != 'application/json; charset=utf-8':
            print(f'Your input datatype is not json!')
        elif list_raw.status_code in range(300, 530):
            print(f"Your have invalid status code")
        else:
            pass
    list_ready = list_raw.json()
    current_date = datetime.now().date()
    request_date = 'Дата створення запиту {}'.format(current_date)
    final_lst = []

    for i in list_ready:
        currency = i['txt']
        currency_cost = i["rate"]
        final_str = f'{currency} to UAH: {currency_cost}'
        final_lst.append(final_str)
    new_txt_file = open("result_file.txt", "w+")
    new_txt_file.write(request_date)
    new_txt_file.write(str(final_lst))
    new_txt_file.close()


currency_exchange('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
