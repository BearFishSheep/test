import sympy
import numpy as np

x1, x2, x3, x4 = sympy.symbols("x1 x2 x3 x4")
f1 = x1 + x2 -2
f2 = x1*x3 + x2*x4 - 2/3
f3 = x1*x3**2 + x2*x4**2 - 2/5
f4 = x1*x3**3 + x2*x4**3 - 2/7

X = sympy.Matrix([1, 1, 1/3, 1/3])	#给X赋初值
f = sympy.Matrix([f1, f2, f3, f4])	#初始f
x = sympy.Matrix([x1, x2, x3, x4])
df = f.jacobian(x)					#导数（雅可比矩阵）
cnt = 0								#迭代次数

while True:
	f_num = np.zeros((4, 1))
	df_num = np.zeros((4, 4))

	for i in range(4):
		f_num[i] = np.array(float(f[i].evalf(subs={x1:X[0], x2:X[1], x3:X[2], x4:X[3]})))
		for j in range(4):
			df_num[i][j] = np.array(float(df.row(i)[j].evalf(subs={x1:X[0], x2:X[1], x3:X[2], x4:X[3]})))
	
	#防止雅可比矩阵行列式接近0而无法求逆，J = J + 0.05 * I
	try:
		deltaX = np.linalg.solve(df_num, -1 * f_num)
	except:
		df_num += 0.05 * np.eye(4)	#单位矩阵
		deltaX = np.linalg.solve(df_num, f_num)
	
	X = np.array(X) + deltaX
	cnt += 1
	print("第{}次迭代：{}".format(cnt, X))
	print("---------------------------------")

	if np.linalg.det(np.dot(f_num.transpose(), f_num)) <= 1e-8:
		break