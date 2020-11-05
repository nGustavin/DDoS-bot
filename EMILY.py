import requests
import json
from lxml import html

proxies = {
    'http': 'http://estag-nii:pantanal2020@proxypge01.pge.parana:8080',
    'https': 'http://estag-nii:pantanal2020@proxypge01.pge.parana:8080',
}

url = 'https://www.gsmcelulares.com.br/'
counter = 1

while True:
    req = requests.get(url, proxies=proxies)
    body = req.text
    counter += 1
    print(counter, "requisicoes")
