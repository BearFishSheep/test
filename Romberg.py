from math import sin
from math import pi
import numpy as np

# 定义常量
a, b = 0, pi / 2		# a是下限，b是上限
e, k = 1e-8, 0			# e是精度，k是二分次数
T = np.zeros(shape=(5, 5))	# 构造一个5*5的矩阵

# 算法第一步，先算出T[0][0]
T[0][0] = ((b-a) / 2 * (sin(a) + sin(b)))

# 理查森加速外推
while True:
	# 复化梯形公式，步长变为一半
	k += 1				# 二分次数加1，步长变为原来的一半
	T[k][0] = T[k-1][0] / 2
	for i in range(1, pow(2, k-1)+1):
		T[k][0] += (b-a) / pow(2,k) * sin(a + (i-1/2) * (b-a) / pow(2, k-1))
	# 加速
	m = 1				# m是加速次数，每次都从Simpson开始
	for i in range(m, k+1):
		T[k][i] = (pow(4, m) * T[k][i-1] - T[k-1][i-1]) / (pow(4, m) - 1)
		m += 1
	# 判断精度是否达到e，若达到则退出循环
	if(abs(T[k][k] - T[k-1][k-1]) < e):
		break

print(T)
	