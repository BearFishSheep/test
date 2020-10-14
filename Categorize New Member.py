def openOrSenior(data):
	s = []
	for i in data:
		a, b = i[0], i[1]
		if a < b:
			a, b = b, a
		if a >= 55 and b > 7:
			s.append('Senior')
		else:
			s.append('Open')
	return s
print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))