def array_diff(a, b):
	diff=[]
	for i in a:
		if i not in b: #在a中而不在b中，把a中在b中的元素全部删除
			diff.append(i)
	return diff

a=[1,2,2,2,3]
print(array_diff(a,[2]))