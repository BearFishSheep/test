def data_reverse(data):
	ls = []
	ls1 = []
	i = 0
	while i < len(data):
		k = 0
		s = ''
		while k < 8:
			s += str(data[i])
			k += 1
			i += 1
		ls.append(s)
	k = len(ls) - 1
	while k >= 0:
		for i in ls[k]:
			ls1.append(int(i))
		k -= 1
	return ls1

print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))
			