def square_digits(num):
	s = str(num)
	ls = list(s)
	ls1 = []
	for i in ls:
		ls1.append(str(int(i)**2))
	s = ''.join(ls1)
	a = int(s)
	return a

print(square_digits(9119))