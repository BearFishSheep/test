def to_weird_case(s):
	ls = s.split()
	ls1 = []
	for i in ls:
		s1 = ''
		for k in range(len(i)):
			if k % 2 == 0:
				s1 += i[k].upper()
			else:
				s1 += i[k]
		ls1.append(s1)
	s1 = ' '.join(ls1)
	return s1
print(to_weird_case('Weird string case'))