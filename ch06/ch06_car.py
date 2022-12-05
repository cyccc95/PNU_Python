# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:17:13 2022

@author: user
"""

import urllib.request as ur
from bs4 import BeautifulSoup as bs
import usecsv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

url = 'http://bpms.kemco.or.kr/transport_2012/car/car_choice.aspx?f=system'

soup = bs(ur.urlopen(url).read(), 'html.parser')
#print(soup)
print('===================================')
#tr_list = soup.find_all('tr')
tr_list = soup.select('#search_top > table > tbody > tr')

car_info = [['업체명', '모델명', '표시연비', '배기량', 'co2배출량', '등급', '연간유류비']]

for tr in tr_list:
    td = tr.find_all('td')
    img_list = td[5].find_all('img')
    car_info.append([td[0].text, td[1].text, td[2].text, td[3].text.replace(',',''), td[4].text, img_list[0].get('src')[-5], td[6].text.replace(',','')])

usecsv.writecsv('car_info.csv', car_info)

df = pd.read_csv('car_info.csv', encoding='euc-kr')
print(df.head())

#df.info()

print('====================================')
#print(df[df['co2배출량']>=115])

print('====================================')
df['연간유류비'].astype(float).head(5).plot(kind='bar')
plt.xticks(range(5), labels=df['모델명'].head(5), rotation=90)
plt.show()

plt.figure(figsize=(5,3))
sns.countplot(y='업체명', hue='등급', data=df)
plt.title('업체별 자동차 등급 현황')
plt.show() 




