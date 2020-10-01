# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:59:20 2018

@author: admin
"""
x=int(input("enter number"))
prime = 1
for i in range(x,1,-1):
    prime = prime*i
print(prime)