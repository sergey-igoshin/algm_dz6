import os
import requests
import xmltodict
from decimal import *
from decor import time_size


@time_size
def currency_rates(cur):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    data = xmltodict.parse(resp)
    return filter(lambda x: x['CharCode'] == cur, data['ValCurs']['Valute'])


if __name__ == '__main__':
    # cur = input('Введите код валюты в формате USD, EUR, GBP, ... ').upper()
    # c = list(currency_rates(cur))[0]
    # print(f'{c["CharCode"]} {c["Name"]} {Decimal(c["Value"].replace(",", "."))}')

    cur = 'JPY'
    r, m, t = currency_rates(cur)
    print(os.path.basename(__file__))
    print(f'{m} MiB', f'{t} sec', sep='\n')
