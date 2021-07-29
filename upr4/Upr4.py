import numpy as np
from numpy import linalg as LA
import pandas as pd
import shutil as sh
import matplotlib.pylab as plt
sh.sys.__stdout__ = sh.sys.stdout

data = pd.read_csv("candy-data.csv",
                    delimiter=',',
                    decimal='.')

XYdata = data.drop(['competitorname','Y'], axis=1)

Chiclets = XYdata.loc[12,:] # берем тестовые строки
Fruit_Chews = XYdata.loc[15,:] # берем тестовые строки
Chiclets = Chiclets.drop('winpercent').to_numpy()
Fruit_Chews = Fruit_Chews.drop('winpercent').to_numpy()
Chiclets = np.r_[1,Chiclets]
Fruit_Chews = np.r_[1,Fruit_Chews]

XYdata = XYdata.drop([12,15],axis = 0) # удаляем тестовые строки

Y = XYdata.winpercent.to_numpy() # берем столбец откликов
X = XYdata.drop('winpercent', axis=1).to_numpy()# берем X то есть
# удаляем столбец с откликами
X = np.c_[np.ones(X.size//X[0].size),X] # добавляем столбец с единицами

A = np.matmul(X.T,X)
A1 = LA.inv(A)
B = np.matmul(X.T,Y)
beta = np.matmul(A1,B)

c = np.array([1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0.607, 0.254])

print(np.matmul(Chiclets,beta))
print(np.matmul(Fruit_Chews,beta))
print(np.matmul(c,beta))











