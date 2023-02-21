import requests
from bs4 import BeautifulSoup

baseUrl = 'https://fr.audiofanzine.com'
uri_instruments = '/instrument-materiel-audio'
uri_news = '/news'
uri_tests = '/editorial/tests'
uri_dossiers = '/editorial/dossiers'
uri_af = '/tv'
uri_avis = '/avis'
uri_forums = '/forums'
uri_ads = '/annonces'
uri_other = ''
uri_deals ='/deals/'

response = requests.get(baseUrl + uri_instruments)
if response.ok:
    swoup = BeautifulSoup(response.text, 'html.parser')
    ul = swoup.find('ul')
    lis = ul.findAll('li')
    for li in lis:
        a = li.find('a')  
        print(baseUrl + uri_instruments + a['href'])
print(response.ok)