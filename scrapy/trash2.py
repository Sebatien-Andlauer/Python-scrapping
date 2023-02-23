import requests
from bs4 import BeautifulSoup
import csv

resultData = []
baseUrl = 'https://fr.audiofanzine.com'
uri = '/petites-annonces'

class Audiofanzine:
    def __init__(self, baseUrl, uri, resultData):
        print("init Class True")
        self.exploitUrl = baseUrl + uri
        self.resultDataUrl = resultData

    def getEndpoints(swoup):

        print('init fonction getEndpoints')
        links = []
        divP = swoup.find('div', {"class":"cmps-tabs"})
        divFC = divP.findAll('div', {"class":"cmps-tabs-col"})
        for a in divFC:
            a = a.find('a')  
            links.append(baseUrl + a['href'])
        for endpoint in links:
            self.resultData.append({'link': endpoint})
        return links

    def getInfoByPage(swoup):

        print('init fonction getInfoByPage')
        fiches = []
        contacts = soup.find("div",{"class": "coordonnees"})
        if contacts is not None:
            tabs = contacts.findAll('li', {"class": "accordeon-item"})
            if tabs is not None:
                for contact in tabs:
                    name = tryToCleanOrReturnBlank(contact.find("div", {"class": "accordeon-header"}))
                    coord = contact.find("div", {"class": "accordeon-body"})
                    adress = coord.find("p")
                    tel = tryToCleanOrReturnBlank(coord.find("a", {"class": "tel"}))
                    email = tryToCleanOrReturnBlank(coord.find("a", {"class": "email"}))
                    title = tryToCleanOrReturnBlank(soup.find("title"))
                    
                    try:
                        adress = adress.getText()
                        cleanArrAdress = []
                        for ele in str(adress).split("\n"):
                            if ele != "":
                                    cleanArrAdress.append(ele.strip())
                        
                        realAdress = cleanArrAdress[0]
                        realCC = cleanArrAdress[1]
                        realCountry = cleanArrAdress[2]
                    except:
                        adress = ""
                        realAdress =""
                        realCC =""
                        realCountry =""
                        cleanArrAdress = []


                    fiche = { 
                    "name": name, 
                    "adress": " ".join(cleanArrAdress),
                    "realAdress": realAdress,
                    "departement":realCC,
                    "country": realCountry,
                    "tel": tel,
                    "email": email, 
                    "title": title.replace(' - Studyrama', "")
                    }
                    fiches.append(fiche)
        return fiches 
    def tryToCleanOrReturnBlank(str):

        print('init fonction Clean or return blank')
        try:
            result = str.getText().strip()
        except:
            result = ''
        return result

    def fileReader(file):

        print('init fonction fileReader')
        result = []
        with open(file, 'r', encoding="UTF8", newline="") as f:
            reader = csv.DictReader(f)
            for line in reader:
                result.append(line) 
        return result

    def fileWriter(file, self, process):

        print('init fonction file writer')
        with open(file, 'w', encoding="UTF8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.resultData[0].keys())
            writer.writeheader()
            for d in self.resultData:
                writer.writerow(d) 
        return process(file)

    def main(self, process):

        print("init main fonction (soup)")
        response = requests.get(self.exploitUrl)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            return process(soup)
        return []

# exec de la classe

instance = Audiofanzine(baseUrl, uri, resultData)
test = "getEndpoints"
endpoints = instance.main(test)
instance.fileWriter('linksHeader.csv', fileReader)


    #get info from all link

    # lignes = []
    # for link in fileReader('links.csv'):
    #     lignes.extend(swoup(link['lien'], getInfoByPage))

    # fields = ["name", "adress","realAdress","departement","country", "tel", "email", "title"]
    # fileWriter('infos.csv', fields, lignes )