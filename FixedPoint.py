# # fixed point
# def f(x):
# 	return 7/15 * (9 * x**5 - 10 * x**3)

# e = 1e-8
# j = 0
# ls = [-1, -0.5, 0.0, 0.5, 1]
# for i in ls:
# 	x = i
# 	while True:
# 		y = f(x)
# 		z = f(y)
# 		if z - 2 * y + x == 0.0:
# 			j += 1
# 			print("x{} = {}".format(j, x))
# 			break
# 		x_k1 = x - (y - x) ** 2 / (z - 2 * y + x)
# 		if abs(x_k1 - x) < e:
# 			j += 1
# 			print("x{} = {}".format(j, x_k1))
# 			break
# 		x = x_k1
	
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.001)
# y = (63*x**5 - 70*x**3 + 15*x) / 8
y = (63*5*x**4 - 210*x**2 + 15) / 8
plt.plot(x, y)
plt.hlines(0.0, -1, 1, color='black', linestyles='dashed')
plt.show()
"""
"""
import random

def f(x):
	return (63*x**5 - 70*x**3 + 15*x) / 8

# x_k = -1
x_k = 0
# lam = random.uniform(0, 2/15)
lam = random.uniform(0, 2/2)
while True:
	x_k1 = x_k - lam*f(x_k)
	if abs(x_k1 - x_k) < 1e-8:
		break
	x_k = x_k1
print(x_k1)
print(x_k)
"""

import random
import matplotlib.pyplot as plt
import numpy as np

#返回函数值
def f(x):
	return (63*x**5 - 70*x**3 + 15*x) / 8

#将导数图像画出来
x = np.arange(-1, 1, 0.001)
y = (315*x**4 - 210*x**2 + 15) / 8
plt.plot(x, y)
plt.hlines(0.0, -1, 1, color='black', linestyles='dashed')
plt.show()

#根据图像可得极值
M = [15, -2.5, 1.875, -2.5, 15]

#不动点迭代
e = 1e-8
j = 0
ls = [-1, -0.5, 0, 0.5, 1]
for i in range(len(ls)):
	cnt = 0		#迭代次数
	x_k = ls[i]
	if M[i] >= 0:
		lam = random.uniform(0, 2/M[i])	#λ的值在区间内任取，引入随机数
	else:
		lam = random.uniform(2/M[i], 0)	#同上
	if f(x_k) != 0.0:
		while True:
			cnt += 1
			x_k1 = x_k - lam*f(x_k)
			if abs(x_k1 - x_k) < e:
				break
			x_k = x_k1
		j += 1
		print("x{} = {}，迭代了{}次".format(j, x_k1, cnt))
	else:
		j += 1
		print("x{} = {}，迭代了{}次".format(j, x_k, cnt))