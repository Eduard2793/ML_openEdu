#from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import shutil as sh
sh.sys.__stdout__ = sh.sys.stdout

stars = pd.read_csv("reportXer.csv",
                    delimiter=',',
                    #nrows=5,
                    decimal='.',
                    usecols=['MIP','STDIP','EKIP','SIP','MC','STDC','EKC','SC','TARGET'])
starsMatr = stars.to_numpy()
#print(np.average(starsMatr[:,0]))
#scaler = MinMaxScaler()
#normalize = scaler.transform(starsMatr)
starsMatr8 = np.delete(starsMatr,8,1) # удаляем восьмой столбец (индексация с 0)

def MinMax(arr):
    newArr = []
    Min = min(arr)
    Max = max(arr)
    for x in arr:
        newArr.append((x-Min)/(Max-Min))
    return newArr
    

def normalize(matr):
    newMatr = []
    n = matr[0].size
    for i in range(n):
        col = matr[:,i] # берём столбец
        normedCol = MinMax(col)
        newMatr.append(normedCol)
    npMatr = np.array(newMatr)
    npMatr = npMatr.T
    return npMatr

norm = normalize(starsMatr8)

def metrik(a,b):
    s = 0
    for i in range(len(a)):
        s += (a[i]-b[i])**2
    return s**(1/2)

S = [0.142,0.324,0.6,0.579,0.124,0.302,0.309,0.231]

D = []
for i in range(norm.size//norm[0].size):
    D.append(metrik(S,norm[i]))

print(min(D))





















        
