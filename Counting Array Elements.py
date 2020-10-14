def count(array):
	dc = {}
	for i in array:
		if i not in dc:
			dc[i] = 1
		else:
			dc[i] += 1
	return dc
print(count(['a', 'a', 'b', 'c', 'a']))