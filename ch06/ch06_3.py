# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:33:16 2022

@author: user
"""

# 웹 크롤링 기본 환경 준비
import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = 'https://news.daum.net/'
soup = bs(ur.urlopen(news).read(), 'html.parser')

print('===머리기사 제목 추출===')
# <div> 내용 추출
soup.find_all('div', {'class' : 'item_issue'})
# 기사 제목 추출
for i in soup.find_all('div', {'class':'item_issue'}):
    i.text
    
print('===하이퍼링크 주소 추출===')
soup.find_all('a')
soup.find_all('a')[:5]
# href 속성값 추출
for i in soup.find_all('a')[:5]:
    i.get('href')
    
print('===원하는 영역에서 하이퍼링크 모두 추출===')
# find_all로 <a> 태그 추출
for i in soup.find_all('div', {'class':'item_issue'}):
    i.find_all('a')
# get으로 href 속성값 구하기
for i in soup.find_all('div', {'class':'item_issue'}):
    print(i.find_all('a')[0].get('href'))
    
print('===기사 제목과 내용 한꺼번에 추출===')
# 웹 문서를 뷰티풀수프 객체에 저장
article1 = 'https://go.seoul.co.kr/news/newsView.php?id=20200427004004&wlog_tag3=daum'
soup2 = bs(ur.urlopen(article1).read(), 'html.parser')
# 기사 내용 가져오기
for i in soup2.find_all('p'):
    print(i.text)
# 기사 제목 가져오기
headline = soup.find_all('div', {'class':'item_issue'})
print(headline[0].text)

print('===하이퍼링크된 모든 기사의 제목과 본문 추출===')
for i in headline:
    #print(i.text, '\n')
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
    for j in soup3.find_all('p'):
        print(j.text)

print('===URL 주소 저장하기===')
f = open('links.txt', 'w')
for i in soup.find_all('div', {'class':'item_issue'}):
    f.write(i.find_all('a')[0].get('href')+'\n')
f.close()

print('===기사 본문을 파일로 저장하기===')
article1 = 'https://news.v.daum.net/v/20200430135751773'
soup = bs(ur.urlopen(article1).read(), 'html.parser')
f = open('article_1.txt','w')
for i in soup.find_all('p'):
    f.write(i.text)
f.close()

print('===기사 제목, 본문, 하이퍼링크를 파일로 저장하기===')
url = 'https://news.daum.net/'
soup = bs(ur.urlopen(url).read(),'html.parser')
f = open('article_total.txt', 'w', encoding='utf8')
for i in soup.find_all('div', {'class':'item_issue'}):
    try:
        f.write(i.text + '\n')
        f.write(i.find_all('a')[0].get('href') + '\n')
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass
f.close()