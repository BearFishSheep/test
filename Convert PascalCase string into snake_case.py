def to_underscore(s):
	a = s.split('_')
	s1 = ''
	for i in a:
		b = list(i)
		if 'a' <= b[0] <= 'z':
			b[0] = chr(ord(b[0])-32)
		s1 += ''.join(b)
	return s1
print(to_underscore('app7_test'))