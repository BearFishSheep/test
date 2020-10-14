def Descending_Order(num):
	s = str(num)
	ls = list(s)
	ls = sorted(ls, reverse = True)
	s = ''.join(ls)
	a = int(s)
	return a

print(Descending_Order(21445))