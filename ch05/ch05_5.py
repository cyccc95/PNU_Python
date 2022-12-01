# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:43:48 2022

@author: user
"""

import re
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

print('=====기초통계량 살펴보기=====')
df2 = pd.read_csv('survey.csv')
#print(df2.head())
#print(df2.mean())
#print(df2.income.median())
print(df2.describe())
print(df2.income.describe())

print('=====기초통계량 분석하기=====')
print(df2.sex.value_counts())
print(df2.groupby(df2.sex).mean())

print('=====싸이파이 패키지로 t검정 하기=====')
male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']
ttest_result = stats.ttest_ind(male, female) 
print(ttest_result)
if ttest_result[1] > .05:
    print('p-value는 %f로 95%% 수준에서 유의미하지 않음' % ttest_result[1])
else:
    print('p-value는 %f로 95%% 수준에서 유의미함' % ttest_result[1])
    
print('=====두 변수의 상관관계 분석하기=====')
corr = df2.corr()
print(corr)
print(df2.income.corr(df2.stress))
corr.to_csv('corr.csv')

print('=====statsmodels 패키지로 회귀 분석하기=====')
model = smf.ols(formula = 'jobSatisfaction~English', data = df2)
result = model.fit()
print(result.summary())

model2 = smf.ols(formula = 'jobSatisfaction~English + stress + income', data = df2)
result = model2.fit()
print(result.summary())