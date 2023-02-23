class AudifanzineEntry:
    def __init__(self,title,name,adress,realAdress,departement,country,tel,email):
        
        self.setTitle(title)
        self.name = name
        self.setAdress(adress)
        self.realAdress = realAdress
        self.departement = departement
        self.country = country
        self.tel = tel
   

    def setTitle(self, title):
        self.title = title.replace('- Studyrama', "")
    def setAdress(self, arrAdress):
        self.adress = " ".join(arrAdress)
    def getDictEntry(self):
        return {
            "title":self.title,
            "name":self.name,
            "adress":self.adress,
            "realAdress":self.realAdress,
            "departement":self.departement,
            "country":self.country,
            "tel":self.tel,
            "email":self.email
        }
