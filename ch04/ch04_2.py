# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:05:32 2022

@author: user
"""

import usecsv

data = usecsv.opencsv('example2.csv')

print(data)

usecsv.writecsv('test3.csv', data)