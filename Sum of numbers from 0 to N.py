def show_sequence(n):
	s = ''
	if n < 0:
		s = s + str(n) + '<0'
	elif n == 0:
		s = '0=0'
	else:
		sum = 0
		ls = []
		for i in range(n+1):
			sum += i
			ls.append(str(i))
		s = '+'.join(ls)
		s = s + ' = ' + str(sum)
	return s
print(show_sequence(-6))