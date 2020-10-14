def filter_list(l):
	ls = []
	for i in l:
		if type(i) == type(1):
			ls.append(i)
	return ls

print(filter_list([1,2,'a','b']))