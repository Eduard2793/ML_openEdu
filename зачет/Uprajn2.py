import numpy as np
import pandas as pd
import shutil as sh
sh.sys.__stdout__ = sh.sys.stdout

stars = pd.read_csv("report.csv",
                    delimiter=',',
                    decimal='.',
                    usecols=['MIP','STDIP','EKIP','SIP','MC','STDC','EKC','SC','TARGET'])
starsMatr = stars.to_numpy()

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

print(np.average(starsMatr[:,0])) # Определите выборочное среднее для столбца MIP до нормировки
norm = normalize(starsMatr)
print(np.average(norm[:,0])) # Определите выборочное среднее для столбца MIP после нормировки

train_data = pd.DataFrame({'MIP': norm[:,0],'STDIP':norm[:,1],'EKIP':norm[:,2] ,'SIP':norm[:,3] ,'MC' :norm[:,4],'STDC':norm[:,5] ,'EKC':norm[:,6] ,'SC':norm[:,7] ,'TARGET':norm[:,8]})
test = [[0.157,0.311,0.676,0.586,0.307,0.848,0.673,0.64]]

# регрессия
X = pd.DataFrame(train_data.drop(['TARGET'], axis=1))
Y = pd.DataFrame(train_data['TARGET'])

from sklearn.linear_model import LogisticRegression

reg = LogisticRegression(random_state=2019).fit(X, Y.values.ravel())
# вероятности указаны для классов 0 и 1 соответственно
pred = reg.predict_proba(test)
print(pred)
print()

# k-NN
test = np.array([0.157,0.311,0.676,0.586,0.307,0.848,0.673,0.64])
XkNN = X.to_numpy()
#YkNN = Y['TARGET'].to_numpy()
#print(YkNN)

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

mE = min(getDE(XkNN,test.reshape(8,1)).values()) # евклид
print(mE)

#mM = min(getDM(XkNN,test.reshape(8,1)).values()) # манхетен
#print(mM)

# Часть 2





































        
