import numpy as np
from numpy import linalg as LA
import pandas as pd
import shutil as sh
import matplotlib.pylab as plt
sh.sys.__stdout__ = sh.sys.stdout

data = pd.read_csv("candy-dataChel.csv",
                    delimiter=',',
                    decimal='.')

XYdata = data.drop(['competitorname','Y'], axis=1)

Runts = XYdata.loc[58,:] # берем тестовые строки 12 14
Starburst = XYdata.loc[68,:] # берем тестовые строки 15 17
Runts = Runts.drop('winpercent').to_numpy()
Starburst = Starburst.drop('winpercent').to_numpy()
Runts = np.r_[1,Runts]
Starburst = np.r_[1,Starburst]

XYdata = XYdata.drop([58,68],axis = 0) # удаляем тестовые строки

Y = XYdata.winpercent.to_numpy() # берем столбец откликов
X = XYdata.drop('winpercent', axis=1).to_numpy()# берем X то есть
# удаляем столбец с откликами
X = np.c_[np.ones(X.size//X[0].size),X] # добавляем столбец с единицами

A = np.matmul(X.T,X)
A1 = LA.inv(A)
B = np.matmul(X.T,Y)
beta = np.matmul(A1,B)

c = np.array([1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0.91, 0.751])

print(np.matmul(Runts,beta))
print(np.matmul(Starburst,beta))
print(np.matmul(c,beta))
