from sympy import symbols
from sympy import solve
from sympy import diff


x = symbols('x')
f = (63 * x**5 - 70 * x**3 + 15 * x) / 8
g = diff(f)		#对f求导

m = solve(g)	#m列表是g(x) = 0的解
m.insert(0, -1)
m.append(1)
m = sorted(m)	#给m排序

e = 1e-8		#精度
j = 0			#解的个数
for i in range(len(m) - 1):
	cnt = 0		#迭代次数
	a, b = m[i], m[i+1]
	while True:
		mid = (a + b) / 2
		A = f.evalf(subs = {x:a})
		Mid = f.evalf(subs = {x:mid})
		if Mid == 0:
			break
		cnt += 1
		if A * Mid < 0:
			b = mid
		else:
			a = mid
		if abs(b - a) < e:
			break
	j += 1
	print("x{} = {}，迭代了{}次".format(j, float(mid), cnt))
