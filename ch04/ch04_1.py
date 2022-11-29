# -*- coding: utf-8 -*-

import csv, os

def opencsv(filename):
    with open(filename, "r") as f:
        new = csv.reader(f)
        a_list = []
    
        for line in new:
            a_list.append(line)
        
    return a_list

li = opencsv('a.csv')
print(li) 
print()
li2 = opencsv('example2.csv')
print(li2)
print()
#############################################
data = [['이름', '국어', '영어', '수학'], 
        ['a', '90', '80', '100'], 
        ['b', '80', '90', '90'], 
        ['c', '100', '80', '60']]

def writecsv(filename, the_list):
    f = open(filename, 'w', newline='')
    csvobject = csv.writer(f, delimiter=',')
    csvobject.writerows(the_list)
    f.close()
    
writecsv('test2.csv', data)

    
