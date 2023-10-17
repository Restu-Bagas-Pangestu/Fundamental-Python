'''
get html file from BeautifulSoup
'''

from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content= result.text
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

box = soup.find('article', class_= 'main-article') #kasih underscore untuk class

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)

for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')
    title= box.find('h1').get_text()
    # print(title)
    transcript=box.find('div', class_='full-script').get_text(strip=True, separator=' ') #separator untuk spasinya pakai apa, strip=untuk spasi
    # print(transcript)

    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)
    #pakai 'utf-8' biar gak eror