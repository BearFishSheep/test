def countBits(n):
	x = 0
	while n:
		if n % 2:
			x += 1
		n = int(n / 2)
	return x
print(countBits(0))