import requests
from bs4 import BeautifulSoup
import csv

resultDataUrl = []
baseUrl = 'https://fr.audiofanzine.com'
uri = '/annonces'
exploitUrl = baseUrl + uri

class AudioFanzine(object):
 
    def getEndpoints(swoup):
        links = []
        ul = swoup.find('ul')
        lis = ul.findAll('li')
        for li in lis:
            a = li.find('a')  
            links.append(baseUrl + a['href'])
        return links

    def getInfoByPage(swoup):
        infosTriees = [swoup]
        return infosTriees  
    
    def fileReader(file):
        result = []
        with open(file, 'r', encoding="UTF8", newline="") as f:
            reader = csv.DictReader(f)
            for line in reader:
                result.append(line) 
        return result

    def fileWriter(file, data):
        print(type(data))
        csv.register_dialect('myDialect',
                     delimiter='|',
                     quoting=csv.QUOTE_ALL)
        with open(file, 'w', encoding="UTF8", newline='') as f:
            writer = csv.writer(f, dialect='myDialect')
            writer.writerows(data)
            
        # return 
        return True

    def main(url, process):
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            return process(soup)
        return []

    # exec des fonctions
    endpoints = main(exploitUrl, getEndpoints)
    resultDataUrl.extend(endpoints)

    fileWriter('links.csv', resultDataUrl)

# exec de la classe
AudioFanzine()

# getUrl = AudioFanzine()
# endpoints = getUrl.main(exploitUrl, getEndpoints)
# print(endpoints)
