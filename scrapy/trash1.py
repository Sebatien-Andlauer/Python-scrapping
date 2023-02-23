import requests
from bs4 import BeautifulSoup

baseUrl = 'https://fr.audiofanzine.com/annonces'
uri = '/annonces/'
response = requests.get(baseUrl)

def getEndpoint(swoup):
    resultData = []
    ul = swoup.find('ul')
    lis = ul.findAll('li')
    for li in lis:
        a = li.find('a')  
        resultData.append(baseUrl + a['href'])
    return resultData
if response.ok:
    swoup = BeautifulSoup(response.text, 'html.parser')
    autolink = getEndpoint(swoup)
 
print(len(resultData))
print(resultData)
print(response.ok)