def narcissistic(value):
	total, t = 0, value
	ls = []
	while t:
		ls.append(t%10)
		t = int(t/10)
#注意：reversed()函数返回的是一个迭代器，
# 而不是一个List，所以需要list函数转换一下
	ls1 = list(reversed(ls))
	for i in ls1:
		total += i ** len(ls1)
	if total == value:
		return True
	else:
		return False
print(narcissistic(153))