#返回函数值
def f(x):
	return (63*x**5 - 70*x**3 + 15*x) / 8

#返回导数值
def df(x):
	return (315*x**4 - 210*x**2 + 15) / 8

e = 1e-8	#精度
j = 0		#解的个数
ls = [-1, -0.5, 0, 0.5, 1]

#牛顿迭代法
for i in range(len(ls)):
	cnt = 0		#迭代次数
	x_k = ls[i]
	if f(x_k) != 0.0:
		while True:
			cnt += 1
			x_k1 = x_k - f(x_k) / df(x_k)
			if abs(x_k1 - x_k) < e:
				break
			x_k = x_k1
		j += 1
		print("x{} = {}，迭代了{}次".format(j, x_k1, cnt))
	else:
		j += 1
		print("x{} = {}，迭代了{}次".format(j, x_k, cnt))
	
