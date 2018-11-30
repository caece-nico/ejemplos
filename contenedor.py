# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:50:33 2018

@author: leali
"""

"""
texto = 'Pablito clavo un clavito que clavito clavo pablito '

print(texto)

palabras =  texto.split(' ')

print(palabras)

cuenta = dict()

for pal in palabras:
    if pal in cuenta:
        cuenta[pal]+=1
    else:
        cuenta[pal]=1


print(cuenta)

for idx, palabra in enumerate(cuenta):
    print('La palabra: ' +  palabra + ' aparece: ' + str(cuenta[palabra]) + ' veces')
"""

print(range(1,10))

from pyspark import SparkConf
from pyspark import SparkContext
conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('anaconda-pyspark')
sc = SparkContext(conf=conf)


