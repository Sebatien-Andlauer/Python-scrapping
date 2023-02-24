class AudiofanzineEntry:
    def __init__(self, title, price, argus, description, location, rate, url):
        self.title = title
        self.price = price
        self.argus = argus
        self.description = description
        self.location = location
        self.rate = rate
        self.url = url


    def setAdress(self, arrAdress):
        self.adress = " ".join(arrAdress)
    def getDictEntry(self):
        fiche = {
                "title":self.title,
                "price":self.price,
                "argus":self.argus,
                "description":self.description,
                "location" :self.location,
                "rate" :self.rate,
                "url" :self.url
                }
        print(fiche)
        return fiche