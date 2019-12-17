import requests

URL = 'https://lohasnet.tw/SHAPARUN2020/'
page = requests.get(URL)

pprint(page);