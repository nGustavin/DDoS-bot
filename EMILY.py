import requests
import json
from lxml import html


url = 'https://www.google.com'
counter = 1

while True:
    req = requests.get(url)
    body = req.text
    counter += 1
    print(counter, "requests")
