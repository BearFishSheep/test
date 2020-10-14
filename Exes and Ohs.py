def xo(s):
	s = s.lower()
	k1 = s.count('x')
	k2 = s.count('o')
	if k1 == k2:
		return True
	else:
		return False

print(xo('asdf'))