def series_sum(n):
	i = 1
	sum = 0
	if n == 0:
		return '0.00'
	while i <= n:
		sum += 1 / (3*i-2)
		i += 1
	s = str(round(sum, 2))
	if len(s) == 3:
		s += '0'
	return s
print(series_sum(1))