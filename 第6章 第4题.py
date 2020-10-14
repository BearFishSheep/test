def fun(ls):
	for i in range(len(ls)):
		c=ls[i]
		ls.pop[i]
		if c in ls:
			return True
	else:
		return False

ls=[1, 2, 3, 4, 1, 5]

if fun(ls):
	print("有")
else:
	print("无")