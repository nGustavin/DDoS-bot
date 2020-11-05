# pip install --proxy=http://estag-nii:pantanal2020@proxypge01.pge.parana:8080 somepackage

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
import json
from lxml import html

proxies = {
    'http': 'http://estag-nii:pantanal2020@proxypge01.pge.parana:8080',
    'https': 'http://estag-nii:pantanal2020@proxypge01.pge.parana:8080',
}

url = 'https://afazenda.r7.com/a-fazenda-12/votacao'
counter = 1

while True:
    req = requests.get(url, proxies=proxies)
    body = req.text
    counter += 1
    print(counter, "requisicoes")
