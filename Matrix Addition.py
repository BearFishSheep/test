def matrix_addition(a, b):
	ls = []
	for i in range(len(a)):
		ls1 = []
		for j in range(len(a[i])):
			ls1.append(a[i][j] + b[i][j])
		ls.append(ls1)
	return ls
print(matrix_addition([[1]],[[2]]))