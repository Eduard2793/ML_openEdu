# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

'''
X = np.array([[31,19],
 [45,23],
 [15,46],
 [92,82],
 [78,29],
 [58,34],
 [25,19],
 [29,93],
 [84,82],
 [82,27]]) # мой
Y = np.array([0,1,1,1,1,0,1,1,1,0]).reshape((10,1))
'''
X = np.array([[51,43],
[22,87],
[10,55],
[90,17],
[59,65],
[13,44],
[73,50],
[75,24],
[31,19],
[55,93]])
Y = np.array([1,1,0,1,0,0,1,1,0,0]).reshape((10,1))

def dE(a,b):
    s = 0
    n = a.size
    for i in range(n):
        s += (a[i]-b[i])**2
    return s**(1/2)

def dM(a,b):
    s = 0
    n = a.size
    for i in range(n):
        s += abs(a[i] - b[i])
    return s

def getDE(X,Z):
    D = {}
    for i in range(X.size//X[0].size):
        D[i] = dE(X[i],Z)
    return D

def getDM(X,Z):
   D = {}
   for i in range(X.size//X[0].size):
       D[i] = dM(X[i],Z)
   return D

print(getDE(X,[34,28]))
print()
print(getDM(X,[34,28]))
        
        
        
        
        
        
        
        
        
        
        









    
