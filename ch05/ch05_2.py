# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:24:52 2022

@author: user
"""

import numpy as np
import os, usecsv

# 배열 슬라이싱 하기
d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
print(d)
print(d[1][2])
print(d[1, 2])
print(d[1:, 3:])

print('=====배열의 크기 알아내기=====')
d = np.array([2,3,4,5,6])
print(d.shape)
e = np.array([[1,2,3,4], [3,4,5,6]])
print(e.shape)

print('=====배열의 원소 유형 확인하기=====')
print(d.dtype)

print('=====배열 유형 바꾸기=====')
data = np.arange(1, 5)
print(data.dtype)
data.astype('float64')
print(data.dtype)

print('=====설문지 데이터 전처리하기=====')
quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
print(quest)
print(quest > 5)
print(quest[quest > 5])
quest[quest > 5] = 5
print(quest)
usecsv.writecsv('resultcsv.csv', list(quest)) 

