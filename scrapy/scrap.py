from Scraper import Scraper
from Audiofanzine import Audiofanzine

# L'url du site que je souhaite Scraper
baseUrl = 'https://fr.audiofanzine.com'
uri = "/petites-annonces/?type=2"

audiofanzineInstanceLink = Audiofanzine(baseUrl, uri, 1, 'Links')
audifanzineInstanceData = Audiofanzine(baseUrl, uri, 1, ["title", "price", "argus", "description", "location", "rate", "url"])
scraper1 = Scraper(audifanzineInstanceData, "./data/linksListaudiofanzine.csv", "./data/dataAudiofanzine.csv")
# scraper = Scraper(audiofanzineInstanceLink, "./data/links.csv", "./data/linksListaudiofanzine.csv")

# scraper.exec()
scraper1.exec()

print("Done")