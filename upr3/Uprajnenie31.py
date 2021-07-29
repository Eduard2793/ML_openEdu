
import numpy as np
import pandas as pd
import shutil as sh
import matplotlib.pylab as plt
sh.sys.__stdout__ = sh.sys.stdout

data = pd.read_csv("dataXer.csv",
                    delimiter=',',
                    decimal='.')
data = data.to_numpy()

avg = data.mean(axis=0)
newData = []
for i in range(data[0].size):
    col = data[:,i]
    newArr = []
    for j in range(len(col)):
        newArr.append(col[j] - avg[i])
    newData.append(newArr)

F = np.array(newData).T

n = F.size

teta = np.matmul((F.T),F)
eig = np.linalg.eig(teta)

eigValues = eig[0]
Fi = eig[1]
Z = np.matmul(F,Fi)
print((eigValues[0] + eigValues[1] + eigValues[2])/sum(eigValues)) # доля объясненой дисперсии при использовании 3-х главных компонент
print(Z) # в строках объекты, по столбцам их координаты относительно главных компонент

fig, ax = plt.subplots()

ax.scatter(Z[:,0], Z[:,1],
           c = 'deeppink')    #  цвет точек

#ax.set_facecolor('black')     #  цвет области Axes
#ax.set_title('Один цвет')     #  заголовок для Axes

#fig.set_figwidth(8)     #  ширина и
#fig.set_figheight(8)    #  высота "Figure"

plt.show()

'''
matr = np.array([[4,5,6],[1,0,2],[3,2,9]])
print(np.linalg.eig(matr))

ve = np.array([[-0.65221283], [-0.17538001],  [-0.73746883]])
print(ve)
print(ve*12.1288082)
print(np.matmul(matr,ve))
'''

























