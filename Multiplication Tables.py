def multiplication_table(row, col):
	ls = []
	for i in range(1, row+1):
		ls1 = []
		for j in range(1, col+1):
			ls1.append(j*i)
		ls.append(ls1)
	return ls
print(multiplication_table(2, 3))