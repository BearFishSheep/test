def find_uniq(arr):
	s=set(arr)  #让列表变成集合，过滤掉重复元素
	for i in s:
		if arr.count(i) == 1:
			return i

ls=[1,1,1,2,1,1]
print(find_uniq(ls))