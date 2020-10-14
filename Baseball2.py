import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
"""
#将baseball.dat文件转换为baseball.csv文件
path0 = 'E:/Downloads/baseball.dat'
data = pd.read_table(path0, header=0, sep=' ')
data = data.to_csv('E:/Downloads/baseball.csv', index=False, header=True)
"""
#读入csv数据
Data = pd.read_csv('E:/Downloads/baseball0.csv')

#将X,Y处理为矩阵形式，salary的对数以e为底
X = Data.drop(['salary'], axis=1).values
Y = Data['salary'].values.reshape(-1, 1)
for i in range(Y.shape[0]):
	Y[i][0] = math.log(Y[i][0])

#解出β矩阵
XT = X.transpose()
XTX = np.dot(XT, X)
XTY = np.dot(XT, Y)
Beta = np.linalg.solve(XTX, XTY)
print(np.dot(X, Beta) - Y)

#计算残差平方和RSS
RSS = 0.0
ls3 = []
for i in range(X.shape[0]):
	s = 0.0
	for j in range(X.shape[1]):
		s += X[i][j] * Beta[j][0]
	ls3.append(s - Y[i][0])
	RSS += (s - Y[i][0]) ** 2


TSS, avg = 0.0, 0.0
avg = Y.sum(axis=0) / Y.shape[0]
for i in range(Y.shape[0]):
	TSS += (Y[i][0] - avg) ** 2

#计算决定系数R^2和AIC
R2 = 1 - RSS / TSS
AIC = X.shape[0] * math.log(RSS / X.shape[0]) + 2 * X.shape[1]


print('回归系数为：{}'.format(Beta))
print('残差平方和RSS为：{}'.format(RSS))
print('决定系数为R^2：{}'.format(R2))
print('AIC信息量为：{}'.format(AIC))

#绘制残差图
plt.scatter(Y, ls3)
plt.xlabel('Y')
plt.ylabel('e')
plt.hlines(0.0, 4.5, 8.5, color='black', linestyles='dashed')
plt.show()















"""
Data = pd.read_csv('E:/Downloads/baseball0.csv')

X = Data.drop(['salary'], axis=1)
Y = Data['salary'].values.reshape(-1, 1)

total = 0.0
for i in range(Y.shape[0]):
	Y[i][0] = math.log(Y[i][0])
	total += Y[i][0]
avg = total / len(Y)

Xt = np.transpose(X)
XtX = np.dot(Xt, X)
XtY = np.dot(Xt, Y)
Beta = np.linalg.solve(XtX, XtY)
print(Beta)

Beta1 = np.transpose(Beta)
print(Beta1)
RSS = 0
for i in range(X.shape[0]):
	s = 0
	for j in range(X.shape[1]):
		s += X[i][j] * Beta1[0][j]
	RSS += (s - Y[i][0]) ** 2

TSS = 0
for i in range(Y.shape[0]):
	TSS += (Y[i][0] - avg) ** 2

R2 = 1 - RSS / TSS
AIC = X.shape[0] * math.log(RSS / X.shape[0]) + 2 * 28

print('回归系数为：{}'.format(Beta))
print('残差平方和RSS为：{}'.format(RSS))
print('决定系数为：{}'.format(R2))
print('AIC信息量为：{}'.format(AIC))
"""