import requests
from bs4 import BeautifulSoup
'''
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print(response.text)
print(type(response.text))
'''
response = requests.get('https://en.wikipedia.org')
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
print(soup.title)
print(soup.p)
print(soup.find_all('p')[1].a)
print(soup.find(id="mp-sister"))