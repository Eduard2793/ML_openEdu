import numpy as np
'''
XY = np.array([[5,12],
[17,45],
[9,18],
[13,25],
[12,23],
[7,18],
[18,43],
[20,36],
[22,66],
[24,78]])
'''
XY = np.array([[4,10],
[22,41],
[20,36],
[7,17],
[13,31],
[12,35],
[17,47],
[3,10],
[1,5],
[21,41]])

X_ = XY.mean(0)[0]
Y_ = XY.mean(0)[1]
print(X_)
print(Y_)

s1 = s2 = 0
n = XY.size//XY[0].size
for i in range(n):
    s1 += (XY[i,0] - X_)*(XY[i,1] - Y_)
    s2 += (XY[i,0] - X_)**2

teta1 = s1/s2
teta0 = Y_ - teta1*X_
print(teta1)
print(teta0)

s1 = 0
s2 = 0
n = XY.size//XY[0].size
for i in range(n):
    s1 += (XY[i,1] - (teta1*XY[i,0] + teta0))**2
    s2 += (XY[i,1] - Y_)**2

R2 = 1 - (s1/s2)

print(R2)
print(s1)
