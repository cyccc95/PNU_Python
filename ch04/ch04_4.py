# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:14:10 2022

@author: user
"""

import usecsv, re

print('=====외국인 비율이 3% 넘는 구 정보만 CSV파일로 저장하기=====')
pop = usecsv.opencsv("popSeoul.csv")
pop = usecsv.switch(pop)

print(pop[:4])

print('=====각 구의 외국인 비율 출력=====')
for i in pop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        print(i[0], foreign)
    except:
        pass
    
print('=====외국인 비율이 3% 초과할 때만 출력=====')
new = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in pop:
    foreign = 0
    try:
        foreign = foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass
for item in new:
    print(item)
usecsv.writecsv('pop.csv', new)

print('=====부동산 실거래가 살펴보기=====')
apt = usecsv.switch(usecsv.opencsv('apt_201910.csv'))
new_apt = []
for i in apt:
    try:
        if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
            print(i[0], i[4], i[-4])
            new_apt.append([i[0], i[4], i[-4]])
    except:
        pass
usecsv.writecsv('over120_lower30000.csv', new_apt)

print('=====번역한 예문을 표로 저장하기=====')
English = 'She is a vegetarian. She does not eat meat. She thinks that animals should not be killed. It is hard for her to hang out with people. Many people like to eat meat. She told his parents not to have meat. They laughed at her. She realized they couldn\'t give up meat.'
Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽여서는 안 된다고 생각합니다. 그녀는 사람들과 어울리는 것이 어렵다. 많은 사람들이 고기를 먹고 싶어합니다. 그녀는 그의 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃었습니다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'
Korean_list = re.split('\.', Korean)
English_list = re.split('\.', English)
print(Korean_list)

total = []
for i in range(len(English_list)):
    total.append([English_list[i], Korean_list[i]])
usecsv.writecsv('Korean_English.csv', total)

















