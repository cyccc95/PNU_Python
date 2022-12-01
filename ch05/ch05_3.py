# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:50:39 2022

@author: user
"""

import numpy as np
import numpy_financial as npf

print('=====자본의 현재 가치 구하기=====')
discount = .05
cashflow = 100

def presentvalue(n):
    return (cashflow / ((1 + discount) ** n))

print(presentvalue(1))
print(presentvalue(2))

for i in range(20):
    print(presentvalue(i))
    
print('=====놀이공원 사업의 사업성 분석하기=====')
loss = [-750, -250]
profit = [100] * 18
print(profit)

cf = loss + profit
print(cf)
print(len(cf))

cashflow = np.array(cf)
n = npf.npv(0.045, np)
i = npf.irr(np)
print(n)
print(i)


