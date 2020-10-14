# 1-变化邻域的局部搜索
import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

# 随机选取5个初值（27个预测变量对应的0-1向量）
def Init():
	ls = np.array([[random.randint(0, 1) for i in range(27)] for j in range(5)])
	print("初始随机选取的5个变量为：{}".format(ls))
	return ls

# 将baseball.dat文件转换为baseball.csv文件，并读入csv数据
def toCSV():
	data = pd.read_table('E:/Downloads/baseball.dat', header=0, sep=' ')
	data = data.to_csv('E:/Downloads/baseball.csv', index=False, header=True)
	Data = pd.read_csv('E:/Downloads/baseball.csv')
	return Data

# 将X,Y处理为矩阵形式，salary的对数以e为底
def X_and_Y(Data):
	X = Data.drop(['salary'], axis=1).values
	Y = Data['salary'].values.reshape(-1, 1)
	for i in range(Y.shape[0]):
		Y[i][0] = math.log(Y[i][0])
	return X, Y

# 1-变化邻域
def oneNeighborhood(X, ls, n, column):
	X_predict = np.array(X[:,0]).reshape((337, 1))	# 先取出第0列（一列都为1）,变维
	for i in range(len(ls[n])):
		if i != column and ls[n][i] == 1:
			arr = np.array(X[:,i+1]).reshape((337, 1))
			X_predict = np.c_[X_predict, arr]
	if ls[n][column] == 0:
		arr = np.array(X[:,column+1]).reshape((337, 1))
		X_predict = np.c_[X_predict, arr]
	return X_predict

# 解出β矩阵
def solveBeta(X_predict):
	XT = X_predict.transpose()
	XTX = np.dot(XT, X_predict)
	XTY = np.dot(XT, Y)
	Beta = np.linalg.solve(XTX, XTY)
	return Beta

# 计算残差平方和RSS
def calculateRSS(X_predict, Y, Beta):
	RSS = 0.0
	ls3 = []
	for i in range(X_predict.shape[0]):
		s = 0.0
		for j in range(X_predict.shape[1]):
			s += X_predict[i][j] * Beta[j][0]
		ls3.append(s - Y[i][0])
		RSS += (s - Y[i][0]) ** 2
	return RSS

# 计算残差平方和TSS
def calculateTSS(Y):
	TSS, avg = 0.0, 0.0
	avg = Y.sum(axis=0) / Y.shape[0]
	for i in range(Y.shape[0]):
		TSS += (Y[i][0] - avg) ** 2
	return TSS

# 计算决定系数R^2和AIC
def calculateR2andAIC(X_predict, RSS, TSS):
	R2 = 1 - RSS / TSS
	AIC = X_predict.shape[0] * math.log(RSS / X_predict.shape[0]) + 2 * X_predict.shape[1]
	return R2, AIC

# 打印信息
def display(ls, Beta, RSS, R2, AIC):
	print("0-1向量为：{}".format(ls))
	print("回归系数为：{}".format(Beta))
	print("残差平方和RSS为：{}".format(RSS))
	print("决定系数为R^2：{}".format(R2))
	print("AIC信息量为：{}".format(AIC))

# 作图（AIC与迭代次数的关系）
def drawPic(AICset):
	a = np.arange(1, 71)
	plt.scatter(a, AICset)
	plt.xlabel('times')
	plt.ylabel('-AIC')
	plt.xticks([1, 14, 28, 42, 56, 70])
	plt.yticks([360, 380, 400, 420])
	# plt.axis([1, 70, 360, 420])	# 设置起点终点
	plt.show()

if __name__ == '__main__':
	ls = Init()				# 初始化
	# Data = toCSV()		# 转换为baseball.csv文件，并读入csv数据
	Data = pd.read_csv('E:/Downloads/baseball0.csv')
	X, Y = X_and_Y(Data)	# 将X,Y处理为矩阵形式，salary的对数以e为底

	AICset = []
	# 开始迭代   5 * 14 * 27 = 1890
	for n in range(5):
		for step in range(14):
			AIC_predict = []
			for column in range(27):
				X_predict = oneNeighborhood(X, ls, n, column)	# 1-变化邻
				Beta = solveBeta(X_predict)						# 解出β矩阵
				RSS = calculateRSS(X_predict, Y, Beta)			# 计算残差平方和RSS
				TSS = calculateTSS(Y)							# 计算TSS
				R2, AIC = calculateR2andAIC(X_predict, RSS, TSS)# 计算决定系数R^2和AIC
				AIC_predict.append(AIC)
			minIndex = AIC_predict.index(min(AIC_predict))		#选取最小的AIC
			AICset.append(-min(AIC_predict))

			if ls[n][minIndex] == 1:
				ls[n][minIndex] = 0
			else:
				ls[n][minIndex] = 1

	
	display(ls, Beta, RSS, R2, AIC)		# 打印信息
	drawPic(AICset)						# 作图


