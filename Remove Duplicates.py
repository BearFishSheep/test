def unique(integers):
	if integers == []:
		return []
	ls = []
	for i in integers:
		if i not in ls:
			ls.append(i)
	return ls
print(unique([1, 5, 2, 0, 2, -3, 1, 10]))