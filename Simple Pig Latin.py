def pig_it(text):
	ls = text.split()
	ls1 = []
	s = ''
	s1 = ''
	for i in ls:
		s = ''
		if len(i) == 1:
			if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
				s = s + i + 'ay'
			else:
				s += i
			ls1.append(s)
		else:
			for j in range(1, len(i)):
				s += i[j]
			s = s + i[0] +'ay'
			ls1.append(s)
	s1 = ' '.join(ls1)
	return s1

print(pig_it('This is my string !'))