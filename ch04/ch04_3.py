# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:20:28 2022

@author: user
"""

import re
import usecsv

total = usecsv.opencsv('popSeoul.csv')

print(usecsv.switch(total))