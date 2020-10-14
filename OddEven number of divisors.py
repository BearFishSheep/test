def oddity(n):
	ls = []
	for i in range(1, n+1):
		if(n % i == 0):
			ls.append(i)
	if len(ls) % 2:
		return 'odd'
	else:
		return 'even'
print(oddity(29))