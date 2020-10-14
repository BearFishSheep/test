def dig_pow(n, p):
	s = str(n)
	i, sum, t = p+len(s)-1, 0, n
	while i >= p:
		sum = sum + (n%10) ** i
		n = int(n/10)
		i -= 1
	if sum//t == sum/t:
		return sum//t
	return -1
print(dig_pow(46288, 3))