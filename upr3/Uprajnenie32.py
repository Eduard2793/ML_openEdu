import numpy as np
import pandas as pd
import shutil as sh
import matplotlib.pylab as plt
sh.sys.__stdout__ = sh.sys.stdout

Z = pd.read_csv("X_loadings_Xer.csv",
                    delimiter=',',
                    decimal='.')
Z = Z.to_numpy()

Fi = pd.read_csv("X_reduced_Xer.csv",
                    delimiter=',',
                    decimal='.')
Fi = Fi.to_numpy()

def foo(M):
    A = []
    m = M.size//M[0].size
    for i in range(m):
        row = M[i][0].split(";")
        a = []
        n = len(row)
        for j in range(n):
            a.append(float(row[j]))
        A.append(a)
    return np.array(A)

Z = foo(Z)
Fi = foo(Fi)

F = np.matmul(Z,Fi.T) # восстановили F

plt.imshow(F) # построили цветовую карту
plt.show()
