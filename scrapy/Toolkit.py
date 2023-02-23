import csv

class Toolkit:
    def tryToCleanOrReturnBlank(str):
        try:
            result = str.getText().strip()
        except:
            result = ""
        return result

    def fileReader(file):
    
        print('init fonction fileReader')
        result = []
        with open(file, 'r', encoding="UTF8", newline="") as f:
            reader = csv.DictReader(f)
            for line in reader:
                result.append(line) 
        return result

    def fileWriter(file, fieldnames, data):

        print('init fonction file writer')
        with open(file, 'w', encoding="UTF8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for d in data:
                writer.writerow(d) 

    def addBaseUrl(baseUrl, urls):
        res = []
        for url in urls:
            res.append(baseUrl + url)
        return res