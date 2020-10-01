# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 00:19:44 2018

@author: admin
"""
f2 = open("new.txt","w")
f2.write("hello")
f2.close()
try:
    x = input("Enter the text name")
    f = open(x,"r")
except:
    print("no such text")