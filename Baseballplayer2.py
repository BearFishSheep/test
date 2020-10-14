# 2-变化邻域的局部搜索
import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

 
#将baseball.dat文件转换为baseball.csv文件
path = 'E:/Downloads/baseball.dat'
data = pd.read_table(path, header=0, sep=' ')
data = data.to_csv('E:/Downloads/baseball.csv', index=False, header=True)


# 读入csv数据
Data = pd.read_csv('E:/Downloads/baseball.csv')


# 随机选取5个初值（27个预测变量对应的0-1向量）
ls = np.array([[random.randint(0, 1) for i in range(27)] for j in range(5)])
print("初始随机选取的5个变量为：{}".format(ls))


# 将X,Y处理为矩阵形式，salary的对数以e为底
X = Data.drop(['salary'], axis=1).values
Y = Data['salary'].values.reshape(-1, 1)
for i in range(Y.shape[0]):
	Y[i][0] = math.log(Y[i][0])


AICset = []
# 开始迭代
for n in range(5):
	for step in range(14):
		for column1 in range(27):
			AIC_predict = []
			for column2 in range(column1+1, 27):
				X_real = np.array(X[:,0]).reshape((337, 1))	# 先取出第0列（一列都为1）,变维
				if ls[n][column1] == 0:
					arr = np.array(X[:,column1+1]).reshape((337, 1))
					X_real = np.c_[X_real, arr]
				if ls[n][column2] == 0:
					arr = np.array(X[:,column2+1]).reshape((337, 1))
					X_real = np.c_[X_real, arr]
				for i in range(len(ls[n])):
					if ls[n][i] == 1 and i != column1 and i != column2:
						arr = np.array(X[:,i+1]).reshape((337, 1))
						X_real = np.c_[X_real, arr]
				
				X_predict = X_real
				
				# 解出β矩阵
				XT = X_predict.transpose()
				XTX = np.dot(XT, X_predict)
				XTY = np.dot(XT, Y)
				Beta = np.linalg.solve(XTX, XTY)

				# 计算残差平方和RSS
				RSS = 0.0
				ls3 = []
				for i in range(X_predict.shape[0]):
					s = 0.0
					for j in range(X_predict.shape[1]):
						s += X_predict[i][j] * Beta[j][0]
					ls3.append(s - Y[i][0])
					RSS += (s - Y[i][0]) ** 2

				TSS, avg = 0.0, 0.0
				avg = Y.sum(axis=0) / Y.shape[0]
				for i in range(Y.shape[0]):
					TSS += (Y[i][0] - avg) ** 2

				# 计算决定系数R^2和AIC
				R2 = 1 - RSS / TSS
				AIC = X_predict.shape[0] * math.log(RSS / X_predict.shape[0]) + 2 * X_predict.shape[1]
				AIC_predict.append(AIC)
			if AIC_predict != []:
				minIndex = AIC_predict.index(min(AIC_predict))	#选取最小的AIC
				AICset.append(-1 * min(AIC_predict))
				if ls[n][minIndex+column1+1] == 1:
					ls[n][minIndex+column1+1] = 0
				else:
					ls[n][minIndex+column1+1] = 1
				if ls[n][column1] == 1:
					ls[n][column1] = 0
				else:
					ls[n][column1] = 1
					
print("0-1向量为：{}".format(ls))
print("回归系数为：{}".format(Beta))
print("残差平方和RSS为：{}".format(RSS))
print("决定系数为R^2：{}".format(R2))
print("AIC信息量为：{}".format(AIC))


plt.figure(figsize=(16, 8))
plt.scatter([i for i in range(1, len(AICset)+1)], AICset)
plt.xlabel('times')
plt.ylabel('-AIC')
plt.show()