def fun(ls):
	for i in range(len(ls)):
		c=ls[i]
		ls.pop(i)  #pop的返回值是那个被删除的元素
		if c in ls:
			return True
		i-= 1
	else:
		return False

ls=[1, 2, 3, 4, 5]

if fun(ls):
	print("有重复元素")
else:
	print("无重复元素")
