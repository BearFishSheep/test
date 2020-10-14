def largest(n, xs):
	xs.sort()
	return xs[-n:]
print(largest(3, [7,1,2,5,4,6,3]))