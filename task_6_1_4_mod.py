import os
import re
import requests
from decor import time_size


@time_size
def parsed(url):
    raw = re.compile(r'(\d+\.\d+\.\d+\.\d+) . . .([^\]]*). .(\w+) ([^\"]*). (\d+) (\d+)')
    resp = requests.get(url).text
    return (str(parsed_raw) for parsed_raw in raw.findall(resp))


url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# print('\n'.join(parsed(url)))

r, m, t = parsed(url)
print(os.path.basename(__file__))
print(f'{m} MiB', f'{t} sec', sep='\n')
