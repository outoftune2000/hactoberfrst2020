# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 23:29:23 2018

@author: admin
"""

c = input()
count = 0
for i in range(0,len(c)):
    if c[i] == "a" or c[i] == "e" or c[i] == "i" or c[i] == "o" or c[i] == "u":
        count+=1
print(count)
