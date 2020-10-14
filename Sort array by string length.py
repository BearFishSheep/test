def sort_by_length(arr):
	ls = []
	ls1 = []
	for i in arr:
		ls.append(len(i))
	ls = sorted(ls)
	for i in ls:
		for j in arr:
			if i == len(j):
				ls1.append(j)
				break
	return ls1
print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))