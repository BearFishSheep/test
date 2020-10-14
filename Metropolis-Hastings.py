# Metropolis-Hastings算法
# 1.取先验分布为建议分布产生候选值
# ​# 2.计算MH比率 R = (L(y|λ) * f(λ*)) / (L(y|λ*) * f(λ))
# 3.判断是否接受，如果r-U(0, 1)，R > r，λ = λ*；否则不更新
# 4.重复上述操作进行10000次迭代
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 将coal.dat文件转换为coal.csv文件，并读入csv数据
def toCSV():
	data = pd.read_table('E:/Downloads/coal.dat', header=0, sep=' ')
	data = data.to_csv('E:/Downloads/coal.csv', index=False, header=True)
	Data = pd.read_csv('E:/Downloads/coal.csv')
	return Data

# 获得disasters这一列数据
def getY(Data):
	Y = Data['disasters'].values
	return Y

# 阶乘
def Fact(k):
	if k == 0:
		return 1
	else:
		return k * Fact(k - 1)

# 泊松分布
def Poisson(lam, k):
	return math.exp(-lam) * pow(lam, k) / Fact(k)

# Metropolis-Hastings算法
def MH(Y):
	alpha, beta = 3, 1
	lambda_list = []
	lam = np.random.gamma(alpha)	#产生候选值
	for step in range(10000):
		lambda_list.append(lam)
		lam_1 = np.random.gamma(alpha)
		p1, p2 = 1, 1
		for y in Y:
			p1 *= Poisson(lam, y)
			p2 *= Poisson(lam_1, y)
		f1 = getGamma(alpha, beta, lam)
		f2 = getGamma(alpha, beta, lam_1)
		acceptance = min(1, (p2 * f1) / (p1 * f2))
		r = random.random()		# [0, 1)之间一个随机浮点数
		if r < acceptance:
			lam = lam_1
	return lam, lambda_list

# 先验分布服从伽马分布Γ(3, 1)
def getGamma(alpha, beta, lam):
	if lam > 0:
		return pow(lam, alpha - 1) * math.exp(-beta * lam) / (pow(beta, alpha) * Fact(alpha - 1))
	else:
		return 0

# 画λ的样本轨迹图
def draw1(lambda_list):
	plt.plot(np.arange(1, 10001), lambda_list)
	plt.xlabel('t')
	plt.ylabel('lambda')
	plt.show()

# 画直方图
def drawHist(Y):
	bins = np.linspace(min(Y), max(Y), max(Y) - min(Y))
	plt.hist(Y, bins)
	plt.xlabel('lambda')
	plt.ylabel('times')
	plt.show()

if __name__ == '__main__':
	Data = toCSV()		# 转换为coal.csv文件，并读入csv数据
	# Data = pd.read_csv('E:/Downloads/coal.csv')
	Y = getY(Data)		# 获取disasters这一列数据
	lam, lambda_list = MH(Y)
	print(lam)
	draw1(lambda_list)
	drawHist(Y)
	

