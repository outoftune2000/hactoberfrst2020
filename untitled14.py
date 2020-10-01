# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 00:53:29 2018

@author: admin
"""
k = []
c = [12,15,7,8,15,17,99,99,8,88,77,77,77]
for i in range(0,len(c)):
    for j in range(0,i):
        if c[i] == c[j]:
            k.append(c[i])
print(k)
            a.
