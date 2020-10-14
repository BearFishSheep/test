def mineLocation(field):
	ls = []
	for i in range(len(field)):
		for j in range(len(field[i])):
			if field[i][j] == 1:
				ls.append(i)
				ls.append(j)
				break
	return ls
print(mineLocation([[1, 0], [0, 0]]  ))