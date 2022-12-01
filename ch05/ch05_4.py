# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:19:47 2022

@author: user
"""

import pandas as pd
import re

data = {'name' : ['Mark', 'Jane', 'Chris', 'Ryan'],
        'age' : [33, 32, 44, 42],
        'score' : [91.3, 83.4, 77.5, 87.7]}
df = pd.DataFrame(data)
print(df)
#print(df.sum())
#print(df.mean())
#print(df.age)
#print(df['age'])

print('=====CSV 파일 불러와 데이터프레임으로 만들기=====')
df = pd.read_csv('apt.csv', encoding='cp949')
print(len(df))

print('=====처음이나 마지막 자료 일부만 출력하기=====')
print(df.head())
print(df.tail())

print('=====열 전체 자료 출력하기=====')
print(df.지역)

print('=====조건별로 출력하기=====')
print(df.면적 > 130)
print(df[df.면적 > 130])
print(df.가격[df.면적 > 130])
print(df.가격[(df.면적 > 130) & (df.가격 < 15000)])

print('=====원하는 자료만 살펴보기=====')
# df.loc[원하는 행의 조건, 원하는 열의 조건]
print(df.loc[:10, ['아파트', '가격']])
print(df.loc[:, ['아파트','가격']] [df.가격 > 40000])

print('=====새로운 값 추가하기=====')
#df['새로운 열 이름'] = 넣고 싶은 값
df['단가'] = df.가격 / df.면적
print(df.loc[:10, ('가격', '면적', '단가')])

print('=====데이터 정렬하기=====')
print(df.sort_values(by = '가격').loc[:, ('가격', '지역')])
print(df.sort_values(by = '가격', ascending = False).loc[:, ('가격', '지역')])
print(df[df.가격 > 40000].sort_values(by = '면적').loc[:, ('가격','면적','지역')])

print('=====문자열 다루기=====')
# df.검색할 열.str.find('찾는 문자열')
# 찾는 문자열이 없다면 -1 반환
print(df.지역.str.find('강릉'))
print(df[df.지역.str.find('강릉') > -1])
dfF = df[df.지역.str.find('강릉') > -1]
print(dfF.mean())














