def accum(s):
	ls = list(s)
	ls1 = []
	s2 = ''
	s3 = ''
	if len(ls) == 1:
		s3 += ls[0].upper()
	elif len(ls) == 2:
		s3 = s3 + ls[0].upper() + '-' + ls[1].upper() + ls[1].lower()
	else:
		ls1.append(ls[0].upper())
		s2 = ls[1].upper() + ls[1].lower()
		ls1.append(s2)
		for i in range(2, len(ls)):
			s2 = ''
			s2 += ls[i].upper()
			for j in range(1, i+1):
				s2 += ls[i].lower()
			ls1.append(s2)
		s3 = '-'.join(ls1)
	return s3

print(accum('cwaa'))