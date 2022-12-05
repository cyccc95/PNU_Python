# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:56:24 2022

@author: user
"""

import re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'http://quotes.toscrape.com/'
#html = ur.urlopen(url)
#soup = bs(html.read(), 'html.parser')
#print(type(html))
#print(type(soup))
#print(soup)

soup = bs(ur.urlopen(url).read(), 'html.parser')
quote = soup.find_all('span')
#print(quote[0].text)

for i in quote:
    i.text
    
soup.find_all('div', {'class' : 'quote'})
soup.find_all('div', {'class' : 'quote'})[0].text
#print(soup.find_all('div', {'class' : 'quote'})[0].text)

for i in soup.find_all('div', {'class' : 'quote'}):
    print(i.text)