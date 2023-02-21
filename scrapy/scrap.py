import requests
from bs4 import BeautifulSoup

baseUrl = 'https://fr.audiofanzine.com'
response = requests.get(baseUrl)
resultData = []
if response.ok:
    swoup = BeautifulSoup(response.text, 'html.parser')
    ul = swoup.find('ul')
    lis = ul.findAll('li')
    for li in lis:
        a = li.find('a')  
        resultData.append(baseUrl + a['href'])
print(resultData)
print(response.ok)