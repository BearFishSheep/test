x = 0
def persistence(n):
	global x  #返回完x要将其清零，不然这个全局变量一直累加
	if n < 10:  #会导致只有第一个结果是对的，后面都是错的
		return x
	while True:
		sum = 1
		while n:
			sum *= n%10
			n = int(n/10)
		x += 1
		if sum < 10:
			t = x
			x = 0
			return t
		else:
			return persistence(sum)
print(persistence(999))
