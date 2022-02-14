import os
import requests
import xmltodict
from decimal import *
from decor import time_size


@time_size
def currency_rates(cur):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    data = xmltodict.parse(resp)
    for i in data['ValCurs']['Valute']:
        if i['CharCode'] == cur:
            return f'{i["CharCode"]} {i["Name"]} {Decimal(i["Value"].replace(",", "."))}'


if __name__ == '__main__':
    #cur = input('Введите код валюты в формате USD, EUR, GBP, ... ').upper()
    #cr = currency_rates(cur)
    #print(cr)

    cur = 'EUR'
    r, m, t = currency_rates(cur)
    print(os.path.basename(__file__))
    print(f'{m} MiB', f'{t} sec', sep='\n')
