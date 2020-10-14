# 模拟退火算法
import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

# 随机选取5个初值（27个预测变量对应的0-1向量）
def init():
	ls = np.array([random.randint(0, 1) for i in range(27)])
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
def oneNeighborhood(X, ls, column):
	X_predict = np.array(X[:,0]).reshape((337, 1))	# 先取出第0列（一列都为1）,变维
	for i in range(len(ls)):
		if i != column and ls[i] == 1:
			arr = np.array(X[:,i+1]).reshape((337, 1))
			X_predict = np.c_[X_predict, arr]
	if ls[column] == 0:
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
def display(ls, RSS, R2, AICset):
	print("0-1向量为：{}".format(ls))
	print("残差平方和RSS为：{}".format(min(RSSset)))
	print("决定系数为R^2：{}".format(max(R2set)))
	print("AIC信息量为：{}".format(min(AICset)))

# 作图（AIC与迭代次数的关系）
def drawAic(AICset):
	plt.plot(np.arange(1, 2001), AICset)
	plt.xlabel('times')
	plt.ylabel('AIC')
	plt.show()

def drawTem(m):
	tem = []
	for i in range(len(m)):
		for j in range(m[i]):
			tem.append(0.9 ** i)
	plt.plot(np.arange(1, 2001), tem)
	plt.xlabel('times')
	plt.ylabel('temperature')
	plt.yticks([0, 0.5, 1])
	plt.show()
	

if __name__ == '__main__':
	# Data = toCSV()		# 转换为baseball.csv文件，并读入csv数据
	Data = pd.read_csv('E:/Downloads/baseball0.csv')
	X, Y = X_and_Y(Data)	# 将X,Y处理为矩阵形式，salary的对数以e为底
	AICset = []
	R2set = []
	RSSset = []
	m = [60 for i in range(5)] + [120 for i in range(5)] + [220 for i in range(5)]
	temperature = [0.9**(i) for i in range(15)]
	for j in range(15):
		for step in range(m[j]):
			AIC_predict = []
			R2_predict = []
			RSS_predict = []
			ls = init()
			for column in range(27):
				X_predict = oneNeighborhood(X, ls, column)	# 1-变化邻域
				Beta = solveBeta(X_predict)					# 解出β矩阵
				RSS = calculateRSS(X_predict, Y, Beta)		# 计算残差平方和RSS
				TSS = calculateTSS(Y)						# 计算TSS
				R2, AIC = calculateR2andAIC(X_predict, RSS, TSS)# 计算决定系数R^2和AIC
				AIC_predict.append(AIC)
				R2_predict.append(R2)
				RSS_predict.append(RSS)
			if j == 0 and step == 0:						# 最开始直接插入
				AICset.append(min(AIC_predict))
				R2set.append(max(R2_predict))
				RSSset.append(min(RSS_predict))
			else:
				r = random.random()
				p = math.exp((AICset[-1]-min(AIC_predict)) / temperature[j])
				if r < min(1, p):		# 当前解 < 上一轮的解
					AICset.append(min(AIC_predict))
					R2set.append(max(R2_predict))
					RSSset.append(min(RSS_predict))
				else:					# 当前解 > 上一轮的解
					AICset.append(AICset[-1])
					R2set.append(R2set[-1])
					RSSset.append(RSSset[-1])

	display(ls, RSSset, R2set, AICset)			# 打印信息
	drawAic(AICset)								# 作AIC图
	drawTem(m)									# 作温度图

