import requests
from bs4 import BeautifulSoup

class AudioFanzine():
    def getUrlMain(self):
        resultDataUrl = []
        baseUrl = 'https://fr.audiofanzine.com'
        response = requests.get(baseUrl)
        if response.ok:
            swoup = BeautifulSoup(response.text, 'html.parser')
            ul = swoup.find('ul')
            lis = ul.findAll('li')
            for li in lis:
                a = li.find('a')  
                resultDataUrl.append(baseUrl + a['href'])
        print(resultDataUrl)

getUrl = AudioFanzine()
getUrl.getUrlMain()