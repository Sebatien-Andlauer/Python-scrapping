from Toolkit import Toolkit
# from AudiofanzineEntry import AudiofanzineEntry

class Audiofanzine:
    def __init__(self, baseUrl, uri, nbPage, fields):
        self.baseUrl = baseUrl
        self.uri = uri
        self.setPageMax(nbPage)
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileNameFields = fields

    def setFinalFileNameFields(self):

        return self

    def setPageMax(self, pageMax):

        self.nbPage = pageMax + 1
        return self
    
    def getLinks(self):

        for i in range(self.nbPage):
            self.urls.append(self.baseUrl + self.uri)
        return self.urls

    def setEndpoints(self,soup):

        print('init fonction getEndpoints')
        links = []
        divP = soup.find('div', {"class":"cmps-tabs"})
        divFC = divP.findAll('div', {"class":"cmps-tabs-col"})
        for a in divFC:
            a = a.find('a')  
            try:
                links.append(a['href'])
            except:
                pass
        self.endpoints.extend(Toolkit.addBaseUrl(self.baseUrl, links))
        return self.endpoints
        
    def getResult(self):

        return self.result

    def getDictResult(self):

        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result

    def getEndpoints(self):

       return self.endpoints
    
    # def getInfoByPage(self, soup):
    
    #     fiches = []
    #     contacts = soup.find("div",{"class": "coordonnees"})
    #     if contacts is not None:
    #         tabs = contacts.findAll('li', {"class":"accordeon-item"})
    #         if tabs is not None:
    #             for contact in tabs:
    #                 name = Toolkit.tryToCleanOrReturnBlank(contact.find("div", {"class": "accordeon-header"}))
    #                 coord = contact.find("div", {"class": "accordeon-body"})
    #                 adress = coord.find("p")
    #                 tel = Toolkit.tryToCleanOrReturnBlank(coord.find("a", {"class": "tel"}))
    #                 email = Toolkit.tryToCleanOrReturnBlank(coord.find("a", {"class": "email"}))
    #                 title = Toolkit.tryToCleanOrReturnBlank(soup.find("title"))
    #                 try:
    #                     adress = adress.getText()
    #                     cleanArrAdress = []
    #                     for ele in str(adress).split("\n"):
    #                         # cleanAdress.push(ele)
    #                         if ele.strip() != "":
    #                             cleanArrAdress.append(ele.strip())
                        
    #                     realAdress = cleanArrAdress[0]
    #                     realCC = cleanArrAdress[1]
    #                     realCountry = cleanArrAdress[2]
    #                 except:
    #                     adress= ""
    #                     realAdress= ""
    #                     realCC= ""
    #                     realCountry= ""
    #                     cleanArrAdress = []
            
    #                 fiche = StudyramaEntry(title, name, cleanArrAdress, realAdress, realCC, realCountry, tel, email)
    #                 fiches.append(fiche)
    #     self.result.extend(fiches)
    #     return fiches

    def getFinalFieldNames(self):

        return self.finalFileNameFields

    def getResult(self):

        return self.result

    def getDictResult(self):

        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result