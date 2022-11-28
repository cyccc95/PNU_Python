# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:49:41 2022

@author: user
"""

import re

# 특정 등장인물의 대사만 모으기
with open('monica.txt', 'w') as m:
    with open('friends101.txt', 'r') as f:
        s101 = f.read()
        Line = re.findall(r'Monica:.+', s101)
        for item in Line:
            m.write(item + "\n")

# 등장인물 리스트 만들기
with open('friends101.txt', 'r') as f:
    s101 = f.read()
    list = set(re.findall(r'[A-Z][a-z]+:', s101))
    character = []
    for char in list:
        character += [char[:-1]]
    print(character)
    
print('-----------------------')
# 지문만 출력하기
with open('friends101.txt', 'r') as f:
    s101 = f.read()
    print(re.findall(r'\([A-Za-z].+?[a-z|\.]\)', s101))
    
print('-----------------------')
# 특정 단어의 예문만 모아 파일로 저장하기
with open('friends101.txt', 'r') as f:
    sentences = f.readlines()
    lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
    would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)
             and re.search('would', i)]
    print(would)
with open('would.txt', 'w') as w:
    w.writelines(would)
    