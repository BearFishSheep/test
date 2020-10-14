def revrot(strng, sz):
	s = ''
	sum1 = 0
	if sz <= 0 or len(strng) == 0 or sz > len(strng):
		return s
	k = sz -1
	while k >= 0:
		s += strng[k]
	for i in strng:
		sum1 += int(strng)**3
	if sum % 2:
		k = len(strng) - 1
		while k >= sz:
			s += strng[k]
	else:
		s