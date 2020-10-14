def highest_rank(arr):
	s = set(arr)
	index = arr[0]
	for i in s:
		if arr.count(i) > arr.count(index):
			index = i
		if arr.count(i) == arr.count(index) and i > index:
			index = i
	return index
print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))