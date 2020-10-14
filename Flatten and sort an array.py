def flatten_and_sort(array):
	s = []
	if array == []:
		return s
	for i in array:
		if i != []:
			for j in i:
				s.append(j)
	s.sort()
	return s
print(flatten_and_sort([[3, 2, 1], [], [6, 4, 5]]))