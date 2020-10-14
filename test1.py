import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def drawHist(Y):
	bins = np.linspace(min(Y), max(Y), max(Y) - min(Y))
	plt.hist(Y, bins)
	plt.xlabel('lambda')
	plt.ylabel('times')
	plt.show()

Data = pd.read_csv('E:/Downloads/coal.csv')
Y = Data['disasters'].values
drawHist(Y)

'''
import numpy as np

ls = []
for i in range(10):
	ls.append(1)
print(ls)
'''

'''
def fact(k):
	if k == 0:
		return 1
	else:
		return k * fact(k - 1)

t = fact(4)
print(t)
'''
'''
import numpy as np

# shape, scale = 2., 2. 
ls = []
for i in range(10):
	ls.append(np.random.gamma(3, 1))
print(ls)
'''

'''
import numpy as np

P = np.matrix([[1/4, 3/4, 0], [1/3, 1/3, 1/3], [0, 1/4, 3/4]])
Init = np.matrix([1/4, 1/2, 1/4])
# 方法 1
P2 = np.dot(P, P)
print(P2)
result1 = np.dot(Init, P2)

# 方法 2
Init_temp = np.dot(Init, P)
result2 = np.dot(Init_temp, P)

print(result1)
print(result2)
'''

# print(7/64 + 2/9 + 13/4/48)
# print(9/64 + 1/18 + 1/64)

# print(1, 2, 3, 4, 5, sep=".", end="\n\n")
'''
import numpy as np
import matplotlib.pyplot as plt
m = [60 for i in range(5)] + [120 for i in range(5)] + [220 for i in range(5)]
tem = []
for i in range(len(m)):
	for j in range(m[i]):
		tem.append(0.9 ** i)
plt.plot(np.arange(1, 2001), tem)
plt.xlabel('times')
plt.ylabel('temperature')
plt.yticks([0, 0.5, 1])
plt.show()
'''
# m = [60 for i in range(5)] + [120 for i in range(5)] + [220 for i in range(5)]
# tem = [0.9 ** j for i in range(m[j]) for j in range(len(m))]
# print(tem)



# m = [i for i in range(10)]
# a = [i  if i % 2 == 0 else 13 for i in range(10)]
'''
# print(a)
import numpy as np
m = [60 for i in range(5)] + [120 for i in range(5)] + [220 for i in range(5)]
tem = []
# for i in range(len(m)):
# 	for j in range(m[i]):
# 		tem.append(0.9 ** i)
tem = np.array([[0.9 ** j for i in range(m[j])] for j in range(len(m))]).reshape(-1)
print(tem)
'''

'''
import random
print(random.random())	# 0-1之间的一个实数，0 <= x < 1
print(random.uniform(0, 1))	# 包括端点值
'''

# print(6 * (0.9**14))
# temperature = [0.9**(i) for i in range(15)]
# print(temperature)
# s1 = [60 for i in range(5)]
# s2 = [120 for i in range(5)]
# s3 = [220 for i in range(5)]
# s = s1 + s2 + s3
# print(s)

# a = [1, 2, 3]
# b = [3, 4, 5]
# print(a + b)	# 合并列表


# import numpy as np

# T1 = np.matrix([[1, 1], [0.7415557, 0.1155871]])
# T2 = np.matrix([[2], [2/3]])

# Beta = np.linalg.solve(T1, T2)

# print(np.dot(T1, Beta))

"""
from math import sqrt

# a = -116600377/134217728 - 17617351*sqrt(-2*sqrt(7)/21 + 1/3)/134217728
# a = -36450163*sqrt(2*sqrt(7)/21 + 1/3)/134217728 + 97767565*sqrt(-2*sqrt(7)/21 + 1/3)/134217728
a = 13399247*sqrt(2*sqrt(7)/21 + 1/3)/33554432 + 20155185/33554432
print(a)
"""
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.001)
# y = (63*x**5 - 70*x**3 + 15*x) / 8
y = (63*5*x**4 - 210*x**2 + 15) / 8
plt.plot(x, y)
plt.hlines(0.0, -1, 1, color='black', linestyles='dashed')
plt.show()
'''


# for i in range(1, 5):
# 	x0, x1, x2, x3 = 2, 1.6667, 1.5911, 1.5874
# 	t1 = abs(x1-x2) / abs(x0-x1)**i
# 	t2 = abs(x2-x3) / abs(x1-x2)**i
# 	print(t1 -t2)
# 	print("\n")


# import sympy
# import numpy as np


# X = np.array([[1, 1, 1/3, 1/3]])	#给X赋初值


# print(X[2][0])


'''
import pandas as pd
import numpy as np

Data = pd.read_csv('E:/Downloads/baseball0.csv')

X = Data.drop(['salary'], axis=1).values
Y = Data['salary'].values.reshape(-1, 1)

sample = np.zeros((337, 2))
a = 1
print(X.shape)
print(Y.shape)
arr = np.array(X[:,a])	#取出某一列
arr = arr.reshape((337, 1))	#变维
print(arr.shape)
# ls = [X[:,a]]
# one = np.r_[sample, ls]
# print(sample.shape)
# print(one.shape)
# print(one)
# print(one[2][5])

one = np.c_[sample, arr]
print("1...")
print(one)
two = one
print("2...")
print(two)

two = np.c_[arr, arr]
print("3...")
print(two)
print("4...")
print(one)
'''

'''
ls = [0 for i in range(27)]	#列表推导式
print(ls)
print(len(ls))
'''

'''
import random

r = []
cnt = 0
for i in range(5):
	ran = random.randint(1, 5)
	while True:
		if ran in r:
			ran = random.randint(1, 5)
			cnt += 1
		else:
			break
	r.append(ran)

print("重复次数为：{}".format(cnt))
print("随机列表：{}".format(r))
# ls.sort()
# ls = sorted(ls)
# index = ls.index(min(ls))	#获取最小元素的下标
# print(index)
'''
'''
import random
import numpy as np

ls = np.array([[random.randint(0, 1) for i in range(27)] for j in range(5)])
r = []
for i in range(5):
	t = []
	for j in range(27):
		if ls[i][j] == 1:
			t.append(j)
	r.append(t)
print(ls)
print(r)
print(r[0])
'''

'''
import itertools
a = [1, 2, 3]
b = [5, 6, 7, 1]
x = list(itertools.combinations(b, 2))
for i in x:
	m, n = i
	print(str(m) + "和" + str(n))
'''
'''
import numpy as np
import matplotlib.pyplot as plt

y1 = [i for i in range(10)]
y2 = [2*i for i in range(10)]

plt.plot(np.arange(0, 1, 0.1), y1)
plt.plot(np.arange(0, 1, 0.1), y2)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlabel('x2')
plt.show()

# a = np.arange(1, 71)
# print(a)
'''