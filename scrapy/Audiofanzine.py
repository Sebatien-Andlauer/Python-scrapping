from Toolkit import Toolkit
from AudiofanzineEntry import AudiofanzineEntry


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
        divP = soup.find("div", {"id": "full-content"})
        divSp = divP.find("div", {"class": "page-content"})
        divFC = divSp.find('div', {"class":"wrapper-playlist"})
        divCU = divFC.find('div', {"class":"classifieds"})
        ulParent = divFC.find('ul')
        liArticles = ulParent.findAll('li')
        for a in liArticles:
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
    
    def getInfoByPage(self, soup):
        # id,title,price,argus,description,location,rate, url
        print('init getInfoByPage')

        div = soup.find("div", {"id":"full-content"})
        
        fiches = []
        if div is not None:
            pageContent = div.find('div', {"class":"page-content"})
            urlMeta = soup.find('meta',{"property":"og:url"})
            data = pageContent.findAll('div')
            divAside = div.find("div", {"class":"cmps-infos"})
            asideArg = divAside.find("aside")
            divInAside = asideArg.find("div", {"class":"priceBlock-content"})
            ulAside = divInAside.find('ul')
            liInAside = ulAside.find('li')
            aArgus = liInAside.find('a', {"class":"priceBlock-argus"})
            rating = div.find('div', {"class":"rate-star"})
            if data is not None:
                for info in data:
                    title = Toolkit.tryToCleanOrReturnBlank(info.find('h1'))
                    price = Toolkit.tryToCleanOrReturnBlank(info.find('div', {"class":"classifieds-price"}))
                    argus = Toolkit.tryToCleanOrReturnBlank(aArgus)
                    description = Toolkit.tryToCleanOrReturnBlank(info.find('div', {"class":"classifieds-content-description"}))
                    location = Toolkit.tryToCleanOrReturnBlank(info.find('div', {"class":"classifieds-localization"}))
                    rate = Toolkit.tryToCleanOrReturnBlank(rating)
                    url = Toolkit.tryToCleanOrReturnBlank(urlMeta)
                    # fiche = {
                    #     "title":title,
                    #     "price":price,
                    #     "argus":argus,
                    #     "description":description,
                    #     "location" :location,
                    #     "rate" :rate,
                    #     "url" :url
                    #     }
                    fiche = AudiofanzineEntry(title, price, argus, description, location, rate, url)
                    fiches.append(fiche)
        self.result.extend(fiches)
        return fiches

    def getFinalFieldNames(self):

        return self.finalFileNameFields

    def getResult(self):

        return self.result

    def getDictResult(self):

        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result