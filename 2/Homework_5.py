# pip install requests
import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'
dict_raw = requests.get(url)
dict_ready = dict_raw.json()
pprint(dict_ready)
print()


for key in dict_ready:
    for i in dict_ready[key]:
        # print(i)
        if i['completed'] is False:
            print(i['todo'])