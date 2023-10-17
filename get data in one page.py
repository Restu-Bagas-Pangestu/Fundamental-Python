'''
get html file from BeautifulSoup
'''

from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content= result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

box = soup.find('article', class_ = 'main-article') #kasih underscore

title= soup.find('h1').get_text()
print(title)

transcript=soup.find('div',class_='full-script').get_text(strip=True, separator=' ') #separator untuk spasinya pakai apa, strip=untuk spasi
print(transcript)

with open (f'{titanic}.txt', 'w') as file:
    file.write(transcript)