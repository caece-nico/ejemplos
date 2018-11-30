# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:30:12 2018

@author: leali
"""
import matplotlib.pyplot as plt
import pandas as pd

directorio = 'C:\\Users\\leali\\Desktop\\ejemplos\\hubble.txt'

f = open(directorio, 'r')

data = f.read()

f.close()


words = data.split(' ')

print('Calculamos la cantidad de palabras')
total = len(words)
print('La cantidad de palabras es:',  str(total))


total = {}

for i in words:
    if i in total:
        total[i]+=1
    else:
        total[i]=1
        
print(total)

for i, idx in enumerate(total):
    print(i,idx,i,total[idx])
     

    