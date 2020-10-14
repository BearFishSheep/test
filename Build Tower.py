def tower_builder(n):
	ls = []
	for i in range(1, n+1):
		s = ''
		j = n - i
		while j > 0:
			s += ' '
			j -= 1
		for k in range(2*i - 1):
			s += '*'
		j = n - i
		while j > 0:
			s += ' '
			j -= 1
		ls.append(s)
	return ls
print(tower_builder(4))