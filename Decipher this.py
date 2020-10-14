def decipher_this(string):
	s = string.split()
	for i in s:
		s1 = ''
		for j in i:
			if '0' <= j <= '9':
				s1 += j