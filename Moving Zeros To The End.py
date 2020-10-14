def move_zeros(array):
	ls = []
	ls1 = []
	if array == []:
		return ls
	for i in array:
		#isinstance(object, type)判断此对象是否为某一类型
		if i != 0 or isinstance(i, bool):
			ls.append(i)
		else:
			ls1.append(i)
	ls = ls + ls1
	return ls

print(move_zeros([0,1,None,2,False,1,0]))