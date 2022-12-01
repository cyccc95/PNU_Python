# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 20:09:40 2022

@author: user
"""

import matplotlib.pyplot as plt

print('=====그래프 만들고 출력하기=====')
x = [1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(x)
plt.show()

print('=====그래프 모양과 색 지정하기=====')
plt.plot(x, color = 'r')
plt.show()

plt.plot(x, 'or')
plt.show()

print('=====축 이름 지정하기=====')
y = [i for i in range(1, 9)]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('matplotlib sample')
plt.show()